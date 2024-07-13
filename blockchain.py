import hashlib
import json
from time import time


# The class Blockchain is a subclass that's inheriting attributes/methods from the class object.
class Blockchain(object):
    def _init_(self): # init is a special method as indicated by the double underscore. Self is referencing the current class in order to access its variables and methods.
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # Creates a new block and adds it to the chain 
        pass

    def new_transactions(self):
        # Adds a new transaction to the list of transactions
        pass

    @staticmethod
    def hash(block):
        # Hashes a Block
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass
    
    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1