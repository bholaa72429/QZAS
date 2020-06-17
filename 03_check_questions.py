# generate two random number
# put them together in an equation (n + n = )
# get users input
# check if it's right or wrong
# also give feedback to invalid string
import random

for i in range(5):
# generating two random number
    num_one = random.randint(1,10)
    num_two = random.randint(1,10)
    valid = False
    while not valid:
        try:
            # putting it in an equation
           equation = int(input("Please answer the question {} + {} = ".format(num_one,num_two)))
           answer = num_one + num_two
           # check if it right/wrong and give feedback
           if equation == answer:
             print("Correct")
             break
           else:
             print("Incorrect")
             print("THE CORRECT ANSWER IS: {}".format(answer))
             break
        except ValueError:
            print("Whoops! Please enter an number ")