from string import digits


class Hand():
    def __init__(self, cards, bid) -> None:
        self.cards = cards
        self.bid = int(bid)
        self.__type = self.__find_type()
        self.__better = None
        self.__worse = None

    def __find_type(self):
        cards = {"A": 0,
                 "K": 0,
                 "Q": 0,
                 "T": 0,
                 "9": 0,
                 "8": 0,
                 "7": 0,
                 "6": 0,
                 "5": 0,
                 "4": 0,
                 "3": 0,
                 "2": 0}
        jokers = 0

        for card in self.cards:
            if card == "J":
                jokers += 1
            else:
                cards[card] += 1

        cards[max(cards, key=cards.get)] += jokers
        
        if 5 in cards.values():
            return 0
        if 4 in cards.values():
            return 1
        if 3 in cards.values():
            if 2 in cards.values():
                return 2
            return 3
        pairs = len([key for key in cards.keys() if cards[key] == 2])
        if pairs == 2:
            return 4
        if pairs == 1:
            return 5
        else:
            return 6
        
    def get_type(self):
        return self.__type

    def get_better(self):
        return self.__better
    
    def get_worse(self):
        return self.__worse
    
    def set_better(self, better):
        self.__better = better

    def set_worse(self, worse):
        self.__worse = worse

    def beats(self, opponent):
        values = {"A": 14,
                  "K": 13,
                  "Q": 12,
                  "J": 1,
                  "T": 10,
                  "9": 9,
                  "8": 8,
                  "7": 7,
                  "6": 6,
                  "5": 5,
                  "4": 4,
                  "3": 3,
                  "2": 2}
        for i in range(5):
            a = values[self.cards[i]]
            b = values[opponent.cards[i]]
            if a > b:
                return True
            if b > a:
                return False
        return False

    def rank(self):
        type_list = types[self.get_type()]
        if self in type_list: return
        type_list.append(self)
        if len(type_list) == 1:
            return
        competitor = type_list[0]
        if self.beats(competitor):
            while True:
                self.set_worse(competitor)
                if competitor.get_better() == None:
                    competitor.set_better(self)
                    self.set_better(None)
                    return
                competitor = competitor.get_better()
                self.set_better(competitor)
                if not self.beats(competitor):
                    competitor.set_worse(self)
                    self.get_worse().set_better(self)
                    return
        else:
            while True:
                self.set_better(competitor)
                if competitor.get_worse() == None:
                    competitor.set_worse(self)
                    self.set_worse(None)
                    return
                competitor = competitor.get_worse()
                self.set_worse(competitor)
                if self.beats(competitor):
                    competitor.set_better(self)
                    self.get_better().set_worse(self)
                    return

    def find_top(self):
        better = self.get_better()
        if better:
            return better.find_top()
        else:
            return self
    
    def __str__(self) -> str:
        return f"Cards: {self.cards}, Bid: {self.bid}"

five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pair = []
one_pair = []
high_card = []

types = [five_of_a_kind,
         four_of_a_kind,
         full_house,
         three_of_a_kind,
         two_pair,
         one_pair,
         high_card
         ]


def count(file):
    rank = 0
    total_winnings = 0
    for line in file:
        rank += 1
        line = line[:-1].split(" ")
        cards = line[0]
        bid = line[1]
        hand = Hand(cards, bid)
        hand.rank()
    for type in types:
        current = type[0].find_top()
        while current:
            total_winnings += current.bid * rank
            rank -= 1
            current = current.get_worse()
    return total_winnings

if __name__ == "__main__":
    file = open(r"inputs/day7.txt","r").readlines()
    print(count(file))
