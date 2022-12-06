LETTER_MATCH = {
    'A': 'ROCK',
    'B': 'PAPER',
    'C': 'SCISSORS',
    'X': 'ROCK',
    'Y': 'PAPER',
    'Z': 'SCISSORS'
}

SHAPE_POINTS = {
    'ROCK': 1,
    'PAPER': 2,
    'SCISSORS': 3
}


class Shape:
    def __init__(self, letter: str):
        self.shape = LETTER_MATCH[letter]
        self.points = SHAPE_POINTS[self.shape]

    def resolve(self, other):
        if self.shape == other.shape:
            return 3
        elif self.shape == 'ROCK':
            return 6 if other.shape == 'SCISSORS' else 0
        elif self.shape == 'PAPER':
            return 6 if other.shape == 'ROCK' else 0
        else:
            return 6 if other.shape == 'PAPER' else 0

    def score(self, other):
        return self.resolve(other) + self.points



def main(fpath: str):
    scores = []

    with open(fpath) as f:
        for line in f:
            them, us = line.strip().split()

            them = Shape(them)
            us = Shape(us)

            scores.append(us.score(them))

    return sum(scores)

if __name__ == '__main__':
    print(main('input.txt'))
