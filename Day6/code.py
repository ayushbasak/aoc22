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
            data.append(line)
        data = data[0]
    part1(data)
    part2(data)

def part1(data):
    index = 0
    mp = {}
    for i in range(4):
        if data[i] in mp:
            mp[data[i]] += 1
        else:
            mp[data[i]] = 1

    while (len(mp) < 4):
        # print(mp)

        if data[index + 4] in mp:
            mp[data[index + 4]] += 1
        else:
            mp[data[index + 4]] = 1
        
        mp[data[index]] = mp[data[index]] - 1
        if (mp[data[index]] == 0):
            del mp[data[index]]
        index += 1
    # print(data, mp, index + 4)
    print(index + 4)
    pass
def part2(data):
    index = 0
    mp = {}
    for i in range(14):
        if data[i] in mp:
            mp[data[i]] += 1
        else:
            mp[data[i]] = 1

    while (len(mp) < 14):
        # print(mp)

        if data[index + 14] in mp:
            mp[data[index + 14]] += 1
        else:
            mp[data[index + 14]] = 1
        
        mp[data[index]] = mp[data[index]] - 1
        if (mp[data[index]] == 0):
            del mp[data[index]]
        index += 1
    # print(data, mp, index + 4)
    print(index + 14)



if arguments[0] == 'test':
    test()
elif arguments[0] == 'final':
    final()