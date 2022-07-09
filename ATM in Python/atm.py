import getpass
import pyttsx3
#-----Global-Variables-Are-Defined-Here----
minBalance = 11000
globals()["balance"] = minBalance
#-----END--OF--Variables--Area--------

#------Functions are defined here-------

# Defining exit function
def exit():
    print("Thank you for using aBank ATM\n")
    quit()

# Defining New Account Function 
def newAccount():
    print("Welcome to create account portal\n")
    print("\nEnter your name: ")
    name = str(input())
    globals()["name"] = name

    print("\nEnter your Email-ID")
    
    email = str(input())
    globals()["email"] = email
    
    phoneNumber = str("\0")

    while len(phoneNumber)!=10:
        print("\nEnter your phone number: ")
        phoneNumber = str(input())

        if(len(phoneNumber) != 10):
            print("Phone Number format is invalid, Retry\n")

    pin = 0
    repin = 1
    counter = 0

    while pin != repin:
        print("\nCreate your pin: ")
        pin = getpass.getpass("Pin: ")

        print("Re-Enter the pin: ")
        repin = getpass.getpass("Re-Pin: ")

        counter+=1
        if(pin != repin):
            print("\nThe pin entered does not match. ")
            print("You have {} chances left\n".format(3-counter))
            if(counter==3):
                exit()
    print("\nYour pin is successfully created\n")
    globals()["repin"] = repin

    print("Congratulations, Your account has been successfully created.")
    print("Do you want to login: Yes(Y), No(N)")
    afterNew = str(input())

    if (afterNew == "Y" or afterNew == "y"):
        login(email, pin, name)
    elif (afterNew == "N" or afterNew == "n"):
        exit()

# Defining CheckBalance function 
def CheckBalance():
    print("Your balance is: ₹{}\n".format(balance))
    LoginOptions()

# Defining Deposit Money 
def DepositMoney(balance):
    print("Enter the amount you want to deposit: ")
    depositAmount = int(input())
    print("Do you want to deposit ₹{}: Yes(Y), No(N)".format(depositAmount))
    depositResponse = None

    while depositResponse != "Y":
        depositResponse = str(input())
        if depositResponse == "Y" or depositResponse == "y":
            globals()["balance"] = balance + depositAmount
            print("\n")
            CheckBalance()
            LoginOptions()
        elif depositResponse == "N" or depositResponse == "n":
            LoginOptions()


# Definign Withdraw Money Function 
def WithdrawMoney(balance):
    print("Enter the amount you want to withdraw: ")
    withdrawAmount = float(input())

    print("Do you want to withdraw ₹{}. Yes(Y), No(N)".format(withdrawAmount))
    withdrawResponse = input()

    if withdrawAmount > balance :
        print("The amount you entered is greater than available balance\n")
        login()

    if withdrawResponse == "Y" or withdrawResponse == "y":
        globals()["balance"] = balance - withdrawAmount
        CheckBalance()
        LoginOptions() 
    
    else:
        login()


# Defining Change Email Function 
def ChangeEmail(email):
    changeEmail = "\0" 
    pinInput = "\0"
    counter = 0
        
    while counter < 3:
        while changeEmail != email and  pinInput != repin:
            print("Enter your Email-ID: ")
            changeEmail = input()

            print("Enter your PIN: ")
            pinInput = getpass.getpass("PIN: ")

            counter+=1
            if changeEmail != email and  pinInput != repin:
                print("The Email-ID you entered does not match.\n")
                print("\nYou have {} chances remaining\n".format(3-counter))

        if changeEmail == email:
            print("Enter your new Email-ID: ")
            newEmail = str(input())
            print("Press \"Y\" to confirm, \"N\" to decline ")
            newEmailResponse = str(input())
            if newEmailResponse == "Y" or "y":
                globals()["email"] = newEmail
                print("Your email is successfully changed !!\n")
                LoginOptions()
            else:
                LoginOptions()
        exit()
      

# Defining Change Pin Function 
def ChangePin(repin):
    print("Enter the current PIN\n")
    pinConfirm = getpass.getpass("PIN: ")
    counterRepin = 0
    while counterRepin < 3:
        if pinConfirm == repin:
            print("Enter your new PIN\n")
            newPin = getpass.getpass("New PIN: ")
            print("PIN successfully changed !!")
            LoginOptions()
        else:
            counterRepin = counterRepin+1
            print("The Entered PIN does not match")
            print("You have {} chance(s) remaining").format(3-counter)

# Defining Login Function 
def login(email, pin, name):
    print("\naBank Welcomes you to login portal.")
    
    print("Enter your Email-ID: ")
    emailInput = str(input())

    print("Enter your pin: ")
    pinInput = getpass.getpass("PIN: ")

    if emailInput == email and pinInput == pin:
        print("\nWelcome, {} \n".format(name))
    else:
        invalidInput()
        exit()

    LoginOptions()
    
    

# Defining Invalid Input Function 
def invalidInput():
    print("The response you entered is invalid\n")

# Defining Login Option function 
def LoginOptions():
    print("Select an option: ")
    print("\t1. Check Balance\n\t2. Deposit Money\n\t3. Withdraw Money\n\t4. Change Email-ID\n\t5. Change PIN\n\t6. Log-Out")

    loginResponse = int(input("Enter your response here: "))

    if loginResponse == 1:
        CheckBalance()
    elif loginResponse == 2:
        DepositMoney(balance)
    elif loginResponse == 3:
        WithdrawMoney(balance)
    elif loginResponse == 4:
        ChangeEmail(email)
    elif loginResponse == 5:
        ChangePin(repin)
    elif loginResponse == 6:
        Main()
    else:
        invalidInput()

#---------END--OF--Function--Area--------

def Main():

    print("\nWelcome to aBank ATM\n")
    print("How may I help you")
    print("  1. Create a new account\n  2. Login\n  3. Exit\n")
    pilotInput = int(input("Enter your response here: "))

    if pilotInput == 1:
        newAccount()
    elif pilotInput == 2:
        login(email, repin, name)
    elif pilotInput == 3:
        exit()
    else:
        invalidInput()

Main()
