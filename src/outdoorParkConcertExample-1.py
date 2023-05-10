"""
This example code creates a 2d list (2d matrix) that can store seating.
The matrix is populated with . since all seats are available
"""
n_row = 4
n_col = 10


# create some available seating

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


def createSeating():
    # available seat
    available_seat = '.'
    seating = []
    for r in range(n_row):
        row = []
        for c in range(n_col):
            row.append(available_seat)
        seating.append(row)
    return seating

def printSeating(seating):
    print("-----------------------------------------------------------")
    print("                        Seating                            ")
    print("-----------------------------------------------------------")
    #print("a b c d e f g h i j      type     price ")
   # print('        ', end='')
    print ("\t", end="")
    for i in range(0,10):
        print ("%s " % chr(ord('a')+i), end = "   ")
    print("")
   
 
# print available seating
    for r in range(n_row):
        print(r+1, end = "\t")
        for c in range(n_col):
            print(seating[r][c], end="    ")
        print()  


#def printReceipt(name, email):
   


def buyTickets(seating):
    n_tix = int(input("Number of seats to buy: "))
    seat_start = input("Starting seat (ex. 3d): ")
    user_r = int(seat_start[0:1])
    user_c = ord(seat_start[1:2])-ord('a')
   # seat_selected = int(input("Select seat: "))
   # user_r = int(input("Enter a row n: "))
   # user_c = input("Enter a column letter: ")
    #user_c1 = ord(user_c) - ord('a')
    #seat_selected = str(user_r) + user_c
    print(f"{n_tix} seats starting at {seat_start} are available for purchase.")
    #print(user_r)
    #print(user_c1)
    #seating[user_r-1][user_c1] ='X'
    end_c = user_c + n_tix - 1
    for c in range (user_c, end_c+1):
        seating[user_r-1][c] = 'X'

   # print(f"{n_tix} seats starting at {seat_selected} are available for purchase.")
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    print("------------------------------------")
    print("            Receipt                 ")
    print("------------------------------------")
   # def calculateCost(n_tix):
    cost = n_tix * 20
    mask_fee = n_tix * 5
    sub_total = cost + mask_fee
    tax = float(sub_total) * 0.0725
    total = float(sub_total) + float(tax)
    print(f"Name:  {name}")
    print(f"Email: {email}")
    print(f"Number of tickets: {n_tix}")
    #print("Seats: {seat_start}")
    print(f"Ticket Cost: ${cost}")
    print(f"Mask fee: ${mask_fee} ")
    print(f"Subtotal: ${sub_total}")
    print("Tax: $", round(tax, 2))
    print("--------------------------------------")
    print("Total: $", round(total, 2))
    menu()

seating = createSeating()
userQuit = False
seating[3][5] = 'G'

while (not userQuit):

		#calling the menu function
    menu()
    userInput = input("Enter a command: ")
    lowerInput = userInput.lower()
    firstChar = lowerInput[0:1]

    if firstChar == 'v':
     # call function printSeating()
        printSeating(seating)
     # our test matrix has 4 rows and 10 columns    

    elif firstChar == 'b':
        buyTickets(seating)
    elif firstChar == 'q':
        userQuit = True
    else:
        print("ERROR: " + firstChar + " is not a valid command")

print("\n")
print("Thank you for using the Outdoor Park Concert App!")
print("\n")
     