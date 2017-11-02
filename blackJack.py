#  Todo : blackjack text
#  1. one player vs automated dealer
#  2. player can stand or hit
#  3. player must be able to pick his betting amount
#  4. keep track of player total money
#  5. alert the player of wins, losses, busts, etc.
#  6. use OOP
#  7. can add other players

from random import *

def printGame(player, cards, points, money = 100, bet = 10, win = 0):
    """
    print board
    :cartes: TODO
    :returns: display board with played cards, and usefull infos for players
    """
    if player == 'dealer':
        screen += "Dealer's cards :\n"
    else:
        screen = player + ", your cards :\n"

    screen += len(cards) * " ----- " + "\n"
    for card in cards:
        screen += " | " + str(card) + " | "
    screen += "\n" + len(cards) * " ----- " + "\n"
    screen += " You have " + str(points) + " points.\n"
    screen += " You have " + str(money) + " dollars left.\n"
    screen += " Your bet is actually " + str(bet) + " dollars, and you could win " + str(win) + " dollars."
    # add comments if Blackjack !
    return screen


def winLoss(player):
    """TODO: determinate if player has won or not
    use Player object
    :returns: win, loss or busted !
    """
    if player.calculPoint() > 21:
        return('busted')
    pass


class Dealer(object):
    """
    Dealer object
    return : a list of cards and point of hand 
    """
    # set the same game for all players
    game = list(range(2, 11))
    heads = ['J', 'Q', 'K', 'A']
    for card in heads:
        game.append(card)

    def __init__(self):
        # initiate the 2 first cards of game
        n1 = randint(0, len(self.game) - 1)
        n2 = randint(0, len(self.game) - 1)
        self.cards = [self.game[n1], self.game[n2]]

    def hit(self):
        nb = randint(0, len(self.game) - 1)
        self.cards.append(self.game[nb])
        return(self.cards)

    def calculPoint(self):
        # create dictionary for points calcul
        # A = 1 if score > 21
        points = {'A':11, 'K':10, 'Q':10, 'J':10}
        score = 0
        for card in self.cards:
            try:
                int(card)
            except:
                score += points[card]
            else:
                score += card
        return(score)


class Player(Dealer):
    """
    Player object, to create player on demand
    return : a list of cards, money, bet and point of hand 
    """

    def __init__(self, name, money):
        Dealer.__init__(self)
        self.name = name
        self.money = money

    def addCarte(self, hitStand):
        newCard = {'hit': 1, 'double': 1, 'stand': 0}
        pass

    def calculWin(self, bet, hitStand):
        """
        bonus : double, blackjack, split
        Faire dictionnaire avec les gains possibles
        """
        bonus = {'blackjack':1.5, 'double':2, 'split':2}
        pass

    def calculMoney(self, winLoss):
        # use self.money to use player's money
        # use calculWin
        pass


# for intro
intro = 'BlackJack\n'
intro += '=========\n'
print(intro)

# set 2 initial random cards for each players...
cartes = []
names = ['Emicile','Lumilie']


d = Dealer()
p1 = Player(names[0], 100)
p2 = Player(names[1], 200)
print(printGame(p1.name, p1.cards, p1.calculPoint()))
print(d.cards)
print(d.hit())
