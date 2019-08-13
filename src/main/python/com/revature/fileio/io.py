import json

def readAccountList():
    try:
        with open('../../../resources/accounts.json', 'r') as accountsFile:
            accounts = json.load(accountsFile)
            return accounts
    except FileNotFoundError:
        print('Exception: Accounts File Not Found\n')
        return

def updateAccounts(accounts):
    try:
        with open('../../../resources/accounts.json', 'w') as accountsFile:
            json.dump(accounts, accountsFile)       
    except FileNotFoundError:
        print('Exception: Accounts File Not Found\n')
        return

def readHistory():
    try:
        with open('../../../resources/transactions.log', 'r') as file:
            history = file.readlines()
            file.close()
    except FileNotFoundError:
        logging.error('Transaction log not found!')
        return

    return history
