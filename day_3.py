from typing import Tuple



def split_bundle(rucksack: str) -> Tuple[str, str]:
    mid = int(len(rucksack) / 2)
    return rucksack[:mid], rucksack[mid:]

def find_overlap(left: str, right: str):
    left = set(left)
    right = set(right)

    return left.intersection(right).pop()

def assign_priority(character: str) -> int:
    if character.isupper():
        return ord(character) - 64 + 26
    else:
        return ord(character) - 96


def main(fpath: str):
    results = []
    with open(fpath) as f:
        for line in f.readlines():
            left, right = split_bundle(line.strip())
            overlap = find_overlap(left, right)

            results.append(assign_priority(overlap))

    return sum(results)

if __name__ == '__main__':
    print(main('input.txt'))
