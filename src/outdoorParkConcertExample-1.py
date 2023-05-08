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
    

userQuit = False
while (not userQuit):

		#calling the menu function
    menu()
    userInput = input("Enter a command: ")
    lowerInput = userInput.lower()
    firstChar = lowerInput[0:1]

    if firstChar == 'v':
     # call function printSeating()
        printSeating()
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

   # elif firstChar == 'b':
     # call function buyTickets()
    elif firstChar == 'q':
        userQuit = True
    else:
        print("ERROR: " + firstChar + " is not a valid command")

print("\n")
print("Thank you for using the Outdoor Park Concert App!")
print("\n")
     
#def createSeating():


def printSeating():
    print("------------------------------------------")
    print("                Seating                   ")
    print("------------------------------------------")
    print("    a b c d e f g h i j k l m n o p      type     price ")
    print("------------------------------------    ------   ------- ")


def buyTickets():
    n_tix = input("Number of seats to buy: ")
    seat_start = input("Starting seat (ex. 3d): ")
    print("f{n_tix} seats starting at {seat_start} are available for purchase.")
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    printReceipt()

def calculateCost(n_tix):
    cost = n_tix * 20
    mask_fee = n_tix * 5
    sub_total = cost + mask_fee
    tax = sub_total * 0.0725
    total = sub_total + tax

def printReceipt():
    print("------------------------------------")
    print("            Receipt                 ")
    print("------------------------------------")
    print("Name:   {name}")
    print("Email: {email}")
    print("Number of tickets: {n_tix}")
  #  print("Seats: {seat_start}")
    print("Ticket Cost: {calculateCost.cost}")
    print("Mask fee: {calculateCost.mask_fee} ")
    print("Subtotal: {calculateCost.sub_total}")
    print("Tax: {calculateCost.tax}")
    print("--------------------------------------")
    print("Total  {calculateCost.total}")



# create some available seating
"""""
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

"""