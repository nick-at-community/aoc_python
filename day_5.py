from collections import deque
import re


def parse_setup(setup: str):
    stacks = dict()

    for line in setup.split('\n'):
        crates_in_this_line = len(line) // 4 + 1

        for idx, stack in enumerate(range(1, crates_in_this_line + 1)):
            content = line[idx * 4 : ((idx + 1) * 4)]

            if match := re.search('[A-Z]', content):
                stacks[stack] = stacks.get(stack, deque())
                stacks[stack].append(match.group())

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

        result = apply_instructions(stacks, instructions)

        return ''.join([
            result[key].popleft()
            for key
            in sorted(result.keys())
        ])

def part_two():
    with open('input.txt') as f:
        data = f.read()



def main():
    print(part_one())
    print(part_two())


if __name__ == '__main__':
    main()
