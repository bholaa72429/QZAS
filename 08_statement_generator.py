# statement generator ( to enhance aesthetics )

# function
def h1_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print()

# Main routine
correct = h1_statement("~~ You have enterd the correct answer .~~", "~")
print()
incorrect = h1_statement("vv You have enterd the incorrect answer   vv", "v")
print()
error = h1_statement("** Please entre an integer  ***", "*")
print()
start_round = h1_statement("--Round 1 of 3 --", "-")
