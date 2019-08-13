class AccountNotFoundError(Exception):
    pass

class CheckError(Exception):
    pass

class TransferError(ValueError):
    pass

class InputError(ValueError):
    pass
