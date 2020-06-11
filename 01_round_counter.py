# ask how many number of rounds
# rounds statement (i.e round 1 )

rounds = int(input("How many rounds would you like to play? "))
rounds_played = 0

while rounds_played < rounds:
    print("Round {}".format(rounds_played+1))
    rounds_played += 1

print("check - round - end")
