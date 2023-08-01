
def deposit():
    while True:
        amount = input("Enter amount to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("Amount should be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

deposit()