import os
from typing import Dict, Set, Tuple

def build_files_and_dirs() -> Tuple[Dict[str, int], Set]:
    with open('input.txt') as f:
        data = f.read()

    files = {}
    dirs = set(['/'])

    pwd = '/'
    in_ls = False
    # shout out to https://www.twitch.tv/codewithanthony
    for line in data.splitlines()[1:]:
        if in_ls and line.startswith('$'):
            in_ls = False
        elif in_ls and line.startswith('dir '):
            _, dirname = line.split(' ', 1)
            dirs.add(os.path.join(pwd, dirname))
            continue
        elif in_ls:
            sz, filename = line.split(' ', 1)
            files[os.path.join(pwd, filename)] = int(sz)
            continue

        if line == '$ ls':
            in_ls = True
        elif line == '$ cd ..':
            pwd = os.path.dirname(pwd) or '/'
        elif line.startswith('$ cd'):
            pwd = os.path.join(pwd, line.split(' ', 2)[-1])
        else:
            raise AssertionError(line)

    return files, dirs

def calc_dirsize(dirname: str):
    size = 0
    for k, v in files.items():
        if k.startswith(dirname):
            size += files[k]

    return size

def part_one():
    global files, dirs
    files, dirs = build_files_and_dirs()

    sizes = [
        calc_dirsize(dirname)
        for dirname
        in dirs
    ]

    return sum(
        size
        for size
        in sizes
        if size <= 100000
    )

def part_two():
    global files, dirs
    MAX = 70000000
    NEED = 30000000

    files, dirs = build_files_and_dirs()

    sizes = [
        calc_dirsize(dirname)
        for dirname
        in dirs
    ]

    TOTAL = calc_dirsize('/')
    TARGET = (TOTAL + NEED) - MAX

    return sorted(
        size
        for size
        in sizes
        if size >= TARGET
    )[0]


def main():
    print(part_one(), '\n')
    print(part_two())


if __name__ == '__main__':
    main()
