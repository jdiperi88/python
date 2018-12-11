###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number


# GET GUESS
import random


def get_guess():
    return list(input('What is your guess?'))

# GENERATE COMPUTER CODE


def generate_code():
    digits = [str(num) for num in range(10)]

    # shuffle the digits
    random.shuffle(digits)
    # grab first three digits
    return digits[: 3]


def generate_clues(code, user_guess):
    if user_guess == code:
        return 'code cracked!'
    clues = []

    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append('match')
        elif num in code:
            clues.append('close')
        if clues == []:
            return ['nope']
        else:
            return clues


print('Welcome code breaker!')

secret_code = generate_code()

clue_report = []
print(secret_code)

while clue_report != 'code cracked!':
    guess = get_guess()

    clue_report = generate_clues(guess, secret_code)

    print('Here is the result of your guess')
    for clue in clue_report:
        print(clue)
