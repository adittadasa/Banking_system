# Simple Banking System Project
balance = 0
# Function for deposit money
def deposit():
    global balance 
    amt = float(input("Enter the amount to deposit :"))
    if amt > 0 :
        balance += amt 
        print(f"Taka {amt} is deposited succesfully ")
    else:
        print("Invalid Amount")

# Function for withdraw money
def withdraw():
    global balance
    amt = float(input("Emter the amount to withdraw :"))
    if  balance > amt:
        balance -= amt 
        print(f"Taka{amt} is withdraw succesfully")
    else:
        print("Not complete Transaction")

# Function to check current balance
def check_balance():
    print(f"Your current balance is Rs {balance}")

# Main program loop
while(True):
    print("______Banking System_____")
    print("1.DEPOSIT")
    print("2.WITHDRAW")
    print('3.BALENCE')
    print('EXIT')

    choice = int(input("Enter your Choice :"))
        # Calling functions based on choice

    if choice == 1 :
        deposit()
    elif choice == 2 :
        withdraw()
    elif choice == 3 :
        check_balance()
    elif choice == 4 :
        print("Thank you ")
    else:
        print("Invalid choise ")


