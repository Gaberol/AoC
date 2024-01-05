from string import digits

symbols = ['%', '&', '$', '=', '*', '@', '-', '+', '#', '/']

def count(file):
    output = 0
    w = len(file[0])
    for i in range(len(file)):
        for j in range(w):
            char = file[i][j]
            if char in digits:
                char_l = 1
                if j+1<w and file[i][j+1] in digits:
                    char_l += 1
                    if j+2<w and file[i][j+2] in digits:
                        char_l += 1
                part_num = ""
                adjacent = False
                for k in range(char_l):
                    part_num += file[i][j+k]
                    file[i] = ".".join([file[i][:j+k],file[i][j+k+1:]])
                    if check(file,i,j+k):
                        adjacent = True
                if adjacent:
                    output += int(part_num)
    return output

def check(file,i,j):
    if j > 0:
        if file[i][j-1] in symbols:
            return True
    if j < len(file[0])-1:
        if file[i][j+1] in symbols:
            return True
    if i > 0:
        if file[i-1][j] in symbols:
            return True
        if j > 0:
            if file[i-1][j-1] in symbols:
                return True
        if j < len(file[0])-1:
            if file[i-1][j+1] in symbols:
                return True
    if i < len(file)-1:
        if file[i+1][j] in symbols:
            return True
        if j > 0:
            if file[i+1][j-1] in symbols:
                return True
        if j < len(file[0])-1:
            if file[i+1][j+1] in symbols:
                return True


if __name__ == "__main__":
    file = open(r"inputs/day3.txt", "r").readlines()
    file = [line for line in file]
    print(count(file))
