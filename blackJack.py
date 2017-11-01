#  Todo : blackjack text
#  1. one player vs automated dealer
#  2. player can stand or hit
#  3. player must be able to pick his betting amount
#  4. keep track of player total money
#  5. alert the player of wins, losses, busts, etc.
#  6. use OOP
#  7. can add other players

game = range(2, 11)
heads = ['J', 'Q', 'K', 'A']
for carte in heads:
    game.append(carte)
#  complete game for 4 colors
game = 4 * game

print(game)

# for intro
screen = 'BlackJack\n'
screen += '=========\n'
print(screen)

def printGame(cartes, points):
    """
    print board
    :cartes: TODO
    :returns: display board with played cards
    """
    screen = "Your cards : \n"
    screen += "-----   -----\n"
    screen += "| " + cartes[0] + " |   | " + cartes[1] + " |\n"
    screen += "-----   -----\n\n"
    screen += "You have " + points + " points."
    # add comments if Blackjack !
    return screen


class Main(object):

    """
    Cards of players, with methods to add and calcul points
    return a list of cards for players
    """

    def __init__(self):
        """TODO: to be defined1. """
        pass

    def calculPoint(self, cartes):
        pass


cartes = ['A', 'K']
print(printGame(cartes, '21'))
