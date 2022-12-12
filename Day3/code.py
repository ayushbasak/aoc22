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
            data.append(line[:-1])
            # x, y = line[0:len(line)//2], line[len(line)//2:-1]
            # data.append([x, y])

    # part1(data)
    part2(data)

def part1(data):
    temp = data
    data = []
    for line in temp:
        x, y = line[0:len(line)//2], line[len(line)//2:]
        data.append([x, y])
    priorities = 0
    for d in data:
        x, y = d[0], d[1]

        for char in x:
            if (char in y):
                if (char.islower()):
                    priorities += ord(char) - ord('a') + 1
                else:
                    priorities += ord(char) - ord('A') + 27
                break
    print(priorities)

def part2(data):
    temp = data
    # gauranteed length of data % 3 == 0
    data = []
    for i in range(0, len(temp), 3):
        data.append([temp[i], temp[i + 1], temp[i + 2]])
    priorities = 0
    for d in data:
        x, y, z = d[0], d[1], d[2]
        _set = set()

        for char in x:
            _set.add(char)
        for char in y:
            _set.add(char)
        for char in z:
            _set.add(char)

        for char in _set:
            if (char in x and char in y and char in z):
                if (char.islower()):
                    priorities += ord(char) - ord('a') + 1
                else:
                    priorities += ord(char) - ord('A') + 27
                break
    print(priorities)



if arguments[0] == 'test':
    test()
elif arguments[0] == 'final':
    final()