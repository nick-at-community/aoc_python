from itertools import islice
import numpy as np

np.set_printoptions(linewidth=180)

def part_one(fpath: str):
    with open(fpath) as f:
        data = f.read()

    cycle = 0
    X = 1

    strengths = []
    for line in data.splitlines():
        try:
            command, val = line.split()
            for i in range(2):
                # print(cycle, X)
                cycle += 1
                strengths.append(cycle * X)
            else:
                X += int(val)

        except ValueError:
            # print(cycle, X)
            cycle += 1
            strengths.append(cycle * X)

    # print(cycle, X)
    return sum([
        strengths[19],
        strengths[59],
        strengths[99],
        strengths[139],
        strengths[179],
        strengths[219],
    ])


############

def make_crt(output = np.array):
    return output.reshape((6, 40))


def print_crt(crt: np.array):
    for line in crt:
        print(''.join(line))


class X:
    def __init__(self, val: int = 1):
        self.val = val

    def __add__(self, other):
        return type(self)(self.val + other)

    @property
    def sprite_trio(self):
        return (self.val - 1, self.val, self.val + 1)

    def print_pixel(self, loc: int):
        return loc % 40 in self.sprite_trio

def part_two(fpath: str):
    with open(fpath) as f:
        data = f.read()

    cycle = 0
    x = X()

    output = []
    for line in data.splitlines():
        # print(line)
        try:
            command, val = line.split()
            for i in range(2):
                # print(cycle, x.val)
                char = '#' if x.print_pixel(cycle) else '.'
                output.append(char)
                cycle += 1
            else:
                x += int(val)

        except ValueError:
            print(cycle, x.val)
            char = '#' if x.print_pixel(cycle) else '.'
            output.append(char)
            cycle += 1

        # print(x.sprite_trio)

    crt = make_crt(np.array(output))
    print_crt(crt)


def main(fpath: str):
    print(part_one(fpath))
    print(part_two(fpath))


if __name__ == '__main__':
    main('prompt.txt')
    main('input.txt')
