"""Generate the solution index, or check syntax and index freshness with --check."""

import argparse
import ast
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- solutions:start -->'
END = '<!-- solutions:end -->'


def index(root):
    folders = sorted((path for path in root.iterdir() if path.is_dir()
                      and path.name.isascii() and path.name.isdigit()), key=lambda path: int(path.name))
    if not folders:
        raise ValueError('No numbered solution folders found')
    rows = []
    python_count = cpp_count = 0
    for folder in folders:
        sources = [source for source in (folder / 'solution.py', folder / 'solution.cpp') if source.is_file()]
        if not sources:
            raise ValueError(f'No solution source found in {folder.name}')
        for source in sources:
            if source.suffix == '.py':
                tree = ast.parse(source.read_text(encoding='utf-8-sig'), filename=str(source.relative_to(root)))
                # Compile but never execute: judge-supplied types need not exist locally.
                compile(tree, str(source.relative_to(root)), 'exec')
                classes = [node for node in tree.body if isinstance(node, ast.ClassDef)]
                primary = [node for node in classes if node.name == 'Solution'] or classes
                names = [f'{node.name}.{method.name}' for node in primary for method in node.body
                         if isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)) and not method.name.startswith('_')]
                if not names:
                    names = [node.name for node in tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]
                methods = ', '.join(f'`{name}`' for name in names) or '—'
                language = 'Python'
                python_count += 1
            else:
                methods, language = 'See source', 'C++'
                cpp_count += 1
            rows.append(f'| [{folder.name}]({folder.name}/{source.name}) | {language} | {methods} |')
    return (f'{len(rows)} solutions ({python_count} Python, {cpp_count} C++).\n\n'
            '| Export folder | Language | Methods |\n| --- | --- | --- |\n'
            + '\n'.join(rows)), len(rows), python_count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='validate without writing files')
    args = parser.parse_args()
    try:
        table, count, python_count = index(ROOT)
        readme = ROOT / 'README.md'
        text = readme.read_text(encoding='utf-8')
        if text.count(START) != 1 or text.count(END) != 1 or text.index(START) > text.index(END):
            raise ValueError('README must contain one ordered solution-index marker pair')
        before, rest = text.split(START, 1)
        _, after = rest.split(END, 1)
        expected = before + START + '\n\n' + table + '\n\n' + END + after
        if args.check and expected != text:
            print('Solution index is outdated. Run: python tools/update_index.py', file=sys.stderr)
            return 1
        if not args.check:
            readme.write_text(expected, encoding='utf-8')
        print(f'{python_count} Python files passed syntax checks; {count}-solution index {"is current" if args.check else "updated"}.')
        return 0
    except (OSError, SyntaxError, ValueError) as error:
        print(f'Check failed: {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
