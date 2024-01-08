from re import split


def count(file):
    times = [int(time) for time in split("\s+", file[0][13:36])]
    records = [int(time) for time in split("\s+", file[1][12:36])]

    ways = 1
    for i in range(len(times)):
        for j in range(times[i]):
            if j * (times[i]-j) > records[i]:
                break
        ways *= times[i] - j*2 + 1
    
    return ways



if __name__ == "__main__":
    file = open(r"inputs/day6.txt","r").readlines()
    print(count(file))
