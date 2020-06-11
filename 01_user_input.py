# user input ( rounds )

# To do:
# ask the number of rounds
# check its an valid integer in range 1 to 10 and also check boundaries
# if yes then continue the program
# if no then provide with an error message

# Integer checking function below

# Integer checking function below
def intcheck(question,low=1,high=10):
    valid = False
    error = "Whoops! Please enter an integer "
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

rounds = intcheck("How many rounds would you like to play with ? ", 1, 10)


