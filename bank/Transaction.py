from bank.Database import accounts, transactions, users, set_accounts, set_users, set_transactions, update_balacne, check_balance
from bank.Account import Account
import os

class Transaction:
    def deposit(self):
        ac = Account.search(self)
        if ac == 0:
            print('Account not found, try again!')
            return 0
        if len(transactions()) > 0:
            for account_info in transactions():
                if account_info['acno'] == self.acno:
                    name = str(input("Enter depositor name : "))
                    contact = int(input("Enter depositor contact no : "))
                    amount = float(input("Enter deposit amount : "))
                    type = str(input("Enter deposit type Cash/Cheque : "))
                    depositor = str(input("Enter depositor is an owner Yes/No : "))
                    transactionDetails = {'name': name, 'contact': contact, 'amount': amount, 'type': type,
                                          'transaction': 'Credit', 'self': depositor}
                    set_transactions(self.acno, transactionDetails)
                    print('Amount deposited')
                    debit = 0
                    credit = 0
                    for account_balance in transactions():
                        if account_balance['acno'] == self.acno:
                            for transaction in account_balance['transactions']:
                                if transaction['transaction'] == 'Credit':
                                    credit += float(transaction['amount'])
                                elif transaction['transaction'] == 'Debit':
                                    debit += float(transaction['amount'])
                            balance = credit - debit
                            update_balacne(self.acno, balance)
                            os.system('cls')
                            print('*' * 40)
                            print(f'Amount balance : {balance}')
                            print('*' * 40)

                    return 1
        return 0

    def withdraw(self):
        ac = Account.search(self)
        if ac == 0:
            print('Account not found, try again!')
            return 0
        if len(transactions()) > 0:
            for account_info in transactions():
                if account_info['acno'] == self.acno:
                    name = str(input("Enter withdrawer name : "))
                    contact = int(input("Enter withdrawer contact no : "))
                    amount = float(input("Enter withdraw amount : "))
                    type = str(input("Enter deposit type Cash/Cheque : "))
                    depositor = str(input("Enter withdrawer is an owner Yes/No : "))
                    transactionDetails = {'name': name, 'contact': contact, 'amount': amount, 'type': type,
                                          'transaction': 'Debit', 'self': depositor}
                    isSufficient = check_balance(self.acno, amount);
                    if isSufficient == 1:
                        set_transactions(self.acno, transactionDetails)
                        print('Amount withdrawn')
                        debit = 0
                        credit = 0
                        for account_balance in transactions():
                            if account_balance['acno'] == self.acno:
                                for transaction in account_balance['transactions']:
                                    if transaction['transaction'] == 'Credit':
                                        credit += float(transaction['amount'])
                                    elif transaction['transaction'] == 'Debit':
                                        debit += float(transaction['amount'])
                                balance = credit - debit
                                update_balacne(self.acno,balance)
                                os.system('cls')
                                print('*' * 40)
                                print(f'Amount balance : {balance}')
                                print('*' * 40)
                        return 1
        return 0
