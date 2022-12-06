


LETTER_MATCH = {
    'A': 'X', # rock
    'B': 'Y', # paper
    'C': 'Z'  # scissors
}

SHAPE_POINTS = {
    'X': 1, # rock
    'Y': 2, # paper
    'Z': 3  # scissors
}

class Shape:
    def __init__(self, letter: str):
        self.letter = LETTER_MATCH.get(letter, letter)
        self.points = SHAPE_POINTS[self.letter]

    def throw(self, other):
        if self.letter == other.letter:
            return 3
        elif self.letter == 'X':
            return 6 if other.letter == 'Z' else 0
        elif self.letter == 'Y':
            return 6 if other.letter == 'X' else 0
        else:
            return 6 if other.letter == 'Y' else 0

    def score(self, other):
        return self.throw(other) + self.points


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
