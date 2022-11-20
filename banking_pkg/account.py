def show_balance(balance):
    # assume that balance is passed from parameter balance and will be a float value
    print("Current Balance:", float(balance))
   


def deposit(balance):
    # takes in input for deposit amount
    amount = input("Enter amount to deposit : $ ")
    return float(balance) + float(amount)


def withdraw(balance): #takes input for withdraw amount
    amount = input("Enter the amount to withdraw: $")
    return float(balance) - float(amount)


def logout(name): #says goodbye and logs out
    print("Goodbye " + name)
