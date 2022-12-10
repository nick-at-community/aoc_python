from collections import deque
import re


def parse_setup(setup: str):
    stacks = {
        1: deque(),
        2: deque(),
        3: deque()
    }

    for line in setup.split('\n')[:-1]:
        if left := re.search('[A-Z]', line[:4]):
            stacks[1].append(left.group())

        if center := re.search('[A-Z]', line[4:8]):
            stacks[2].append(center.group())

        if right := re.search('[A-Z]', line[8:]):
            stacks[3].append(right.group())

    return stacks

def parse_instructions(instruction_text: str):
    return [
        [
            int(x)
            for x
            in re.findall('\d+', line)
        ]
        for line
        in instruction_text.split('\n')[:-1]
    ]

def apply_instructions(stacks, instructions):
    for step in instructions:
        boxes, from_, to_ = step

        for box in range(boxes):
            temp = stacks[from_].popleft()
            stacks[to_].appendleft(temp)

    return stacks


def part_one():
    with open('input.txt') as f:
        data = f.read()

        setup, instruction_text = data.split('\n\n')

        stacks = parse_setup(setup)
        instructions = parse_instructions(instruction_text)

        return apply_instructions(stacks, instructions)

def part_two():
    with open('input.txt') as f:
        data = f.read()



def main():
    print(part_one())
    print(part_two())


if __name__ == '__main__':
    main()
