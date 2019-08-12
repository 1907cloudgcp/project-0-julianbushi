import logging
from fileio import io
from error import exceptions
import re

def getUserList():
    accounts = io.readAccountList()
    return accounts
    
def getUserAccount(user):
    try:
        account = io.readAccount(user)
        if account is not None:
            return account
        raise AccountNotFoundError  

    except:
        logging.error('AccountNotFoundError with name ' + user)

    return None
        
def loginUser(user, password):
    account = getUserAccount(user)
    if account is None:
        return 0
    elif account.get('password') == password:
        return 2
    else:
        return 1

def registerUser(user, password):
    io.addAccount(user, password)
    return

def getBalance(user):
    account = getUserAccount(user)
    return account.get('balance')

def transfer(user, amount, op):
    account = getUserAccount(user)
    logstr = ''
    if op == 1:
        nBalance = float(account.get('balance')) + float(amount)
        logstr = 'Deposit $' + str(amount) + '!' + user
    else:
        nBalance = float(account.get('balance')) - float(amount)
        if nBalance < 0:
            print('You do not have enough money to withdraw.')
            return
        logstr = 'Withdraw $' + str(amount) + '!' + user
    b = {'balance' : str(nBalance)}
    account.update(b)
    io.updateAccount(account)

    logging.info(logstr)
    print('\nNew balance: $' + str(nBalance) + '\n')
    return

def getHistory(user):
    history = []
    regstring = ".*(?:Withdraw|Deposit)\s\$.*!(?:{})".format(user)
    try:
        for line in open('../../../resources/transactions.log', 'r'):
            history.append(re.search(regstring, line))
    except FileNotFoundError:
        logging.error('Transaction log not found!')
        return

    for entry in history:
        if entry is not None:
            print(entry.group().split('!')[0])

    return
    


