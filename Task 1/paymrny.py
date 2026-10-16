balance = 5000
amount = int(input("Enter the amount to pay: "))

if amount > 0:
    if amount > balance:
        print("Insufficient Balance")
    else:
        balance = balance - amount
        print("Payment Successfull")

        if balance == 0:
            print("Account  Khali Ho Gaya Hain")
        else:
            print("Remaining Balance:", balance)
else:
    print("Invalid Amount")