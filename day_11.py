from collections import deque
from itertools import islice
import math
import re
from typing import Tuple

import numpy as np

np.set_printoptions(linewidth=180)

MONKEYS = dict()

class Item:
    def __init__(self, worry: int):
        self.worry = worry

class Inspect:
    def __init__(self, operation: str, inspect_divide: int, floor_or_mod: str):
        self.operation = operation
        self.inspect_divide = inspect_divide
        self.floor_or_mod = floor_or_mod

    def run(self, item: Item):
        global new, old
        new = 0
        old = item.worry
        exec(self.operation, globals())
        if self.floor_or_mod == 'floor':
            return Item(worry=new // self.inspect_divide)
        elif self.floor_or_mod == 'mod':
            return Item(worry=new % self.inspect_divide)
        else:
            raise AssertionError('floor_or_mod not defined')

class Test:
    def __init__(self, divisor: int, t_monkey: int, f_monkey: int):
        self.divisor = divisor
        self.t_monkey = t_monkey
        self.f_monkey = f_monkey

    def run(self, item: Item):
        if not item.worry % self.divisor:
            return self.t_monkey
        else:
            return self.f_monkey

class Monkey:
    def __init__(self, test: Test, inspect: Inspect):
        self.haul = deque()
        self.test = test
        self.inspect = inspect
        self.checks = 0

    def inspect_haul(self):
        for _ in range(len(self.haul)):
            item = self.inspect.run(self.haul.popleft())
            self.haul.appendleft(item)
            self.run_test()
            self.checks += 1

    def run_test(self):
        item = self.haul.popleft()
        target_monkey = self.test.run(item)
        self.give(item, target_monkey)

    def take(self, item: Item):
        self.haul.append(item)

    def give(self, item: Item, target_monkey: int):
        MONKEYS[target_monkey].take(item)


def monkey_factory(input_text: str, floor_or_mod: str, inspect_divide: int = 3) -> Tuple[int, Monkey]:
    monkey_idx = re.findall('Monkey (\d+)', input_text)[0]

    starting_item_worries = [
        int(x)
        for x in
        re.findall('Starting items: ([\d,\s]+)', input_text)[0].split(', ')
    ]
    starting_items = [
        Item(worry)
        for worry
        in starting_item_worries
    ]
    # print(starting_items)

    divisor = int(re.findall('Test: divisible by (\d+)', input_text)[0])
    t_monkey = int(re.findall('true: throw to monkey (\d+)', input_text)[0])
    f_monkey = int(re.findall('false: throw to monkey (\d+)', input_text)[0])

    test = Test(divisor, t_monkey, f_monkey)

    operation = re.findall('(new = old .*)', input_text)[0]
    inspect = Inspect(
        operation,
        floor_or_mod=floor_or_mod,
        inspect_divide=inspect_divide
    )

    monkey = Monkey(test, inspect)

    for item in starting_items:
        monkey.take(item)

    return monkey_idx, monkey


def part_one(fpath: str):
    with open(fpath) as f:
        data = f.read()

    for input_text in data.split('\n\n'):
        idx, monkey = monkey_factory(input_text, floor_or_mod='floor', inspect_divide=3)
        MONKEYS[int(idx)] = monkey

    # sim simians
    for round_ in range(20):
        for idx in range(len(MONKEYS)):
            MONKEYS[idx].inspect_haul()

        # for idx in range(len(MONKEYS)):
        #     print([x.worry for x in MONKEYS[idx].haul])

    first, second = sorted([monkey.checks for monkey in MONKEYS.values()])[::-1][:2]
    return first * second

def part_two(fpath: str):
    with open(fpath) as f:
        data = f.read()

    for input_text in data.split('\n\n'):
        idx, monkey = monkey_factory(input_text, floor_or_mod='mod', inspect_divide=1)
        MONKEYS[int(idx)] = monkey

    # "find another way to keep your worry levels manageable."
    lcm = math.lcm(*[monkey.test.divisor for monkey in MONKEYS.values()])
    for monkey_idx in range(len(MONKEYS)):
        MONKEYS[monkey_idx].inspect.inspect_divide = lcm

    # sim simians
    for round_ in range(10000):
        for idx in range(len(MONKEYS)):
            MONKEYS[idx].inspect_haul()

        # for idx in range(len(MONKEYS)):
        #     print([x.worry for x in MONKEYS[idx].haul])

    first, second = sorted([monkey.checks for monkey in MONKEYS.values()])[::-1][:2]
    return first * second


def main(fpath: str):
    print(part_one(fpath))
    print(part_two(fpath))


if __name__ == '__main__':
    main('prompt.txt')
    main('input.txt')
