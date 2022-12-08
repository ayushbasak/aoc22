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
            a, b = line.split(' ')
            if b[-1] == '\n':
                b = b[:-1]
            data.append([a, b])

    # part1(data)
    part2(data)


mappings = {
    'A': 1, 'X': 1,
    'B': 2, 'Y': 2,
    'C': 3, 'Z': 3
}

losing = { 1: 3, 2: 1, 3: 2 }
winning = { 1: 2, 2: 3, 3: 1 }

def part1(data):
    score1, score2 = 0,0
    for d in data:
        a, b = d
        a, b = mappings[a], mappings[b]
        score1 += a
        score2 += b

        if ( a == 1 and b == 3 or a == 2 and b == 1 or a == 3 and b == 2 ):
            score1 += 6
        elif ( a == 1 and b == 2 or a == 2 and b == 3 or a == 3 and b == 1 ):
            score2 += 6
        elif a == b:
            score1 += 3
            score2 += 3
    print(score1, score2)


def part2(data):
    score1, score2 = 0,0
    for d in data:
        A,B = d
        a, b = d
        a, b = mappings[a], mappings[b]
        if (B == 'X'):
            score1 += a
            score2 += losing[a]
            score1 += 6
        elif (B == 'Y'):
            score1 += a + 3
            score2 += a + 3
        elif (B == 'Z'):
            score1 += a
            score2 += winning[a]
            score2 += 6

    print(score1, score2)



if arguments[0] == 'test':
    test()
elif arguments[0] == 'final':
    final()