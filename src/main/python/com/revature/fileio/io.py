import json

def readAccountList():
    try:
        with open('../../../resources/accounts.json', 'r') as accountsFile:
            accounts = json.load(accountsFile)
            return accounts
    except FileNotFoundError:
        print('Exception: File Not Found\n')
        return
    
def readAccount(user):
    accounts = readAccountList()
    for account in accounts:
        if account.get('username') == user:
            return account
    return None

def addAccount(user, password):
    accounts = readAccountList()
    account = {'username':user, 'password':password, 'balance':0.00}
    accounts.append(account)

    try:
        with open('../../../resources/accounts.json', 'w') as accountsFile:
            json.dump(accounts, accountsFile)       
    except FileNotFoundError:
        print('Exception: File Not Found\n')
        return

def updateAccount(nAccount):
    accounts = readAccountList()
    i = 0
    while i < len(accounts):
        if accounts[i].get('username') == nAccount.get('username'):
            accounts[i] = nAccount
            break
        i = i+1

    try:
        with open('../../../resources/accounts.json', 'w') as accountsFile:
            json.dump(accounts, accountsFile)      
    except FileNotFoundError:
        print('Exception: File Not Found\n')
        return
