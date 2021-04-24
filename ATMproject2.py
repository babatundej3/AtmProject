#initialisation


import random

database = {}

def init():
    
    isValidOptionSelected = False
    print("Welcome to BTJ Bank of Africa")

    while isValidOptionSelected == False:
        
        haveAccount = int(input("Do you have an account with us: 1 (yes) 2 (No) \n"))

        if(haveAccount == 1):
            isValidOptionSelected = True
            login()
        
        elif(haveAccount == 2):
            isValidOptionSelected = True
            register()
        else:
            print("invalid selection")

def login ():

    print('***Login****')

    isLogisSuccessful = False

    while isLogisSuccessful == False:
        accountNumberFromUser = int(input("Enter Your Acount number \n"))
        Password = input("Enter Password \n")

        for  accountNumber,userDetails in database.items():
            if(accountNumber == accountNumberFromUser):
                if(userDetails[3] == Password):
                    isLogisSuccessful = True

        print('Account or Password not correct')
    bankOperation(userDetails)


def register():
    print("*****Register*****")
    email = input("Enter your email address \n")
    First_name = input ("Enter your first name \n")
    Last_name = input ("Enter your last name \n")
    Password = input ("Create a Password \n")
    
    accountNumber = generationAccountNumber()

    database[accountNumber] = [ First_name, Last_name, email, Password ]

    print("Your account number has been created successfully")
    print("Your account number is: %d" % accountNumber)
    print("Keep it safe")
    login()


def bankOperation(user):
    print("Welcome %s %s " % (user[0], user[1]))
    
    selectedOption = int(input("Available Services (1) Deposit (2) Withdrawal (3) Sign Out (4) Exit \n"))

    if(selectedOption == 1):
        DepositOperation()
    elif(selectedOption == 2):
        WithdrawalOperation()
    elif(selectedOption == 3):
        login()
    elif(selectedOption == 4):
        Exit()
    
    else:
        print("invalid selection, try again")
        bankOperation(user)

def WithdrawalOperation():
    print('withdrawal')

def DepositOperation():
    print("Deposit")

def SignOutOperation():
    print('Sign Out')

def ExitOperation():
    Print("Thank You")

def generationAccountNumber():

    return random.randrange(111111111,9999999999)

init()