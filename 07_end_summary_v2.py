# --modify my end game summary--
# -- add variety in feedback--


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
correct_round = 0
won = 0
lost = 0
# defining the following terms
question = ""
answer = ""
comment = ""
equation = ""
right = 0
wrong = 0
# empty list to store the question therefore hold the history
game_history = []

# question counter
while rounds_played < rounds:
    print("Question {} of {} ".format(rounds_played+1,rounds))
    rounds_played += 1

    # generating two random number
    symbol = ['+', '-', '*']
    # variety of feedbacks
    good_comm = ["Good job!", "Well done!", "Keep it up! ", "Prefect!","Excellent Work!"]
    bad_comm = ["Wrong","Not right","Try again","Oops","Incorrect",]
    # randomly generating two numbers and symbol to form a equation
    num_one = random.randint(1, 15)
    num_two = random.randint(1, 10)
    sign = random.choice(symbol)


    valid = False
    while not valid:
        try:
            # putting it in an equation
            equation = int(input("Please answer the question {} {} {} = ".format(num_one, sign, num_two)))
            # made to display question in end history
            question = ("{} {} {} = {} ".format(num_one, sign, num_two,equation))
            answer = check(num_one, sign, num_two)
            # check if it right/wrong and give feedback
            if equation == answer:
                comment = "Correct"
                print(random.choice(good_comm))
                # to calculate percentage
                correct_round += 1
                # to calculate total right answers
                right += 1
                break
            else:
                comment = "Incorrect"
                print(random.choice(bad_comm))
                wrong += 1
                print("THE CORRECT ANSWER IS: {}".format(answer))
                break
        # if user enters invalid
        except ValueError:
            print("Whoops! Please enter an number ")
    # end game history
    if comment == "Correct":
        rounds_result = "Question {}: {} |  Result: {} " .format(rounds_played,question,comment)
        game_history.append(rounds_result)
    # If users guess is wrong then display this
    else:
        rounds_result = "Question {}: {} |  Result: {} | Correct Answer = {} " .format(rounds_played,question,comment,answer)
        game_history.append(rounds_result)
# to calculate percentage
percentage = int(correct_round/rounds*100)
# to print game stats
print()
print("****Game Statistics****")
print("Your Accuracy Rate is  {} % ".format(percentage))
print("You Got Total {} Correct ".format(right))
print("You Got Total {} Incorrect ".format(wrong))

# to print end game summary
print()
print("**** Summary ****")

for item in game_history:
    print(item)
