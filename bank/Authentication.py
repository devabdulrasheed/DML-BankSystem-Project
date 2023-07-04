from bank.Database import users


class Authentication:
    def login(self):
        for user in users():
            if user['username'] == self.username and user['password'] == self.password:
                return user
        print('Invalid username or password')
        return 0


    def menus(self):
        if self.user['privilege'] == 'admin':
            print('-' * 40)
            print('Bank Menu : ')
            print('-' * 40)
            print('1 - Account opening : ')
            print('2 - Cash deposit : ')
            print('3 - Cash withdrawal : ')
            print('4 - Account balance : ')
            print('5 - Logout : ')
            print('-' * 40)
            return int(input("Choose an option : "))
        else:
            print('-' * 40)
            print('Bank Menu : ')
            print('-' * 40)
            print('1 - Account statement : ')
            print('3 - Logout : ')
            print('-' * 40)
            return int(input("Choose an option : "))