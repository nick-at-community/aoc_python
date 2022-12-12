from itertools import islice



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




def part_two(fpath: str):
    with open(fpath) as f:
        data = f.read()



def main(fpath: str):
    print(part_one(fpath))
    print(part_two(fpath))


if __name__ == '__main__':
    main('prompt.txt')
    main('input.txt')
