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


def validate_plugin(plugin_path):
    canonical = load(plugin_path / 'plugin.json')
    check(canonical['$schema'] == 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json', 'Unexpected portable schema')
    check(canonical['name'] == plugin_path.name, 'Plugin name must match directory')
    check(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', canonical['name']), 'Invalid plugin name')
    check(re.fullmatch(r'\d+\.\d+\.\d+', canonical['version']), 'Use a stable major.minor.patch version')
    for host in ['.claude-plugin', '.cursor-plugin']:
        path = plugin_path / host / 'plugin.json'
        manifest = load(path)
        for key in ['name', 'version', 'description', 'author', 'license', 'keywords', 'repository', 'homepage']:
            check(manifest[key] == canonical[key], f'{path}: {key} differs from plugin.json')
    check(load(plugin_path / '.cursor-plugin/plugin.json')['skills'] == './skills/', 'Cursor must share plugin skills')
    count = 0
    for directory in sorted((ROOT / plugin_path / 'skills').iterdir()):
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
    return count


def validate():
    plugins = sorted(p for p in (ROOT / 'plugins').iterdir() if not p.name.startswith('.'))
    check(bool(plugins), 'At least one plugin is required')
    expected = {p.name: './plugins/' + p.name for p in plugins}
    count = 0
    for plugin in plugins:
        check(plugin.is_dir() and not plugin.is_symlink(), f'{plugin.name}: expected a local plugin directory')
        count += validate_plugin(plugin.relative_to(ROOT))
    for path in ['.claude-plugin/marketplace.json', '.cursor-plugin/marketplace.json', '.agents/plugins/marketplace.json']:
        market = load(path)
        check(market['name'] == 'decodedskills', f'{path}: inconsistent marketplace name')
        entries = market['plugins']
        check(len(entries) == len(expected), f'{path}: missing or duplicate plugins')
        check({entry['name'] for entry in entries} == set(expected), f'{path}: catalog does not match plugin directories')
        for entry in entries:
            source = entry['source']
            if path.startswith('.agents/'):
                check(source == {'source': 'local', 'path': expected[entry['name']]}, f'{path}: unexpected source')
                check(entry['policy'] == {'installation': 'AVAILABLE', 'authentication': 'ON_INSTALL'}, f'{path}: unexpected policy')
                check(bool(entry['category']), f'{path}: missing category')
            else:
                check(source == expected[entry['name']], f'{path}: unexpected source')
    print(f'Validated {len(plugins)} plugin(s), marketplaces, and {count} skill(s).')
    if not count:
        print('Scaffold only: no installable skills yet.')


if __name__ == '__main__':
    try:
        validate()
    except (ValueError, KeyError, OSError, TypeError) as error:
        print(f'Validation failed: {error}', file=sys.stderr)
        sys.exit(1)
