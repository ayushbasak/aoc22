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
        temp = []
        for line in f:
            line = line.split('\n')[0]
            if (len(line) == 0):
                data.append(temp)
                temp = []
            else:
                temp.append(int(line))
        data.append(temp)

    part1(data)
    part2(data)

def part1(data):
    max_calories = 0
    for d in data:
        calories = 0
        for value in d:
            calories += value
        max_calories = max(max_calories, calories)

    print(max_calories)


def part2(data):
    summed_calories = []
    for d in data:
        summed_calories.append(sum(d))
    summed_calories.sort(reverse=True)
    print(sum(summed_calories[:3]))


if arguments[0] == 'test':
    test()
elif arguments[0] == 'final':
    final()