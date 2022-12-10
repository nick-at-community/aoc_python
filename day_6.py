import itertools

def sliding_window(iterable, n=2):
    iterables = itertools.tee(iterable, n)

    for iterable, num_skipped in zip(iterables, itertools.count()):
        for _ in range(num_skipped):
            next(iterable, None)

    return zip(*iterables)


def part_one():
    with open('input.txt') as f:
        data = f.read().strip()

        for idx, s in enumerate(sliding_window(data, 4)):
            if len(set(''.join(s))) == 4:
                return idx + 4

def part_two():
    with open('input.txt') as f:
        data = f.read().strip()

        for idx, s in enumerate(sliding_window(data, 14)):
            if len(set(''.join(s))) == 14:
                return idx + 14



def main():
    print(part_one())
    print(part_two())


if __name__ == '__main__':
    main()
