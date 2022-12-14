class Sack:
    def __init__(self, contents):
        self.contents = contents

    @property
    def sum(self):
        return sum(self.contents)

    def __le__(self, other):
        return self.sum <= other.sum

    def __gt__(self, other):
        return self.sum > other.sum

    def __repr__(self):
        return str(self.sum)


def read_inventory_file(fpath: str):
    sacks = []

    with open(fpath) as f:
        data = f.readlines()

    contents = []
    for line in data:
        if line != '\n':
            contents.append(int(line.strip()))
        else:
            sacks.append(Sack(contents))
            contents = []

    else:
        sacks.append(Sack(contents))

    return sacks


if __name__ == '__main__':
    results = read_inventory_file('input.txt')

    print(max(results))

    print(sum([x.sum for x in sorted(results)[-3:]]))
    print([x.sum for x in sorted(results)[-3:]])
