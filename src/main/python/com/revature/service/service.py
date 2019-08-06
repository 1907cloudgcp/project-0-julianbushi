from fileio import io


def getUserList():
    accounts = io.readAccounts()
    return accounts
    
def getUser(user):
    accounts = io.readAccounts()
    for account in accounts:
        if account.get('username') == user:
            return account

    return None

def loginUser(user, password):
    account = getUser(user)

    if account.get('password') == password:
        return 1
    else:
        return 2

def registerUser(user, password):
    io.addAccount(user, password)
    return


