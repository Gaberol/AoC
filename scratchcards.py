from re import split


def count(file):
    total = 0
    for line in file:
        line = line[10:-1].split(" | ")
        winning = list(filter(None, split("\s+", line[0])))
        numbers = list(filter(None, split("\s+", line[1])))
        power = -1
        for num in numbers:
            if num in winning:
                power += 1
        if power < 0: continue
        total += 2**(power)
    return total


if __name__ == "__main__":
    file = open(r"inputs/day4.txt","r").readlines()
    print(count(file))
