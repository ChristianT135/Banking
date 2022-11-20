from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("          === Automated Teller Machine ===          ")

name = input("Enter name to Register ")
pin = input("Enter pin number ")
balance = 0

print (name + "has been registered with a starting balance of $" + str(balance))
print ()

print("          === Automated Teller Machine ===          ")
print ("LOGIN")
    
while True:

    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter pin number: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("LOGIN Successful")
        break
    else:
        print("Invalid Credentials!")
        
while True:
    atm_menu(name)
    option = input("Choose an Option! ")
    
    if option == "1":
        account.show_balance(balance)
    
    elif option == "2":
        balance += account.deposit(balance)
        account.show_balance(balance)
        
    elif option == "3":
        balance -= account.deposit(balance)
        account.show_balance(balance)
        
    elif option == "4":
        account.logout(name)
        break
    
    
    