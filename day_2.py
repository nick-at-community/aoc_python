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

RESULTS = {
    'X': 'LOSE',
    'Y': 'DRAW',
    'Z': 'WIN'
}


class Shape:
    def __init__(self, letter: str = None, name: str = None):
        if letter:
            self.shape = LETTER_MATCH[letter]
        elif name:
            self.shape = name

        self.points = SHAPE_POINTS[self.shape]

    def beats(self):
        return {
            'ROCK': 'SCISSORS',
            'SCISSORS': 'PAPER',
            'PAPER': 'ROCK'
        }[self.shape]

    def loses_to(self):
        return {
            'SCISSORS': 'ROCK',
            'PAPER': 'SCISSORS',
            'ROCK': 'PAPER'
        }[self.shape]


class Match:
    def __init__(self, us: Shape, them: Shape):
        self.us = us
        self.them = them

    def resolve(self):
        if self.us.shape == self.them.shape:
            return 3
        elif self.them.shape == self.us.beats():
            return 6
        else:
            return 0

    def score(self):
        return self.resolve() + self.us.points


def fix_the_match(opp_shape: Shape, result_key: str) -> Shape:
    result = RESULTS[result_key]
    if result == 'WIN':
        return Shape(name=opp_shape.loses_to())
    elif result == 'LOSE':
        return Shape(name=opp_shape.beats())
    else:
        return Shape(name=opp_shape.shape)


def main(fpath: str):
    scores = []

    with open(fpath) as f:
        for line in f:
            them, result_key = line.strip().split()

            them = Shape(letter=them)

            us = fix_the_match(them, result_key)

            scores.append(Match(us, them).score())

    return sum(scores)

if __name__ == '__main__':
    print(main('input.txt'))
