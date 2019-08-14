import logging
from fileio import io
from error import exceptions
import re

def getUserList():
    accounts = io.readAccountList()
    return accounts
    
def getUserAccount(user):
    accounts = getUserList()
    
    try:
        for account in accounts:
            if account.get('username') == user:
                return account
        raise AccountNotFoundError
    except:
        logging.error('AccountNotFoundError with name ' + user)

    return None

def checkUser(user):
    accounts = getUserList()
    
    for account in accounts:
        if account.get('username') == user:
            return True

    return False

def updateUser(account):
    accounts = getUserList()
    i = 0
    while i < len(accounts):
        if accounts[i].get('username') == account.get('username'):
            accounts[i] = account
            break
        i = i+1
    io.updateAccounts(accounts)
        
def loginUser(user, password):
    account = getUserAccount(user)
    if account is None:
        return 0
    elif account.get('password') == password:
        return 2
    else:
        return 1

def registerUser(user, password):
    accounts = getUserList()
    account = {'username':user, 'password':password, 'balance':'0.00'}
    accounts.append(account)
    io.updateAccounts(accounts)
    return

def removeUser(user):
    accounts = getUserList()
    for account in accounts:
        if account.get('username') == user:
            accounts.remove(account)
    io.updateAccounts(accounts)        
    return

def getBalance(user):
    account = getUserAccount(user)
    return account.get('balance')

def setBalance(user, amount):
    account = getUserAccount(user)
    b = {'balance' : '{:.2f}'.format(amount)}
    account.update(b)
    updateUser(account)

def transfer(user, amount, op):
    account = getUserAccount(user)
    amount = '{:.2f}'.format(amount)
    logstr = ''
    if op == 1:
        try:
            if float(amount) < 0:
                raise TransferError
        except:
            print('Exception: value out of range')
            return
        nBalance = float(account.get('balance')) + float(amount)
        logstr = 'Deposit $' + amount + '!' + user
    else:
        try:
            nBalance = float(account.get('balance')) - float(amount)
            if nBalance < 0:
                raise TransferError
            logstr = 'Withdraw $' + amount + '!' + user
        except:
            logging.error(user + ': withdrawl not possible')
            print('You do not have enough money to withdraw.')
            return
    b = {'balance' : '{:.2f}'.format(nBalance)}
    account.update(b)
    updateUser(account)
    logging.info(logstr)
    print('\nTransaction successful.\nNew balance: $' + '{:.2f}'.format(nBalance) + '\n')
    return



def getHistory(user):
    history = []
    regstring = ".*(?:Withdraw|Deposit)\s\$.*!(?:{})".format(user)

    historyFile = io.readHistory()
    
    for line in historyFile:
        history.append(re.search(regstring, line))

    transactions = []
    for entry in history:
        if entry is not None:
            transactions.append(entry.group().split('!')[0])

    return transactions

def printHistory(user):
    transactions = getHistory(user)
    for entry in transactions:
        print(entry)
    


