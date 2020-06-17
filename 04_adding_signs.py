# add subtraction, multiplication questions together with addition and randomly generating them
#  check it works as required


import random
# function to check the answer
def check(num_one,sign,num_two):
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

symbol = ['+','-','*']
for i in range(5):
    # generating two random number
    num_one = random.randint(1,15)
    num_two = random.randint(1,10)
    sign = random.choice(symbol)
    valid = False
    while not valid:
        try:
            # putting it in an equation
           equation = int(input("Please answer the question {} {} {} = ".format(num_one,sign,num_two)))
           answer = check(num_one,sign,num_two)
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