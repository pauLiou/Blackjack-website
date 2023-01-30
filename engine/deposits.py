class Bank:
    def __init__(self,current_funds):
        self.current_funds = current_funds
        self.chips = ['1','2','5','10','20','50','100','500']


def make_bet(player):
    if player.bank > 1:

        print('Current funds: ', player.bank)
        bet = input('How much would you like to bet? ')
        player.bank -= int(bet)
        return player,bet
    else:
        print('Out of funds, please add some more!')
    


def winner_calculation(player,house,bet,outcome):
    if house.value <= 21: # neither side busts
        if outcome == 'Value':
            if player.value > house.value:
                print('You have won', str(int(bet)*2))
                player.bank += int(bet)*2 # return double bet
            elif player.value < house.value:
                print('You have lost!')
            elif player.value == house.value:
                print('Push!')
                player.bank += int(bet) # return bet
    elif outcome == 'Blackjack': # blackjack means auto win
        player.bank += int(bet)*2.5 # return 2.5 times bet
    else: # house busts
        print('You have won')
        player.bank += int(bet)*2 # return double bet
        

def check_conditions(score):
    # see if the player has a blackjack (1.5 payout)
    if score == 21:
        print('21! Blackjack! You win!')
        return 'Blackjack'

    # see if the player has busted (0 payout)
    elif score > 21:
        print(score)
        print('Busted! You have lost!')
        return 'Bust'
    else:
        return 'Value'

