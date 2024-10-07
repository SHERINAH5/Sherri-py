balance = 0

print("Welcome to WITIAcademy Sacco")
print("\nplease choose an option:")
print("1. Deposit Money")
print("2. Withdraw Money")
print("3. Check Balance")

choice = input("Enter your choice (1/2/3): ")

if choice == '1':
    amount = float(input("Enter amount to deposit:"))
    if amount >= 1000:
        balance += amount
        print(f"successfully deposited {amount}. New balance is {balance}.")
    else: 
        print("minimum deposit amount is 1000.")

elif choice == '2':    
    amount = float(input("Enter amount to withdraw:")) 
    if amount >= 500:
        if balance >=amount:
            balance -= amount
            print(f"successfully withdrawn {amount}. New balance {balance}.")
        else:
            print("insufficient balance.")  
    else:
        print("minimum withdraw amount is 500.")
elif  choice == '3': #check balance
    print(f"your current balance is {balance}.")       

