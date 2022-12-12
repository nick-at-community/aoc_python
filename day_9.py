import numpy as np

from math import sqrt


np.set_printoptions(linewidth=160)

def dist(head, tail):
    head_x, head_y = head
    tail_x, tail_y = tail

    return sqrt((tail_x - head_x) ** 2 + (tail_y - head_y) ** 2)


def move_head(dir):
    global snake

    if dir == 'R':
        snake[0] = [snake[0][0] + 1, snake[0][1]]
    elif dir == 'L':
        snake[0] = [snake[0][0] - 1, snake[0][1]]
    elif dir == 'U':
        snake[0] = [snake[0][0], snake[0][1] + 1]
    else:
        snake[0] = [snake[0][0], snake[0][1] - 1]

def move_segment(segment_idx: int, tail_idx: int):
    global snake, last_segment_pos, tail_visited

    d = dist(snake[segment_idx - 1], snake[segment_idx])

    ax, ay = snake[segment_idx - 1]
    bx, by = snake[segment_idx]

    if d <= 1:
        pass
    elif d == sqrt(2): # diag is still legal
        pass
    elif d == 2: # straight line follow
        tmp = snake[segment_idx]
        snake[segment_idx] = last_segment_pos
        last_segment_pos = tmp
    else: # catch up diag move
        snake[segment_idx] = (
            (ax + bx) // 2,
            (ay + by) // 2
        )

    tail_visited.add(tuple(snake[tail_idx]))

def debug_state():
    global snake
    debug = np.full((30, 30), '.')
    origin_x = 15
    origin_y = 15

    for segment in snake:
        debug[
            origin_x + snake[segment][0],
            origin_y + snake[segment][1]
        ] = segment

    print(debug)
    print()


def part_one(fpath: str):
    global snake, last_segment_pos, tail_visited

    with open(fpath) as f:
        data = f.read()

    tail_idx = 1
    tail_visited = set()
    snake = {x: [0, 0] for x in range(2)}

    for step in data.splitlines():
        dir, amt = step.split()
        print(dir, amt)

        amt = int(amt)
        for tick in range(amt):
            last_segment_pos = snake[0]
            move_head(dir)
            for segment_idx in range(1, len(snake)):
                move_segment(segment_idx, tail_idx)
            print(snake[0], snake[1])

    return len(tail_visited)

def part_two(fpath: str):
    global snake, last_segment_pos, tail_visited

    with open(fpath) as f:
        data = f.read()

    tail_idx = 9
    tail_visited = set()
    snake = {x: [0, 0] for x in range(10)}

    for i, step in enumerate(data.splitlines()):
        dir, amt = step.split()
        print(dir, amt)

        amt = int(amt)
        for tick in range(amt):
            last_segment_pos = snake[0]
            move_head(dir)
            # debug_state()
            for segment_idx in range(1, len(snake)):
                move_segment(segment_idx, tail_idx)
                # debug_state()

    return len(tail_visited)


def main(fpath: str):
    # print(part_one(fpath))
    print(part_two(fpath))


if __name__ == '__main__':
    main('prompt.txt')
    # main('input.txt')
