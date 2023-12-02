from string import digits
from re import split


def check(file):
    total = 0
    for line in file:
        colours = {"red": 0,
                   "green": 0,
                   "blue": 0
                   }
        id = ""
        for i in range(3):
            if line[5+i] in digits:
                id += line[5+i]
        line = split(":\s|;\s|,\s", line[7+len(id):-1].strip())
        for segment in line:
            s = segment.split(" ")
            amount = int(s[0])
            colour = s[1]
            if amount > colours[colour]:
                colours[colour] = amount
        total += colours["red"] * colours["green"] * colours["blue"]
    return total


if __name__ == "__main__":
    file = open(r"inputs/day2.txt", "r")
    print(check(file))
