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

def part_two(fpath: str):
    with open(fpath) as f:
        data = f.read()



def main(fpath: str):
    print(part_one(fpath))
    print(part_two(fpath))


if __name__ == '__main__':
    main('prompt.txt')
    main('input.txt')
