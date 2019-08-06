import json

def readAccounts():
    try:
        with open('../../../resources/accounts.json', 'r') as accountsFile:
            accounts = json.load(accountsFile)
            return accounts
    except FileNotFoundError:
        print('Exception: File Not Found\n')
        return

def addAccount(user, password):
    try:
        with open('../../../resources/accounts.json', 'r') as accountsFile:
            accounts = json.load(accountsFile)

        account = {'username':user, 'password':password, 'balance':0.00}
        accounts.append(account)
        with open('../../../resources/accounts.json', 'w') as accountsFile:
            json.dump(accounts, accountsFile)
            
    except FileNotFoundError:
        print('Exception: File Not Found\n')
        return



