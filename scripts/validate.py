"""Check repository conventions; host validators remain authoritative."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check(condition, message):
    if not condition:
        raise ValueError(message)


def load(path):
    return json.loads((ROOT / path).read_text())


def validate():
    canonical = load('plugin.json')
    check(canonical['$schema'] == 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json', 'Unexpected portable schema')
    check(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', canonical['name']), 'Invalid plugin name')
    check(re.fullmatch(r'\d+\.\d+\.\d+', canonical['version']), 'Use a stable major.minor.patch version')
    for path in ['.claude-plugin/plugin.json', '.cursor-plugin/plugin.json']:
        manifest = load(path)
        for key in ['name', 'version', 'description', 'author', 'license', 'keywords']:
            check(manifest[key] == canonical[key], f'{path}: {key} differs from plugin.json')
    check(load('.cursor-plugin/plugin.json')['skills'] == './skills/', 'Cursor must share root skills')
    for path in ['.claude-plugin/marketplace.json', '.cursor-plugin/marketplace.json', '.agents/plugins/marketplace.json']:
        market = load(path)
        check(market['name'] == canonical['name'], f'{path}: inconsistent marketplace name')
        check(len(market['plugins']) == 1, f'{path}: expected one plugin')
        entry = market['plugins'][0]
        check(entry['name'] == canonical['name'], f'{path}: inconsistent plugin name')
        source = entry['source']
        if isinstance(source, dict):
            check(source == {'source': 'local', 'path': './'}, f'{path}: unexpected source')
            check(entry['policy'] == {'installation': 'AVAILABLE', 'authentication': 'ON_INSTALL'}, f'{path}: unexpected policy')
            check(entry['category'] == 'Productivity', f'{path}: unexpected category')
        else:
            check(source == './', f'{path}: plugin must point to repository root')
    count = 0
    for directory in sorted((ROOT / 'skills').iterdir()):
        if directory.name.startswith('.'):
            continue
        check(directory.is_dir(), f'{directory.name}: expected a skill directory')
        check(not directory.is_symlink(), f'{directory.name}: skills must live in this repository')
        check(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', directory.name), f'{directory.name}: invalid skill name')
        skill = directory / 'SKILL.md'
        check(skill.is_file(), f'{directory.name}: missing SKILL.md')
        text = skill.read_text()
        # This repository deliberately uses simple, single-line frontmatter.
        match = re.match(r'\A---\n(.*?)\n---\n(.+)', text, re.S)
        check(match, f'{directory.name}: missing frontmatter or body')
        fields = {}
        for line in match[1].splitlines():
            key, separator, value = line.partition(':')
            check(separator and key not in fields, f'{directory.name}: invalid or duplicate metadata')
            fields[key] = value.strip().strip('\"\'')
        check(fields.get('name') == directory.name, f'{directory.name}: name must match directory')
        check(bool(fields.get('description')), f'{directory.name}: description is required')
        check('Replace these steps' not in text, f'{directory.name}: unfinished template')
        count += 1
    print(f'Validated manifests, marketplaces, and {count} skill(s).')
    if not count:
        print('Scaffold only: no installable skills yet.')


if __name__ == '__main__':
    try:
        validate()
    except (ValueError, KeyError, OSError, TypeError) as error:
        print(f'Validation failed: {error}', file=sys.stderr)
        sys.exit(1)
