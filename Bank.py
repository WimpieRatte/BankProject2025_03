import random
import time

class Bank:
    """Bank class"""
    
    accounts = {}  # account_number : [ name, account_balance, account_type ] 
    
    def __init__(self, bank_name: str, name: str, account_balance: float, account_type: str):
        """Create the Bank object with a first account as default."""
        
        self.bank_name = bank_name
        self.name = name
        self.account_balance = account_balance
        self.account_type = account_type
        account_num = random.randrange(0, 999999999)
        self.accounts[account_num] = [name, account_balance, account_type]
        
    def create_account(self, name: str, initial_deposit: float, account_type: str):
        """add a new account"""
        account_num = random.randrange(0, 999999999)
        self.accounts[account_num] = [name, initial_deposit, account_type]
        
    def authenticate(self, name: str, account_number: int):
        """Checks if account number and name exists"""
        found_name = self.accounts.get(account_number, None)
        if found_name == name:
            return True
        else:
            return False
        
    def withdraw(self, account_number: int, withdraw_amount: float):
        """Withdraws the given amount and returns the resulting balance."""
        self.accounts[account_number][1] -= withdraw_amount
        return self.accounts[account_number][1]
    
    def deposit(self, account_number: int, deposit_amount: float):
        """Deposits the given amount and returns the resulting balance."""
        self.accounts[account_number][1] += deposit_amount
        return self.accounts[account_number][1]
    
    def check_balance(self, account_number: int):
        """Returns the current account balance for the given account number"""
        return self.accounts[account_number][1]
    
myBank = Bank("Volksbank", "Wimpie", 10000.00, "Savings")
while True:
    print("")
    print(f"Welcome to {myBank.bank_name}")
    print("")
    option = input("Would you like to login(l) or register(r)? ")
    if option == "l":
        print("    Login screen:")
        user = input("Please enter the name/owner of the account: ")
        acc_num = input("Please enter the account number: ")
        if myBank.authenticate(user, acc_num):
            while True:
                print("")
                print(f"Welcome, {user}.")
                print("1. Withdraw")
                print("2. Deposit")
                print("3. Check balance")
                print("4. Logout")
                l_option = input("Please choose an option:")
                if l_option == "1":
                    amt = float(input("Enter withdrawal amount: "))
                    myBank.withdraw(acc_num, amt)
                elif l_option == "2":
                    amt = float(input("Enter deposit amount: "))
                    myBank.deposit(acc_num, amt)
                elif l_option == "3":
                    print(f"Your current balance is: {myBank.check_balance(acc_num)}")
                elif l_option == "4":
                    break
                else:
                    print("Invalid option")
        else:
            print("Login failed...")
            time.sleep(3)  # let him soak in his mistake
            continue
    elif option == "r":
        print("    Account Registration:")
        name = input("Account name: ")
        init_dep = input("Initial Deposit: ")
        a_type = input("Account Type: ")
        myBank.create_account(name, init_dep, a_type)
        continue  # Take back to welcome screen
        
    else:
        print("Invalid option.")
        break