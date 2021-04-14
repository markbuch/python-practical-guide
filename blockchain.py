# Initializing our blockchain list
genesis_block = {
        'previous_hash':'',
        'index': 0,
        'tranactions': []
        }
blockchain = [genesis_block]
open_transactions = []
owner = 'Oscar'

def hash_block(block):
    return '-'.join([str(block[key]) for key in block])

def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def add_transaction(recipient, sender = owner,  amount=1.0):
    """ Append a new value as well as the last blockchain to the blockchain 
    
    Arguments:
        :sender: The sender of the coins
        :recipient: The recipient of the coins
        :amount: The amount of coins sent with the transaction (default = 12.0)
    """
    transaction = {
        'sender':sender, 
        'recipient': recipient, 
        'amount': amount
        }
    
    open_transactions.append(transaction)
    

def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    block = {
        'previous_hash':hashed_block,
        'index': len(blockchain),
        'tranactions':open_transactions
        }
    blockchain.append(block)


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
    return True


# initialize bool variable for while loop
waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data # unpack the tuple data into variables
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()    
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice =="h":
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash':'',
                'index': 0,
                'tranactions': [{'sender': 'Chris', 'recipeint':'Max', 'amount': 100.0}]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        break
else: print('User left!')

print('Done!')