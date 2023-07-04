from bank.Database import accounts, transactions, users, set_accounts, set_users,set_transactions
from bank.Utils import account_no
import os


class Account:

    def register(self):
        os.system('cls')
        print('*' * 40)
        print(f"New account registration")
        print('*' * 40)
        acno = account_no()
        name = str(input('Enter account holder full name : '))
        print('Account types : ')
        print('S : Savings')
        print('C : Current')
        type = str(input('Choose account type S/C'))
        if type.upper() != 'S' and type.upper() != 'C':
            return 'Wrong entry , try again'
        balance = float(input('Enter account balance : '))
        email = str(input('Enter account email address : '))
        contact = int(input('Enter account contact no : '))
        username = str(input('Enter account username : '))
        password = str(input('Enter account password : '))
        if len(accounts()) > 0 and len(users()) > 0:
            for account in accounts():
                if  account['email'] == email or account['contact'] == contact or account['acno'] == acno:
                    return 'Provided account details already exists'
            for user in users():
                if user['username'] == username:
                    return 'Provided username already exists'
        set_accounts(acno, name, type, balance, email)
        set_users(username, password, 'user', acno)
        transactionDetails = {'name':name, 'contact':contact, 'amount':balance, 'type':type, 'transaction':'Credit', 'self':'Yes' }
        set_transactions(acno,transactionDetails)
        print('Account Registered')
        os.system('cls')
        print('*'*40)
        print(f"Registered account number : {acno}")
        print('*'*40)
        return 1

    def balance(self):
        ac = Account.search(self)
        if ac == 0:
            print('Account not found, try again!')
            return 0
        for account in accounts():
            if account['acno']==self.acno:
                os.system('cls')
                print('*' * 40)
                print(f"Amount number : {account['acno']} | Amount balance : {account['balance']}")
                print('*' * 40)
                return 1
            print('Account not found, try again!')
            return 0
        print('Account not found, try again!')
        return 0

    def search(self):
        for account in accounts():
            if account['acno'] == self.acno:
                return account
        return 0

