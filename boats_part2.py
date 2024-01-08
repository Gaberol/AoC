from re import split


def count(file):
    times = split("\s+", file[0][13:36])
    records = split("\s+", file[1][12:36])

    time = ""
    for t in times:
        time += t
    time = int(time)

    record = ""
    for r in records:
        record += r
    record = int(record)

    for i in range(time):
        if i * (time-i) > record:
            break
    
    return time - i*2 + 1



if __name__ == "__main__":
    file = open(r"inputs/day6.txt","r").readlines()
    print(count(file))
