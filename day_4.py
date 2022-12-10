

def part_one():
    with open('input.txt') as f:
        data = f.read().split()

        count = 0

        for pair in data:
            a, b = pair.split(',')
            a0, a1 = map(int, a.split('-'))
            b0, b1 = map(int, b.split('-'))

            if (
                a1 <= b1 and a0 >= b0
            ) or (
                b1 <= a1 and b0 >= a0
            ):
                count += 1

    return count


def part_two():
    with open('input.txt') as f:
        data = f.read().split()

        count = 0

        for pair in data:
            a, b = pair.split(',')
            a0, a1 = map(int, a.split('-'))
            b0, b1 = map(int, b.split('-'))

            if (
                a0 <= b1
            ) and (
                b0 <= a1
            ):
                count += 1

    return count

def main():
    print(part_one())
    print(part_two())


if __name__ == '__main__':
    main()
