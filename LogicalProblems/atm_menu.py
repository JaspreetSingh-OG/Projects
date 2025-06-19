#ATM Menu 
"""
1.Check Balance
2.Deposit Money
3.Withdraw Money
4.Exit
"""

balance=10000000000
def atm():
    global balance
    while True:
        print("====ATM Menu====")
        print("1.Check Balance")
        print("2.Deposit Money")
        print("3.Withdraw Money")
        print("4.Exit")
        choice=int(input("Enter your choice (1/2/3/4): "))
        if choice==1:
            print("Checking Balance.....")
            pin=int(input("Enter your 4-digit ATM pin: "))
            if pin!=None:
                print("Checking Balance...")
                print(f"Your current balance is ₹ {float(balance)}")
            else:
                print("Please enter your PIN correctly!")
        
        elif choice==2:
            amount=float(input("Enter amount to deposit: ₹"))
            balance+=amount
            print(f"Amonut Credited with amount ₹{round(amount,2)}, your current balance is now ₹{balance}")
        elif choice==3:
            withdraw=float(input("Enter amount to withdraw: ₹"))
            balance-=withdraw
            print(f"Amount debited with ₹{round(withdraw,2)}, available balance ₹{balance}")
        elif choice==4:
            print("Thank You for choosing our ATM")
            break
        else:
            print("Please enter the choice between 1 to 4")

atm()
        

    