from re import split


def count(file):
    cards = {i: 1 for i in range(1, len(file)+1)}
    for card in cards.keys():
        line = file[card-1][10:-1].split(" | ")
        winning = list(filter(None, split("\s+", line[0])))
        numbers = list(filter(None, split("\s+", line[1])))
        wins = 0
        for num in numbers:
            if num in winning:
                wins += 1             
        if wins == 0: continue
        for i in range(1,wins+1):
            cards[card+i] += cards[card]
    return sum(cards.values())


if __name__ == "__main__":
    file = open(r"inputs/day4.txt","r").readlines()
    print(count(file))