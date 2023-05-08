"""
This example code creates a 2d list (2d matrix) that can store seating.
The matrix is populated with . since all seats are available
"""

def menu():
    print("---------------------------------------------------------")
    print("          Welcome to the Outdoor Park Concert App!       ")
    print("---------------------------------------------------------")
    print()
    print("[v] view seating")
    print("[b] buy tickets")
    print("[s] search for a customer name and display the tickets purchased")
    print("[d] display all the pirchase made and total amount of income")
    print("[q] to quit")
    print()
    userInput = input("Enter a command: ")
    lowerInput = userInput.lower()
    firstChar = lowerInput[0:1]

    userQuit = False
    while (not userQuit):

		#calling the menu function
	    menu()
userInput = input("Enter a command: ")
lowerInput = userInput.lower()
firstChar = lowerInput[0:1]

if firstChar == 'v':
     



# our test matrix has 4 rows and 10 columns
n_row = 4
n_col = 10

# available seat
available_seat = '.'

# create some available seating
seating = []
for r in range(n_row):
    row = []
    for c in range(n_col):
        row.append(available_seat)
    seating.append(row)

# print available seating
for r in range(n_row):
    print(r+1, end="\t")
    for c in range(n_col):
        print(seating[r][c], end=" ")
    print()
