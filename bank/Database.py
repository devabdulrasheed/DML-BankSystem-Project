import os
tblAccounts = []
tblAccountsTransactionHistory = []
tblUserLogins = [{'username': 'admin', 'password': 'admin', 'privilege': 'admin', 'acno': '0000000000'}]


def accounts():
    return tblAccounts


def transactions():
    return tblAccountsTransactionHistory


def users():
    return tblUserLogins


def set_users(username, password, privilege,acno):
    tblUserLogins.append({'username': username, 'password': password, 'privilege': privilege, 'acno': acno})


def set_transactions(acno:int,transaction:{}):
    isfound = False
    for tran in tblAccountsTransactionHistory:
        if tran['acno'] == acno:
            tran['transactions'].append(transaction)
            isfound = True
    if  isfound == False:
        tblAccountsTransactionHistory.append({'acno':acno,'transactions':[transaction]})


def check_balance(acno:int, amount:float):
    for ac in tblAccounts:
        if ac['acno'] == acno:
            if ac['balance'] < amount:
                os.system('cls')
                print('*'*40)
                print('Insufficient balance')
                print('*' * 40)
                return 0
            else:
                return 1


def update_balacne(acno:int, balance:float):
    index = 0
    for ac in tblAccounts:
        if ac['acno'] == acno:
            print(tblAccounts[index])
            tblAccounts[index]['balance'] = balance
            print(tblAccounts[index])
            return 1
        index += 1
    return 0


def set_accounts(acno: int, name: str, type: str, balance: float, email: str):
    tblAccounts.append({'acno': acno, 'full_name': name, 'type': type,'balance': balance, 'email': email})