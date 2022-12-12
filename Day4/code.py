import sys
arguments = sys.argv[1:]

if (not arguments):
    print("No arguments provided")
    exit()


def test():
    file = 'test.txt'
    main(file)

def final():
    file = 'input.txt'
    main(file)


def main(file):
    data = []
    with open(file, 'r') as f:
        for line in f:
            x, y = line.split(',')
            y = y[:-1] if y[-1] == '\n' else y
            data.append([x, y])
    part1(data)
    part2(data)

def part1(data):
    count = 0
    for d in data:
        x, y = d[0], d[1]
        t = x.split('-')
        xa, xb = int(t[0]), int(t[1])
        t = y.split('-')
        ya, yb = int(t[0]), int(t[1])

        c = 0
        if (xa <= ya and xb >= yb):
            c += 1
        elif (ya <= xa and yb >= xb):
            c += 1

        # print(xa, xb, ya, yb, ": ", c)
        count += c
    print("Part 1: ", count)

def part2(data):
    count = 0
    for d in data:
        x, y = d[0], d[1]
        t = x.split('-')
        xa, xb = int(t[0]), int(t[1])
        t = y.split('-')
        ya, yb = int(t[0]), int(t[1])

        c = 0
        if (xa <= ya and xb >= yb):
            c += 1
        elif (ya <= xa and yb >= xb):
            c += 1
        elif ((ya >= xa and ya <= xb) or (xa >= ya and xa <= yb)):
            c += 1

        # print(xa, xb, ya, yb, ": ", c)
        count += c
    print("Part 2: ", count)



if arguments[0] == 'test':
    test()
elif arguments[0] == 'final':
    final()