"""Synthetic SQLite decision experiments; prints JSON, uses temporary databases only.

Run with Python 3.11+. This verifies engineering mechanisms, not prompt efficacy.
"""

import json
import platform
import random
import sqlite3
import statistics
import tempfile
import time
from pathlib import Path


def deduplication(root):
    results = {}
    for constrained in (False, True):
        path = root / f'jobs-{constrained}.sqlite'
        left = sqlite3.connect(path, isolation_level=None)
        right = sqlite3.connect(path, isolation_level=None)
        try:
            unique = ', UNIQUE(tenant, request_key)' if constrained else ''
            left.execute('CREATE TABLE jobs(id INTEGER PRIMARY KEY, '
                         f'tenant TEXT NOT NULL, request_key TEXT NOT NULL{unique})')
            # Force a valid overlapping-request schedule without timing-dependent threads:
            # both reads complete before either request writes, with no spanning transaction.
            reads = [conn.execute('SELECT id FROM jobs WHERE tenant=? AND request_key=?',
                                  ('a', 'retry-1')).fetchall() for conn in (left, right)]
            outcomes = []
            for conn in (left, right):
                try:
                    conn.execute('INSERT INTO jobs(tenant, request_key) VALUES (?, ?)',
                                 ('a', 'retry-1'))
                    outcomes.append('inserted')
                except sqlite3.IntegrityError:
                    outcomes.append('duplicate rejected')
            ids = left.execute('SELECT id FROM jobs WHERE tenant=? AND request_key=?',
                               ('a', 'retry-1')).fetchall()
            left.execute('INSERT INTO jobs(tenant, request_key) VALUES (?, ?)',
                         ('b', 'retry-1'))
            results['unique' if constrained else 'check_then_insert'] = {
                'initial_reads': reads, 'write_outcomes': outcomes,
                'same_key_job_ids': [row[0] for row in ids],
                'other_tenant_rows': left.execute(
                    'SELECT count(*) FROM jobs WHERE tenant=?', ('b',)).fetchone()[0],
            }
            assert reads == [[], []]
            assert len(ids) == (1 if constrained else 2)
        finally:
            left.close()
            right.close()
    return results


def exact_lookup():
    conn = sqlite3.connect(':memory:')
    try:
        conn.execute('CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT NOT NULL)')
        conn.executemany('INSERT INTO users(name) VALUES (?)', [('Ada',), ("O\'Brien",)])
        inputs = ['Ada', "O\'Brien", "\' OR 1=1 --", 'missing']
        results = []
        for value in inputs:
            try:
                unsafe = conn.execute(f"SELECT id FROM users WHERE name = '{value}'").fetchall()
            except sqlite3.OperationalError as error:
                unsafe = {'error': str(error)}
            bound = conn.execute('SELECT id FROM users WHERE name = ?', (value,)).fetchall()
            results.append({'input': value, 'interpolated': unsafe, 'bound': bound})
        assert [row['bound'] for row in results] == [[(1,)], [(2,)], [], []]
        assert results[2]['interpolated'] == [(1,), (2,)]
        return results
    finally:
        conn.close()


def index_tradeoff(root):
    rng = random.Random(810)
    tags = [f'tag-{rng.randrange(997):04d}' for _ in range(400)]
    rows = [(i, f'tag-{i % 997:04d}', 'x' * 80) for i in range(20000)]
    inserted = [(i, f'tag-{i % 997:04d}', 'x' * 80) for i in range(20000, 21000)]
    query = 'SELECT id FROM events WHERE tag = ? ORDER BY id'
    results = {'scan': [], 'index': []}
    for repetition in range(5):
        # Alternate order so one variant is not always run first.
        order = (False, True) if repetition % 2 == 0 else (True, False)
        observed = {}
        for indexed in order:
            conn = sqlite3.connect(root / f'events-{repetition}-{indexed}.sqlite')
            try:
                conn.execute('PRAGMA journal_mode=DELETE')
                conn.execute('PRAGMA synchronous=FULL')
                conn.execute('CREATE TABLE events(id INTEGER PRIMARY KEY, tag TEXT, body TEXT)')
                conn.executemany('INSERT INTO events VALUES (?, ?, ?)', rows)
                if indexed:
                    conn.execute('CREATE INDEX events_tag ON events(tag)')
                conn.commit()
                pages = conn.execute('PRAGMA page_count').fetchone()[0]
                page_size = conn.execute('PRAGMA page_size').fetchone()[0]
                for tag in tags[:10]:
                    conn.execute(query, (tag,)).fetchall()
                start = time.perf_counter()
                answers = [conn.execute(query, (tag,)).fetchall() for tag in tags]
                lookup_ms = (time.perf_counter() - start) * 1000
                observed[indexed] = answers
                start = time.perf_counter()
                with conn:
                    conn.executemany('INSERT INTO events VALUES (?, ?, ?)', inserted)
                insert_ms = (time.perf_counter() - start) * 1000
                results['index' if indexed else 'scan'].append({
                    'repetition': repetition + 1,
                    'lookup_400_ms': round(lookup_ms, 3),
                    'insert_1000_ms': round(insert_ms, 3),
                    'database_bytes_before_inserts': pages * page_size,
                    'query_plan': [row[3] for row in conn.execute(
                        'EXPLAIN QUERY PLAN ' + query, (tags[0],))],
                    'rows_after_inserts': conn.execute('SELECT count(*) FROM events').fetchone()[0],
                })
                assert results['index' if indexed else 'scan'][-1]['rows_after_inserts'] == 21000
            finally:
                conn.close()
        assert observed[False] == observed[True]
    summary = {}
    for label, samples in results.items():
        summary[label] = {
            key: round(statistics.median(sample[key] for sample in samples), 3)
            for key in ('lookup_400_ms', 'insert_1000_ms', 'database_bytes_before_inserts')
        }
    return {'seed': 810, 'repetitions': 5, 'warmup_lookups': 10,
            'same_lookup_results_all_repetitions': True, 'samples': results, 'medians': summary}


def main():
    with tempfile.TemporaryDirectory(prefix='engineering-partner-') as directory:
        root = Path(directory)
        result = {
            'environment': {'python': platform.python_version(), 'sqlite': sqlite3.sqlite_version,
                            'platform': platform.platform()},
            'deduplication': deduplication(root),
            'exact_lookup': exact_lookup(),
            'index_tradeoff': index_tradeoff(root),
        }
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
