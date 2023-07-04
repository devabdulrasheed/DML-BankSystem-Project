from bank.Account import Account
from bank.Authentication import Authentication
from bank.Transaction import Transaction
import os


class Main:
    def login(self):
        print('-' * 40)
        print('User account login : ')
        print('-' * 40)
        self.username = str(input('Enter username : '))
        self.password = str(input('Enter password : '))
        result = Authentication.login(self)
        if result == 0:
            self.run()
        return result

    def menu(self):
        self.option = Authentication.menus(self)
        self.open_dialog()

    def open_dialog(self):
        is_admin = lambda x : x == 'admin'
        if self.option == 1 and is_admin(self.user['privilege']):
            RegisterStatus = Account.register(self)
            if RegisterStatus == 1:
                self.menu()
            else:
                print(RegisterStatus)
                self.menu()
        elif self.option == 2 and is_admin(self.user['privilege']):
            os.system('cls')
            print('*' * 40)
            print(f"Cash deposit")
            print('*' * 40)
            self.acno = int(input("Enter 10 digit account number : "))
            DepositStatus = Transaction.deposit(self)
            if DepositStatus == 1:
                self.menu()
            else:
                self.menu()
        elif self.option == 3 and is_admin(self.user['privilege']):
            os.system('cls')
            print('*' * 40)
            print(f"Cash withdraw")
            print('*' * 40)
            self.acno = int(input("Enter 10 digit account number : "))
            WithdrawStatus = Transaction.withdraw(self)
            if WithdrawStatus == 1:
                self.menu()
            else:
                self.menu()
        elif self.option == 4 and is_admin(self.user['privilege']):
            os.system('cls')
            print('*' * 40)
            print(f"Account Balance")
            print('*' * 40)
            self.acno = int(input("Enter 10 digit account number : "))
            BalanceStatus = Account.balance(self)
            if BalanceStatus == 1:
                self.menu()
            else:
                self.menu()
        elif self.option == 5 and is_admin(self.user['privilege']):
            os.system('cls')
            self.run()

    def run(self):
        os.system('cls')
        self.user = self.login()
        os.system('cls')
        self.menu()

    def __init__(self):
        self.acno = None
        self.option = None
        self.user = None
        self.username = None
        self.password = None
        self.run()


if __name__ == '__main__':
    Main()
