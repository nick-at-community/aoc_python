from itertools import islice
from typing import Tuple


def split_bundle(rucksack: str) -> Tuple[str, str]:
    mid = int(len(rucksack) / 2)
    return rucksack[:mid], rucksack[mid:]

def find_overlap(vals):
    running_set = set(vals[0])
    for val in vals[1:]:
        running_set = running_set.intersection(set(val))

    return running_set.pop()

def assign_priority(character: str) -> int:
    if character.isupper():
        return ord(character) - 64 + 26
    else:
        return ord(character) - 96


def part_one(fpath: str):
    results = []
    with open(fpath) as f:
        for line in f.readlines():
            left, right = split_bundle(line.strip())
            overlap = find_overlap([left, right])

            results.append(assign_priority(overlap))

    return sum(results)


###########

def load_in_threes(io_obj):
    yield from islice(io_obj, 3)

def part_two(fpath: str):
    gen = (line.strip() for line in open(fpath))

    results = []
    while gen:
        try:
            a, b, c = load_in_threes(gen)
            overlap = find_overlap([a, b, c])
            results.append(assign_priority(overlap))
        except:
            break

    return sum(results)



def main(fpath):
    print(part_one(fpath))
    print(part_two(fpath))

if __name__ == '__main__':
    main('input.txt')
