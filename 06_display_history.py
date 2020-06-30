import random

# Number of rounds
how_many = 5
# Number of rounds won
won = 0
# Number of rounds lost
lost = 0

# empty list to store the question therefore hold the history
game_history = []

for item in range(1, how_many + 1 ):
    question = ("What is 5 + 6 = ?")
    result = input(" What is 5 + 6 ? ")

    if result == "11":
        feedback = "You Won"
        won += 1
    else:
        feedback = "You Lost"
        won += 1
    rounds_result = "Question {}: {} | Your response: {} | Result: {}".format(item,question,result,feedback)
    game_history.append(rounds_result)

print()
print("**** Result ****")

for item in game_history:
    print(item)