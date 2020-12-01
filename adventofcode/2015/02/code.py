def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [str(line[:-1]) for line in f.readlines()]

def part1(l, w, h):
    wrap = 0
    lw = l * w
    lh = l * h
    wh = w * h

    extra = min(lw, lh, wh)
    wrap = 2*lw + 2*lh + 2*wh + extra
        
    return wrap
def part2(l,w,h):
    lw = 2*l + 2*w
    lh = 2*l + 2 * h
    wh = 2*w + 2 * h
    bow = l*w*h
    return bow+min(lw,lh,wh)

if __name__ == '__main__':
    paper = 0
    ribbon_length = 0
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as fh:
        for line in fh.readlines():
            l, w, h = map(int, line.split('x'))
            
            paper += part1(l, w, h)
            ribbon_length += part2(l, w, h)


    print(f'Part 1 = {paper}')
    print(f'Part 1 = {ribbon_length}')