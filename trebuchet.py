from string import ascii_lowercase


def unfuck():
    result = 0
    file = open(r"inputs/day1.txt", "r").readlines()
    for line in file:
        line = "".join(c for c in line if c not in ascii_lowercase)
        first = line[0]
        last = line[-2]
        result += int(first+last)
    return result


if __name__ == "__main__":
    print(unfuck())