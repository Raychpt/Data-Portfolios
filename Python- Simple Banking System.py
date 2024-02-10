#Given this initial database, create a simple banking system

database = {
    'Rachel Anne Trinidad': {
        'pass_word': "5245",
        'full_name': "Rachel Anne Trinidad",
        'account_number': "0011",
        'balance': 10000.00
    },
    'Albert Jay Cruz': {
        'pass_word': "4321",
        'full_name': "Albert Jay Cruz",
        'account_number': "0022",
        'balance': 25000.00
    },
    'Ruth Ramirez': {
        'pass_word': "6782",
        'full_name': "Ruth Ramirez",
        'account_number': "0033",
        'age': 30,
        'balance': 50000.00
    }
}
# Defining the menu
def mainmenu ():
    print ("1. Login")
    print ("2. Register")        
    print ("3. Check Balance")
    print ("4. Deposit")
    print ("5. Withdraw")
    print ("6. Transfer Funds")
    print ("7. Logout")
    print ()
    
#Defining functions
def login (fullname,password):
    if fullname in database  and database[fullname]['pass_word'] == password:
        return True
        
def register (fullname,password,accntno, balance):
    if fullname in database:
        print ("Account already exists! Please try another fullname.")
    else:
        database [fullname] = {'pass_word': password, 'full_name': fullname, 'balance': 0}
        print ("Registration successful")
        
    
def deposit(login, amount):
    database[fullname]['balance'] += amount
    print(f"Deposited {amount} successfully. Current balance: {database[fullname]['balance']}")
    
def withdraw(login, amount):
    if amount > database[fullname]['balance']:
         print("Insufficient balance!")
    else:
        database[fullname]['balance'] -= amount
        print(f"Withdrawn {amount} successfully. Current balance: {database[fullname]['balance']}")

def transfer(fullname, to_account, trf_amount1):
    if trf_amount1 > database[fullname]['balance']:
        print("Insufficient balance for transfer!")
    else:
        database[fullname]['balance'] -= trf_amount1 
        print(f"Transferred {trf_amount1} successfully")
        print(f"Your current balance is: {database[fullname]['balance']}")
        
def logout(fullname):
    print("Logged out successfully!")


logged_in = None

while True:
    mainmenu ()
    userinput = input ("Enter your choice: ")
   
    # If user chose option 1 
    if userinput == "1":
        if logged_in:
            print("Already logged in!")
        else:
            fullname = input ("Input your fullname: ")
            password = input ("Input your password: ")
            if login (fullname,password):
                logged_in = fullname and password 
                print ("Login successful")
            else:
                print ("Invalid login details")
   
    # If user chose option 2            
    if userinput == "2":
            fullname = input ("Input your fullname: ")
            password = input ("Create your password: ")
            accntno = input ("Enter your account number: ")
            bal = 0
            register (fullname, password, accntno, bal)
         
    # If user chose option 3
    if userinput == "3":
        if logged_in:
            print("Balance:", database [fullname]['balance'])
        elif login (fullname,password):
            print("Balance:", database [fullname]['balance'])
        else:
            print("Please login first.")

    # If user chose option 4
    if userinput == "4":
        if login (fullname,password):
            amount = float(input("Enter amount to deposit: "))
            deposit (login, amount) 
        else:
            print("Please login first.")
            
    # If user chose option 5
    if userinput == "5":
        if login (fullname,password):
            amount = float(input("Enter amount to withdraw: "))
            withdraw (login, amount) 
        else:
            print("Please login first.")
            
    
    # If user chose option 6
    if userinput == "6":
        if login (fullname,password):
            to_account = input("Enter receiver's account number: ")
            trf_amount1 = float(input("Enter amount to transfer: "))
            transfer(fullname, to_account, trf_amount1)
        else:
            print("Please login first.")

    
    # If user chose option 7
    if userinput == "7":
        if login (fullname,password):
            logout (login)
            logged_in = None
        else:
            print("Invalid choice. Please try again.")
