#  Todo : blackjack text
#  1. one player vs automated dealer
#  2. player can stand or hit
#  3. player must be able to pick his betting amount
#  4. keep track of player total money
#  5. alert the player of wins, losses, busts, etc.
#  6. use OOP
#  7. can add other players

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


def winLoss(player):
    """TODO: determinate if player has won or not
    use Player object
    :returns: win, loss or busted !
    """
    if player.calculPoint() == 21:
        return('blackjack')
    elif player.calculPoint() > 21:
        return('busted')
    pass


def playerNb():
    """TODO: Docstring for nbPlayer.
    :returns: number of players
    """
    #  while int(nb) not in range(1,5):
        #  nb = input('Number of players (1 to 4) :')
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


#  def playerName(nb):
    #  """TODO: Docstring for playerName.
    #  :nb: number of players 
    #  :returns: a list with the name of the players
    #  """
    #  names = []
    #  for n in range(0, nb):
        #  query = 'Player ' + str(n+1) + ', what is your name ? '
        #  names.append(input(query))
    #  return(names)    


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
        #  self.cards = ['A', 'K' , 2]
        self.name = 'dealer'

    def hit(self):
        nb = randint(0, len(self.game) - 1)
        self.cards.append(self.game[nb])
        return(self.cards)

    def calculPoint(self):
        # create dictionary for points calcul
        points = {'A':11, 'K':10, 'Q':10, 'J':10}
        score = 0
        for card in self.cards:
            # try method iot use value of cards
            try:
                int(card)
            except:
                score += points[card]
            else:
                score += card
        # set value of 'A' to 1 if score to high
        if score > 21 and 'A' in self.cards:
            score -= 10
        return(score)


class Player(Dealer):
    """
    Player object, inherit from Dealer
    init : name, money
    method : 
    return : a list of cards, money, bet and point of hand 
    """

    #  def __init__(self, name, money):
    def __init__(self, money, number):
        Dealer.__init__(self)
        self.name = input('Player ' + str(number) + ', what is your name ? ')
        self.money = money

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
        if winLoss == 'win':
            self.money += self.bet
        elif winLoss == 'loss':
            self.money -= self.bet
        elif winLoss == 'draw':
            pass


# for intro
intro = 'BlackJack\n'
intro += '========='

d = Dealer()

print(intro)
# initiate the game : nb of players and names
nbPlayer = playerNb()
#  names = playerName(nb)

printGame(d.name, d.cards, d.calculPoint())
# display cards fos each players and dealer
for n in range(1, nbPlayer + 1):
    p = Player(400, n)
    initialBet = input("What's your bet ? ")
    nextMove = ''
    while nextMove != 'Q':
        printGame(d.name, d.cards, d.calculPoint())
        printGame(p.name, p.cards, p.calculPoint(), bet = initialBet, money = p.money)
        nextMove = input("What's your next move ? \n H for hit - Q for Stand - D for double - S for Split\n ")
        if nextMove in 'HD':
            p.hit()
