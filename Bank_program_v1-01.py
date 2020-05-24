def withdraw_money(amount):
    global current_balance
    try:
        val_amount = int(amount)
        print(val_amount, "is a valid entry. Let's see if you have enought money.")
        if (int(current_balance) >= int(amount)):
            current_balance = int(int(current_balance) - int(amount))
            print("                             ")
            print("You have enough money, your new balance is", current_balance)
            print("                             ")
            menu(input("Do you want to withdraw money? (Yes/No) "))
            return current_balance
        else:
            print("                             ")
            print("Sorry you don't have enought money.")
            menu(input("Do you want to try to enter another amount of money? "))
            print("                             ")
    except ValueError:
        print("Sorry that is not a valid number. Please write a valid number.")
        print("                             ")
        menu(input("Do you want to withdraw money? (Yes/No) "))

def menu(Yes_No):
    print("                                 ")
    if Yes_No == "Yes":
        withdraw_money(input("How much money do you want to take out? "))
        print("                                 ")
    elif Yes_No == "yes":
        withdraw_money(input("How much money do you want to take out? "))
        print("                                 ")
    elif Yes_No == "No":
        want_to_deposit(input("Do you want to deposit some money? "))
        print("                                 ")
    elif Yes_No == "no":
        want_to_deposit(input("Do you want to deposit some money? "))
        print("                                 ")
    else:
        print("Sorry we did not understand if you said yes or no.")
        print("                                 ")
        menu(input("Do you want to withdraw money? (Yes/No) "))

def want_to_deposit(Yes_No_deposit):
    if Yes_No_deposit == "Yes":
        amount_deposit_money(input("How much do you want to deposit?"))
    elif Yes_No_deposit == "yes":
        amount_deposit_money(input("How much do you want to deposit?"))
    elif Yes_No_deposit == "No":
        print("Thank you for coming, see you again!")
        print("                                 ")
    elif Yes_No_deposit == "no":
        print("Thank you for coming, see you again!")
        print("                                 ")
    else:
        print("Sorry this is not a valid response")
        print("                                 ")
        menu(input("Do you want to withdraw money? (Yes/No) "))

def amount_deposit_money(deposit):
    global current_balance
    try:
        val_amount = int(deposit)
        print(val_amount, "is a valid entry.")
        current_balance = int(int(current_balance) + int(deposit))
        print("                             ")
        print("Your new balance is", current_balance)
        print("                             ")
        menu(input("Do you want to withdraw money? (Yes/No) "))
        return current_balance
    except ValueError:
        print("Sorry that is not a valid number. Please write a valid number.")
        print("                             ")
        menu(input("Do you want to withdraw money? (Yes/No) "))

#What is below is the beggining of the code, what is above are different parts that are used.
current_balance = int(1000)
print("                         ")
print("You currently have", current_balance, "$ in your account.")
print("                         ")

menu(input("Do you want to withdraw money? (Yes/No) "))