import random


def get_player_choice() -> str: # Indicates that the function will return a string
    '''
    This function just puts all the logic for the input and validation of the players choice.
    This could be cleaner, but this implementation does work, the other possible implementation can be seen below.
    '''
    # We use a while loop here to ensure the user selects a valid input, it breaks when one is selected
    while True:
        # Take input
        player_choice = input('Rock, paper, scissors? ')
        # Match the formatted input to valid options 
        match player_choice.lower().strip(): # .lower() changes all uppercase to lower (i.e ABC -> abc) .strip() removes trailing whitespace
            case 'rock':
                return 'rock'
            case 'paper':
                return 'paper'
            case 'scissors':
                return 'scissors'
            case _: # case _ catches every other case
                print('Invalid option, you must select rock, paper, or scissors.')

'''
def get_player_choice() -> str:
    while True:
        player_choice = input('Rock, paper, or scissors? ').lower().strip()
    
        match player_choice:
            case 'rock' | 'paper' | 'scissors':
                return player_choice
            case _:
                print('Invalid option, you must select rock, paper, or scissors.')
'''

def get_computer_choice() -> str: # Indicates that the function will return a string
    '''
    This function generates the computer's choice pseudorandomly*

    * I recommend reading up on this topic, it's highly intriguing
    '''

    return random.choice(['rock', 'paper', 'scissors']) # Each element in the list has a 1 in 3 chance to be chosen, then gets returned.

def determine_winner(player: str, computer: str) -> str:
    """Return the round result based on the player's and computer's choices."""
    if player == computer:
        return 'Try again! Draw.'

    # We create a set of tuples to set the conditions in which the player wins.
    # Values are set out in the following format (PLAYER, COMPUTER)
    player_wins = {
        ('rock', 'scissors'),
        ('paper', 'rock'),
        ('scissors', 'paper')
    }

    if (player, computer) in player_wins:
        return 'You win!'

    return 'You lose! Better luck next time.'
    
def main() -> None:
    print(determine_winner(get_player_choice(), get_computer_choice())) # Calls determine winner, get_player_choice and get_computer_choice 

if __name__ == '__main__':
    main()
