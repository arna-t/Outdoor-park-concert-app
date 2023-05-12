
"""
This code creates a 2d list (2d matrix) that can store seating.
The matrix is populated with . since all seats are available
"""
import json

n_row = 19
n_col = 26
mask_fee = 5
tax_rate = 0.0725

# create some available seating

def menu():
    print("---------------------------------------------------------")
    print("          Welcome to the Outdoor Park Concert App!       ")
    print("---------------------------------------------------------")
    print()
    print("[v] view seating")
    print("[b] buy tickets")
    print("[s] search for a customer name and display the tickets purchased")
    print("[d] display all the purchase made and total amount of income")
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
    print("-------------------------------------------------------------------------------------------------------")
    print("                                         Seating                                                       ")
    print("-------------------------------------------------------------------------------------------------------")
    print ("\t", end="")
    for i in range(0,26):
        print ("%s " % chr(ord('a')+i), end = " ")
    print(" type     price")
    print("-------------------------------------------------------------------------------------------------------")
   
 
# print available seating
    for r in range(n_row):
        print(r+1, end = "\t")
        for c in range(n_col):
            print(seating[r][c], end="  ") # 5 spaces in between columns
        if r in range(0,5):
            print ("front     $80 ")
        elif r in range (5,11):
            print("middle    $50")
        else:
            print("back      $25")
        print()             


def buyTickets(seating):
    n_tix = int(input("Number of seats to buy: "))
    seat_start = input("Starting seat (ex. 3d): ")
    user_r = int(seat_start[0:1])
    user_c = ord(seat_start[1:2])-ord('a')

    if user_r in range(0,5):
        seat_type = 'front'
        price = 80
    elif user_r in range (5,11):
        seat_type = 'middle'
        price = 50
    else:
        seat_type = 'back'
        price = 25

    print(f"{n_tix} seats starting at {seat_start} are available for purchase.")
    end_c = user_c + n_tix - 1
    for c in range (user_c, end_c+1):
        seating[user_r-1][c] = 'X'

    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    print("------------------------------------")
    print("            Receipt                 ")
    print("------------------------------------")
   # def calculateCost(n_tix):
    cost = n_tix * price
    mask_cost = n_tix * mask_fee
    sub_total = cost + mask_cost
    tax = float(sub_total) * tax_rate
    total = float(sub_total) + float(tax)
    print(f"Name               : {name}")
    print(f"Email              : {email}")
    print(f"Number of tickets  : {n_tix}")
    print(f"Seat type          : {seat_type}")
    print(f"Ticket Cost        : ${cost}")
    print(f"Mask fee           : ${mask_cost} ")
    print(f"Sub-total          : ${sub_total}")
    print(f"Tax                : ${round(tax, 2)}")
    print("------------------------------------")
    print(f"Total              : ${round(total, 2)}")
    
    #create a dictionary with customer data
    customer_info = {}
    customer_info['name'] = name
    customer_info['email'] = email        
    customer_info['number of tickets purchased'] = n_tix
    customer_info['seat type'] = seat_type
    customer_info['total'] = total
    
    #create a json file and dump dictionary content to the json file
    with open(r'/Users/arna.togayeva/Documents/GitHub/Outdoor-park-concert-app/cust_data.json', 'a') as outfile:
        json.dump(customer_info, outfile)

    print()
    ask = input("Do you want make a new purchase(y/n)? ")
    if ask == 'y':
            buyTickets(seating)
            
    else:
        menu()


def display_purchases(customer_info):
    print(customer_info)

seating = createSeating()
userQuit = False

while (not userQuit):

		#calling the menu function
    menu()
    userInput = input("Enter a command: ")
    lowerInput = userInput.lower()
    firstChar = lowerInput[0:1]

    if firstChar == 'v':
     # call function printSeating()
        printSeating(seating)
    
    elif firstChar == 'b':
        buyTickets(seating)
    elif firstChar == 'd':
        display_purchases
    elif firstChar == 'q':
        userQuit = True
    else:
        print("ERROR: " + firstChar + " is not a valid command")

print("\n")
print("Thank you for using the Outdoor Park Concert App!")
print("\n")
     