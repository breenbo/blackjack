#  Todo : blackjack text
#  1. one player vs automated dealer
#  2. player can stand or hit
#  3. player must be able to pick his betting amount
#  4. keep track of player total money
#  5. alert the player of wins, losses, busts, etc.
#  6. use OOP
#  7. can add other players

########################################

#  for split : use set() iot see if there are double items (len(set(l))<len(l))

from random import *

def printGame(player, cards, points, money = 100, bet = 10, win = 0, final = 'no'):
    """
    print board
    :returns: display board with played cards, and usefull infos for players
    """
    # use intermediate variable carte=list() unless both variables change
    cartes = list(cards)

    if player == 'dealer':
        # hide the first dealer's card during the game
        if final == 'no':
            cartes[1] = ' '
        # display the 'title'
        screen = "\nDealer's cards :\n"
    else:
        screen = "\n" + player + ", your cards :\n"

    # display the common screen (the cards for all players and the dealer)
    screen += len(cartes) * " ----- " + "\n"
    for card in cartes:
        screen += " | " + str(card) + " | "
    screen += "\n" + len(cartes) * " ----- " + "\n"

    # for players only
    if player != 'dealer':
        screen += " Hand score   : " + str(points) + " points.\n"
        screen += " Money        : " + str(money) + " dollars left.\n"
        screen += " Bet          : " + str(bet) + " dollars\n"
        screen += " Possible win : " + str(win) + " dollars.\n"

    # add comments if Blackjack !
    print(screen)


def playerNb():
    """TODO: Docstring for nbPlayer.
    :returns: number of players
    """
    nb = 0
    while nb not in range(1, 5):
        print('Please choose 1 to 4 players.')
        nb = input('Number of players : ')
        while True:
            try:
                nb = int(nb)
            except:
                print('Please enter a integer.')
                nb = input('Number of players : ')
                continue
            else:
                break
    return(nb)


class Dealer(object):
    """
    Dealer object
    init : 2 random cards
    methods : hit, score of hand
    return : list of cards, point of hand 
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
        self.name = 'dealer'
        self.score = 0

    def resetCards(self):
        """TODO: Docstring for resetCards.
        :returns: a new pair of cards for another round
        """
        n1 = randint(0, len(self.game) - 1)
        n2 = randint(0, len(self.game) - 1)
        self.cards = [self.game[n1], self.game[n2]]
        self.score = 0

    def hit(self):
        nb = randint(0, len(self.game) - 1)
        self.cards.append(self.game[nb])
        return(self.cards)

    def calculPoint(self):
        # create dictionary for points calcul
        points = {'A':11, 'K':10, 'Q':10, 'J':10}
        self.score = 0
        for card in self.cards:
            # try method iot use value of cards or points list
            try:
                int(card)
            except:
                self.score += points[card]
            else:
                self.score += card
        # set value of 'A' to 1 if self.score to high
        if self.score > 21 and 'A' in self.cards:
            self.score -= 10
        return(self.score)

    def playTurn(self):
        printGame(self.name, self.cards, self.calculPoint(), final = 'yes')
        while True:
            while self.calculPoint() < 17:
                self.hit()
                printGame(self.name, self.cards, self.calculPoint(), final = 'yes')

            if self.calculPoint() > 21:
                print("Congrats, I'm BUSTED, take your money...\n\n")
                return('busted')
                #  print("Sorry, but you're BUSTED ! Gimme your money...\n\n")
                break
            # check if simple win (score = 21) : stop the turn
            elif self.calculPoint() == 21:
                return('win')
                print("I WON, or I didn't loose, nevermind, gimme my money !")
                break
            # break the loop if dealer score < 21 and no simple winner : compare scores with another function
            else:
                print("We have to check")
                return(self.calculPoint())
                break

class Player(Dealer):
    """
    Player object, inherit from Dealer
    init : name, money
    method : 
    return : a list of cards, money, bet and point of hand 
    """

    def __init__(self, money, number):
        Dealer.__init__(self)
        # number to ask for player name
        self.name = input('Player ' + str(number) + ', what is your name ? ')
        self.bet = input("What's your bet ? ")
        self.money = money

    def playTurn(self):
        #  bet = input("What's your bet ? ")
        while True:
            try:
                int(self.bet)
            except:
                print('Please bet an integer...')
                self.bet = input("What's your bet ? ")
                continue
            else:
                break
        nextMove = ''
        while True:
            printGame(self.name, self.cards, self.calculPoint(), self.bet, self.money)
            if self.calculPoint() > 21:
                print('BUUUSTED !')
                return('busted')
                break
            elif self.calculPoint() == 21:
                return('win')
                #  print(winPrint)
                #  print("You WON ! Take your money !\n")
                break

            nextMove = input("What's your next move ? \n H for hit - S for Stand - D for double - T for Split - Q for quit\n ")
            if nextMove in 'HhDd':
                self.hit()
            elif nextMove in 'SsQq':
                return(self.calculPoint())
                break

    def calculMoney(self, winLoss):
        bonus = {'blackjack':1.5, 'double':2, 'split':2}
        # use self.money to use player's money
        if winLoss == 'win':
            self.money += int(self.bet)
        elif winLoss == 'lost':
            self.money -= int(self.bet)
        elif winLoss == 'draw':
            pass


# for intro
intro = 'BlackJack\n'
intro += '========='

d = Dealer()

print(intro)
# initiate the game : nb of players and names
nbPlayer = playerNb()
initialMoney = input("How many bucks for the players ? \n")
try:
    int(initialMoney)
except:
    print("Please enter an integer...\n")
    initialMoney = input("How many bucks for the players ? \n")
else:
    print("Let's the party begin !\n")

printGame(d.name, d.cards, d.calculPoint())
# display cards fos each players and dealer
players = {}
# use dict instead of increment variable name... Usefull to use players for another round, or abandon, or etc.
# first round : create players
roundCount = 0
if roundCount == 0:
    for n in range(1, nbPlayer  + 1):
        players[n] = Player(int(initialMoney), n)
    roundCount += 1

anotherRound = 'y'
while anotherRound in 'yY':
    for n in range(1, nbPlayer + 1):
        #  players[n] = Player(int(initialMoney), n)
        #  players[n].playTurn()
        result = players[n].playTurn()
        if result == 'busted':
            players[n].calculMoney('lost')
            print(players[n].money)
    d.playTurn()

    anotherRound = input("Another round ? \nY - N : ")
