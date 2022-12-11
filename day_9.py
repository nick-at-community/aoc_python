from math import sqrt


def dist(head, tail):
    head_x, head_y = head
    tail_x, tail_y = tail

    return sqrt((tail_x - head_x) ** 2 + (tail_y - head_y) ** 2)


def move_head(dir):
    global head_pos

    if dir == 'R':
        head_pos = [head_pos[0] + 1, head_pos[1]]
    elif dir == 'L':
        head_pos = [head_pos[0] - 1, head_pos[1]]
    elif dir == 'U':
        head_pos = [head_pos[0], head_pos[1] + 1]
    else:
        head_pos = [head_pos[0], head_pos[1] - 1]

def move_tail():
    global head_pos, tail_pos, last_head_pos, tail_visited

    d = dist(head_pos, tail_pos)
    if d <= 1:
        pass
    elif d == sqrt(2): # diag is still legal
        pass
    elif d == 2: # straight line follow
        tail_pos = last_head_pos
    else: # catch up diag move
        tail_pos = last_head_pos

    tail_visited.add(tuple(tail_pos))


def part_one(fpath: str):
    global head_pos, last_head_pos, tail_pos, tail_visited

    with open(fpath) as f:
        data = f.read()

    tail_visited = set()
    head_pos = [0, 0]
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

def part_two(fpath: str):
    with open(fpath) as f:
        data = f.read()



def main(fpath: str):
    print(part_one(fpath))
    print(part_two(fpath))


if __name__ == '__main__':
    main('prompt.txt')
    main('input.txt')
