import numpy as np



def build_topomap(data: str):
    topomap = []

    for line in data.splitlines():
        topomap.append([int(x) for x in line])

    topomap = np.array(topomap)

    return topomap

def is_visible(x: int, y: int):
    val = topomap[x, y]

    up = topomap[:x, y]
    up_vis = all(up < val)

    left = topomap[x, :y]
    left_vis = all(left < val)

    right = topomap[x, y+1:]
    right_vis = all(right < val)

    down = topomap[x+1:, y]
    down_vis = all(down < val)

    return any([
        up_vis,
        left_vis,
        right_vis,
        down_vis
    ])

def part_one(fpath: str):
    global topomap

    with open(fpath) as f:
        topomap = build_topomap(f.read())

    x_lim, y_lim = topomap.shape

    total = x_lim * 2 + (y_lim * 2 - 4)

    for x in range(1, x_lim - 1):
        for y in range(1, y_lim - 1):
            if is_visible(x, y):
                total += 1

    return total

##########

def score_line_of_sight(val, los):
    view_score = 0
    for tree in los:
        view_score += 1
        if tree < val:
            continue
        else:
            break
    return view_score


def calc_view_score(x, y):
    val = topomap[x, y]
    print(val)

    view_scores = []

    up = topomap[:x, y][::-1]
    # print(up)
    up_score = score_line_of_sight(val, up)
    # print(up_score)

    left = topomap[x, :y][::-1]
    # print(left)
    left_score = score_line_of_sight(val, left)
    # print(left_score)

    right = topomap[x, y+1:]
    # print(right)
    right_score = score_line_of_sight(val, right)
    # print(right_score)

    down = topomap[x+1:, y]
    # print(down)
    down_score = score_line_of_sight(val, down)
    # print(down_score)

    return up_score * left_score * right_score * down_score

def part_two(fpath: str):
    global topomap

    with open(fpath) as f:
        topomap = build_topomap(f.read())

    x_lim, y_lim = topomap.shape

    max_ = 0
    for x in range(1, x_lim -1):
        for y in range(1, y_lim -1):
            val = calc_view_score(x, y)
            if val > max_:
                max_ = val

    return max_



def main(fpath: str):
    print(part_one(fpath))
    print(part_two(fpath))


if __name__ == '__main__':
    main('prompt.txt')
    main('input.txt')
