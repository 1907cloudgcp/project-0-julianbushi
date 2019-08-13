import unittest
import logging
import logging.config
import yaml
from controller import controller
from service import service
from fileio import io

#LOG_PATH = 'C:/Users/Julian/Documents/Rev/project-0-julianbushi/src/main/resources/transactions.log'

class BankTest(unittest.TestCase):

    def test_a_register(self):
        service.registerUser('testuser', 'test')
    
    def test_b_balance(self):
        self.assertEqual(service.getBalance('testuser'), '0.00')
        service.setBalance('testuser', 600.3)
        self.assertEqual(service.getBalance('testuser'), '600.30')

    def test_c_deposits(self):
        service.transfer('testuser', 515, 1)
        self.assertEqual(service.getBalance('testuser'), '1115.30')
        service.transfer('testuser', 082.33, 1)
        self.assertEqual(service.getBalance('testuser'), '1197.63')
        service.transfer('testuser', 253.9583, 1)
        self.assertEqual(service.getBalance('testuser'), '1451.59')

    def test_d_withdrawls(self):
        service.transfer('testuser', 90, 2)
        self.assertEqual(service.getBalance('testuser'), '1361.59')
        service.transfer('testuser', 34.2442, 2)
        self.assertEqual(service.getBalance('testuser'), '1327.35')
        service.transfer('testuser', 1900, 2)
        self.assertEqual(service.getBalance('testuser'), '1327.35')

    def test_f_transactionLog(self):
        history = service.getHistory('testuser')
        self.assertEqual(len(history), 5)
    
if __name__ == '__main__':
        
    try:
        with open('../../../resources/logging.yaml','r') as f:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
    except FileNotFoundError:
        logging.basicConfig(level=logging.DEBUG)
        print('Logging configuration not found')
        
    unittest.main()
