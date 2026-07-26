import random


def generate_number() -> int:
    '''
    Generate a pseudorandom number
    
    Realistically, this does not need to be it's own function however will remain one.
    '''
    return random.randint(1, 100)

def main() -> None:
    number = generate_number() # This must not be in the loop, if it is a new number will be generated every time.. poor user..
    print(number)
    
    # 'Game' loop
    while True:
        user_guess = input('Enter a number (1-100): ')
        if int(user_guess) == number:
            break

        print('Nope! Try again.')

    print('You got it!')

if __name__ == '__main__':
    main()