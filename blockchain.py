import functools
import hashlib as hash
from collections import OrderedDict

from hash_util import hash_string_256, hash_block

# Initializing our blockchain list
MINING_REWARD = 10 # Constant value.  Reward for person who mined a new block.
genesis_block = {
        'previous_hash':'',
        'index': 0,
        'transactions': [],
        'proof': 100
        }
blockchain = [genesis_block]
open_transactions = []
owner = 'Oscar'
particpants = {'Oscar'}

def load_data():
    with open('blockchain.txt', mode='r') as f:
        file_content = f.readlines()
        global blockchain
        global open_transactions
        blockchain = file_content[0]
        open_transactions = file_content[1]

load_data()

def save_data():
    with open('blockchain.txt', mode='w') as f:
        f.write(str(blockchain))
        f.write('\n')
        f.write(str(open_transactions))

def valid_proof(transactions, last_hash, proof):
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    guess_hash = hash_string_256(guess)
    print(guess_hash)
    return guess_hash[0:2] == '00'

def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof
    
def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender']== participant]
    tx_sender.append(open_tx_sender)
    amount_sent = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
    
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain] 

    amount_received = functools.reduce(lambda tx_sum, tx_amt: tx_sum + tx_amt[0] if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)       

    return amount_received - amount_sent
    
def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']
    
def add_transaction(recipient, sender = owner,  amount=1.0):
    """ Append a new value as well as the last blockchain to the blockchain 
    
    Arguments:
        :sender: The sender of the coins
        :recipient: The recipient of the coins
        :amount: The amount of coins sent with the transaction (default = 12.0)
    """
    # transaction = {
    #     'sender':sender, 
    #     'recipient': recipient, 
    #     'amount': amount
    #     }
    transaction = OrderedDict([('sender', sender),('recipient', recipient), ('amount', amount)])

    if verify_transaction(transaction):
        open_transactions.append(transaction)
        particpants.add(sender)
        particpants.add(recipient)
        save_data()
        return True
    return False

def mine_block():
    """ Create a new block and add open transactions to it."""
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    # Proof of work
    proof = proof_of_work()

    # Miners should be rewarded. Create a reward transaction
    # reward_transaction = {
    #     'sender': 'MINING',
    #     'recipient': owner,
    #     'amount': MINING_REWARD
        #}

    reward_transaction = OrderedDict(
        [('sender', 'MINING'), ('recipient', owner), ('amount', MINING_REWARD)])
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        'previous_hash':hashed_block,
        'index': len(blockchain),
        'transactions':copied_transactions,
        'proof': proof
        }
    blockchain.append(block)
    save_data()
    return True


def get_transaction_value():
    """ Returns the input of a user (a new transaction amount) 
        as a float.) """
    tx_recipient = input('Enter the recipient of the transaction:')
    tx_amount =  float(input('Your transaction amount please: '))
    return (tx_recipient, tx_amount) # tuple

def get_user_choice():
    """ Prompts the user for their choice and returns it."""
    user_input = input('Your choice: ')
    return user_input

def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)

def verify_chain():
    """ Verify the current blockchain and return True if it's valid, False otherwise"""
    # compare the stored has with a recalculated has of a previous block
    for (index, block) in enumerate(blockchain):
        if index == 0: # if genesis block, move to next block
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
        if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
            return False
    return True

def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])


# initialize bool variable for while loop
waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output participants')
    print('5: Check transaction validity')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data # unpack the tuple data into variables
        if add_transaction(recipient, amount=amount):
            print('Added transactions')
        else:
            print('Transaction failed')
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []    
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(particpants)
    elif user_choice == '5':
        if verify_transactions():
            print('All transactions are valid')
        else:
            print('There are invalid transactions')
    elif user_choice =="h":
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash':'',
                'index': 0,
                'transactions': [{'sender': 'Chris', 'recipeint':'Max', 'amount': 100.0}]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        break
    print('Balance of {}: {:6.2f}'.format('Max', get_balance('Oscar')))
    #get_balance('Oscar')
else: print('User left!')

print('Done!')