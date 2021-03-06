################################################################################
#                                 BlackJack game
# Features :
#    - 1 to 4 players
#    - random player's and dealer's card
#    - dealer hit while his score <17
#    - hit, stand, double, split or quit
#    - bets can be picked
#    - manage amount of player's money, with bonuses for double, split and blackjack
#    - use OOP
#    - lots of fun
################################################################################

# to split : use set() iot see if there are double items (len(set(l))<len(l))

from random import *

################################################################################
#    Function : print the game on the board
################################################################################
def printGame(player, cards, points, money = 100, bet = 10, win = 0, final = 'no'):
    """
    print board
    :returns: display board with played cards, and useful infos for players
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
    else:
        if final == 'yes':
            screen += " Hand score   : " + str(points) + " points.\n"

    # add comments if Blackjack !
    print(screen)

################################################################################
#   Function : define the player's number
################################################################################

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

################################################################################
#    Define the dealer object with methods
################################################################################

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
                self.score += int(card)
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
                printGame(self.name, self.cards, self.calculPoint(), final = 'yes')
                #  print("Congrats, I'm BUSTED, take your money...\n\n")
                return('busted')
                break
            # check if simple win (score = 21) : stop the turn
            elif self.calculPoint() == 21:
                printGame(self.name, self.cards, self.calculPoint(), final = 'yes')
                #  print("I WON, or I didn't loose, nevermind, gimme your money !")
                return('win')
                break
            # break the loop if dealer score < 21 and no simple winner : compare scores with another function
            else:
                #  print("We have to check")
                return(self.calculPoint())
                break

################################################################################
#    Define the player object, inherit from dealer
################################################################################

class Player(Dealer):
    """
    Player object, inherit from Dealer
    init : name, money
    method :
    return : a list of cards, money, bet and point of hand
    """

    def __init__(self, money, number, bet = 0, quit = 'no', bonus = 'none'):
        Dealer.__init__(self)
        # number to ask for player name
        self.name = input('Player ' + str(number) + ', what is your name ? ')
        self.bet = bet
        self.money = money
        self.quit = quit
        self.bonus = bonus

    def playTurn(self):
        self.bet = input(str(self.name) + ", what's your bet ? ")
        while True:
            try:
                int(self.bet)
            except:
                print('Be kind ' + str(self.name) + ', please bet an integer...')
                self.bet = input("What's your bet ? ")
                continue
            else:
                while int(self.bet) > int(self.money):
                    print("Come on, you can't bet more than you have...")
                    self.bet = input("Now, what's your bet ? ")
                break
        nextMove = ''
        self.money = int(self.money) - int(self.bet)
        while True:
            printGame(self.name, self.cards, self.calculPoint(), bet = self.bet, money = self.money)
            if self.calculPoint() > 21:
                print("Sorry, but you're BUSTED, gimme your money and... NEXT !\n")
                return('busted')
                break
            elif self.calculPoint() == 21:
                return('win')
                print("Congrat's, you WON ! Take your money !\n")
                break

            #  nextMove = input("What's your next move ? \n [H]it - [S]tand - [D]ouble - Spli[t] - [Q]uit\n ")
            nextMove = input("What's your next move ? \n [H]it - [S]tand - [D]ouble - [Q]uit\n ")
            bonus = {'H':1, 'S':1, 'D':2, 'T':2, 'Q':1, 'h':1, 's':1, 'd':2, 't':2, 'q':1}
            self.bonus = bonus[nextMove]
            if nextMove in 'HhDd':
                self.hit()
            if nextMove in 'DdSs':
                return(self.calculPoint())
            if nextMove in 'Qq':
                self.quit = 'yes'
                break

    def calculMoney(self, winLoss):
        # use self.money to use player's money and self.bonus depending of the choices
        if winLoss == 'win':
            #  self.money += int(self.bet) * (1 + bonusCoef[self.bonus])
            self.money += int(self.bet) * (1 + float(self.bonus))
        elif winLoss in ['busted','lost']:
            #  self.money += int(self.bet) * (bonusCoef[self.bonus] - 1)
            self.money -= int(self.bet) * (float(self.bonus) - 1)
        elif winLoss == 'draw':
            self.money += int(self.bet)
        else:
            pass

################################################################################
#    Intro
################################################################################

intro = 'BlackJack\n'
intro += '========='

d = Dealer()

print(intro)
################################################################################
#    Initiate the game : nb of players and names
################################################################################

nbPlayer = playerNb()
initialMoney = input("How many bucks for the players ? \n")

try:
    int(initialMoney)
except:
    print("Please enter an integer...\n")
    initialMoney = input("How many bucks for the players ? \n")
else:
    print("Let's the party begin !\n")


################################################################################
#    Manage the game, the score and the player's money
################################################################################
# display cards fos each players and dealer
# use dict instead of increment variable name... Usefull to use players for another round, or abandon, or etc.
players = {}

anotherRound = 'y'
roundCount = 0
while anotherRound in 'yY':
    # first round : create players
    if roundCount == 0:
        for n in range(1, nbPlayer + 1):
            players[n] = Player(int(initialMoney), n)
            # check if there is a blackjack
            if players[n].calculPoint() == 21:
                players[n].bonus = 1.5
                print("\nBLACKJACK !!! Woowoowoop !!!")
        roundCount = 1
    # reset cards for another round
    else:
        for n in players:
            players[n].resetCards()
            # check if there is a blackjack
            if players[n].calculPoint() == 21:
                players[n].bonus = 1.5
                print("\nBLACKJACK !!! Woowoowoop !!!")
        d.resetCards()

    # manage players turn with playTurn() method
    countLost = 0
    for n in players:
        # allow only player with money to play
        if players[n].money > 0:
            printGame(d.name, d.cards, d.calculPoint())
            result = players[n].playTurn()
            #  players[n].calculMoney(result)
        else:
            print(players[n].name + ", you can't play : you don't have money anymore")
            countLost += 1
    # check if all have lost, end of game
    if countLost == len(players):
        print("\nOk, you all have lost, goodbye felows, thanks for the money !")
        break

    # check if all players have quit
    abandon = 0
    for p in players:
        if players[p].quit == 'yes':
            abandon += 1
    if abandon == len(players):
        print("\nYou're all cowards, I'm too good for you, see you !")
        break

    # dealer'r turn, with it's own method
    d.playTurn()

    # compare players game with dealer
    # possibly have to change busted and win rules
    for p in players:
        # check if player has quit or not
        if players[p].quit == 'yes':
            print("Ok " + players[p].name + " , you can be a coward if you want to...\n")
            players[p].calculMoney('lost')
        else:
            points = players[p].calculPoint()
            if points > 21:
                print(players[p].name + ", you're BUSTED")
                players[p].calculMoney('lost')
            else:
                if d.calculPoint() > 21:
                    print("OMG, impossible, I'm... I'm BUSTED..." + players[p].name + ", you have to be paid...\n")
                    players[p].calculMoney('win')
                elif points == d.calculPoint():
                    print("Ladies and gentlemen, we have a draw with " + players[p].name + " !\n")
                    players[p].calculMoney('draw')
                elif points > d.calculPoint():
                    print("NOOOOOO ! I've lost ! I'm gonna kill you, you ear me " + players[n].name + " ?\n")
                    players[p].calculMoney('win')
                elif points < d.calculPoint():
                    print("Ahahahahahahaha, I've WON, you 'dear' " + players[n].name + " !\n")
                    players[p].calculMoney('lost')

    print("----------------------")
    for p in players:
        print(" " + players[p].name + " : " + str(players[p].money) + " dollars left.")
    print("----------------------")
    anotherRound = input("Another round ? \n[Y]es - [N]o : ")
    if anotherRound in 'nN':
        print("\nOk that was fun, see you bro!\n")
