from math import sqrt


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

def move_tail(tail_idx: int):
    global snake, last_head_pos, tail_visited

    d = dist(snake[0], snake[tail_idx])
    if d <= 1:
        pass
    elif d == sqrt(2): # diag is still legal
        pass
    elif d == 2: # straight line follow
        snake[tail_idx] = last_head_pos
    else: # catch up diag move
        snake[tail_idx] = last_head_pos

    tail_visited.add(tuple(snake[tail_idx]))


def part_one(fpath: str):
    global snake, last_head_pos, tail_visited

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
            last_head_pos = snake[0]
            move_head(dir)
            move_tail(tail_idx)
            print(snake[0], snake[1])

    return len(tail_visited)

def part_two(fpath: str):
    global head_pos, last_head_pos, tail_pos, tail_visited

    with open(fpath) as f:
        data = f.read()

    tail_visited = set()

    tail_pos = [0, 0]

    for step in data.splitlines():
        dir, amt = step.split()
        print(dir, amt)

        amt = int(amt)
        for tick in range(amt):
            last_head_pos = head_pos
            move_head(dir)
            move_tail()
            print(head_pos, tail_pos)

    return len(tail_visited)



def main(fpath: str):
    print(part_one(fpath))
    # print(part_two(fpath))


if __name__ == '__main__':
    main('prompt.txt')
    # main('input.txt')
