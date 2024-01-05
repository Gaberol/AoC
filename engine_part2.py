from string import digits


def count(file):
    w = len(file[0])
    output = 0
    for i in range(len(file)):
        for j in range(w):
            if file[i][j] != "*": continue
            coords = check(file,i,j)
            if len(coords) != 2: continue
            nums = ["",""]
            for k in range(2):
                if coords[k][1] > 0 and file[coords[k][0]][coords[k][1]-1] in digits:
                    if coords[k][1]-1 > 0 and file[coords[k][0]][coords[k][1]-2] in digits:
                        nums[k] += file[coords[k][0]][coords[k][1]-2]
                    nums[k] += file[coords[k][0]][coords[k][1]-1]
                nums[k] += file[coords[k][0]][coords[k][1]]
                if coords[k][1] < w-1 and file[coords[k][0]][coords[k][1]+1] in digits:
                    nums[k] += file[coords[k][0]][coords[k][1]+1]
                    if coords[k][1] < w-2 and file[coords[k][0]][coords[k][1]+2] in digits:
                        nums[k] += file[coords[k][0]][coords[k][1]+2]
            output += int(nums[0]) * int(nums[1])
    return output

def check(file,i,j):
    coords = []
    if j > 0:
        if file[i][j-1] in digits:
            coords.append((i,j-1))
    if j < len(file[0])-1:
        if file[i][j+1] in digits:
            coords.append((i,j+1))
    if i > 0:
        if file[i-1][j] in digits:
            coords.append((i-1,j))
        else:
            if j > 0:
                if file[i-1][j-1] in digits:
                    coords.append((i-1,j-1))
            if j < len(file[0])-1:
                if file[i-1][j+1] in digits:
                    coords.append((i-1,j+1))
    if i < len(file)-1:
        if file[i+1][j] in digits:
            coords.append((i+1,j))
        else:
            if j > 0:
                if file[i+1][j-1] in digits:
                    coords.append((i+1,j-1))
            if j < len(file[0])-1:
                if file[i+1][j+1] in digits:
                    coords.append((i+1,j+1))
    return coords




if __name__ == "__main__":
    file = open(r"inputs/day3.txt", "r").readlines()
    print(count(file))
