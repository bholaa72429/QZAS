# combine the previous version
# that is ....
# User input (number of questions)
# question counter
# asking question + checking and giving feedback

import random

# int-check function for the rounds
def intcheck(question,low,high):
    valid = False
    error = "Whoops! Please enter an number "
    while not valid:
        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print("Please Enter a Number between 1 and 10")
                print()

        except ValueError:
            print(error)

# function to check the answer
def check(num_one, sign, num_two):
 # For addiction
    if sign == '+':
        ans_add = num_one + num_two
        return ans_add
    # For subtraction
    elif sign == '-':
        ans_minus = num_one - num_two
        return ans_minus
    # For multiplication
    else:
        ans_multiply = num_one * num_two
        return ans_multiply

# Main routine
rounds = intcheck("How many questions would you like to play with ? ", 1, 10)
rounds_played = 0

# question counter
while rounds_played < rounds:
    print("Question {} of {} ".format(rounds_played+1,rounds))
    rounds_played += 1

    # generating two random number
    symbol = ['+', '-', '*']
    num_one = random.randint(1, 15)
    num_two = random.randint(1, 10)
    sign = random.choice(symbol)

    valid = False
    while not valid:
        try:
            # putting it in an equation
            equation = int(input("Please answer the question {} {} {} = ".format(num_one, sign, num_two)))
            answer = check(num_one, sign, num_two)
            # check if it right/wrong and give feedback
            if equation == answer:
                print("Correct")
                break
            else:
                print("Incorrect")
                print("THE CORRECT ANSWER IS: {}".format(answer))
                break
                # if user enters invalid
        except ValueError:
            print("Whoops! Please enter an number ")