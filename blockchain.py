# Initializing our blockchain list
blockchain = []
open_transactions = []
owner = 'Oscar'

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
    pass # allows to define functions, and don't do anything when function is called

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
    #block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        if blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else: 
            is_valid = False
            break
    return is_valid


    # for block in blockchain:
    #     if block_index == 0:
    #         block_index += 1
    #         continue
    #     if block[0] == blockchain[block_index - 1]:
    #         is_valid = True
    #     else: 
    #         is_valid = False
    #         break
    #     block_index += 1
    # return is_valid

waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data # unpack the tuple data into variables
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice =="h":
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    if not verify_chain():
        print('Invalid blockchain!')
        break
else: print('User left!')

print('Done!')