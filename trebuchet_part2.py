def unfuck(file):
    result = 0
    digits = {"one": "1",
              "two": "2",
              "three": "3",
              "four": "4",
              "five": "5",
              "six": "6",
              "seven": "7",
              "eight": "8",
              "nine": "9",
              "1": "1",
              "2": "2",
              "3": "3",
              "4": "4",
              "5": "5",
              "6": "6",
              "7": "7",
              "8": "8",
              "9": "9",
              }
    for line in file:
        index_first = 1000
        index_last = 0
        first = ""
        last = ""
        for digit in digits.keys():
            index = line.find(digit)
            if 0 <= index < index_first:
                index_first = index
                first = digits[digit]
            index = line.rfind(digit)
            if index >= index_last:
                index_last = index
                last = digits[digit]
        result += int(first+last)
        print(line+"first: ["+first+"] last: ["+last+"] value: ["+first+last+"] "+"cumulative: "+str(result))
    return result


if __name__ == "__main__":
    file = open(r"inputs/day1.txt", "r").readlines()
    #file = ["6twotwo18eightthreeeight\n","oneight\n", "sevenine\n", "eightwo\n"]
    print(unfuck(file))
