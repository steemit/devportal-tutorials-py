# Transfer STEEM and SBD to savings balance

How to transfer STEEM and SBD to savings using Python.

In this tutorial we will explain and show you how to check the STEEM and SBD balance of an account and also how to transfer a portion of that to a "savings" account on the **Steem** blockchain using the `commit` class found within the [steem-python](https://github.com/steemit/steem-python) library.

## Intro

The Steem python library has a built-in function to transmit transactions to the blockchain. We are using the `transfer_to_savings` method found within the `commit` class in the library. Before we do the transfer, we check the current balance of the account to ensure that there are sufficient funds available. This is not strictly necessary as the process will automatically abort with the corresponding error, but it does give some insight into the process as a whole. We use the `get_account` function to check for this. The `transfer_to_savings` method has 5 parameters:

1.  _amount_ - The amount of STEEM or SBD that the user wants to transfer. This parameter has to be of the `float` data type and is rounded up to 3 decimal spaces
1.  _asset_ - A string value specifying whether `STEEM` or `SBD` is being transferred
1.  _memo_ - An optional text field containing comments on the transfer
1.  _to_ - The recipient savings account name. Funds can be transferred to any other users' savings balance
1.  _account_ - The source account for the transfer

## Steps

1.  [**App setup**](#setup) - Library install and import. Connection to testnet
1.  [**User information and steem node**](#userinfo) - Input user information and connection to Steem node
1.  [**Check balance**](#balance) - Check current STEEM and SBD balance of user account
1.  [**Transfer type and amount**](#amount) - Input of transfer type and the amount to transfer
1.  [**Transfer commit**](#commit) - Commit of transfer to blockchain

#### 1. App setup <a name="setup"></a>

In this tutorial we use 2 packages:

- `steem` - steem-python library and interaction with Blockchain
- `pick` - helps select the query type interactively

We import the libraries and connect to the `testnet`.

```python
import steembase
import steem
from pick import pick

# connect to testnet
steembase.chains.known_chains['STEEM'] = {
    'chain_id': '79276aea5d4877d9a25892eaa01b0adf019d3e5cb12a97478df3298ccdd01673',
    'prefix': 'STX', 'steem_symbol': 'STEEM', 'sbd_symbol': 'SBD', 'vests_symbol': 'VESTS'
}
```

Because this tutorial alters the blockchain we connect to the testnet so we don't create spam on the production server.

#### 2. User information and steem node <a name="userinfo"></a>

We require the `private active key` of the user in order for the transfer to be committed to the blockchain. This is why we have to specify this alongside the `testnet` node. The values are supplied via the terminal/console before we initialise the steem class. There is a demo account available to use with this tutorial but any account that is set up on the testnet can be used.

```python
#capture user information
username = input('Enter username: ') #demo account: cdemo
wif = input('Enter private ACTIVE key: ') #demo account: 5KaNM84WWSqzwKzY82fXPaUW43idbLnPqf5SfjGxLfw6eV2kAP3

#connect node and private active key
client = steem.Steem(nodes=['https://testnet.steem.vc'], keys=[wif])
```

#### 3. Check balance <a name="balance"></a>

In order to give the user enough information to make the transfer we check the current balance of the account using the `get_account` function.

```python
#get account balance for STEEM and SBD
userinfo = client.get_account(username)
total_steem = userinfo['balance']
total_sbd = userinfo['sbd_balance']

print('CURRENT ACCOUNT BALANCE:' + '\n' + total_steem + '\n' + total_sbd + '\n')

input('Press enter to continue with the transfer' + '\n')
```

The result of the query is displayed in the console/terminal.

#### 4. Transfer type and amount <a name="amount"></a>

The user is given a choice on the type of transfer, or to cancel the process entirely. Once the user makes their choice we proceed to assign the `amount` as well as the `asset` parameter.

```python
#choice of transfer
title = 'Please choose transfer type: '
options = ['STEEM', 'SBD', 'Cancel Transfer']
# get index and selected transfer type
option, index = pick(options, title)

if option == 'Cancel Transfer':
    print('Transaction cancelled')
    exit()
else:
    if option == 'STEEM':
        #get STEEM transfer amount
        amount = input('Enter amount of STEEM to transfer to savings: ')
        asset = 'STEEM'
    else:
        #get SBD transfer amount
        amount = input('Enter amount of SBD to transfer to savings: ')
        asset = 'SBD'
```

#### 5. Transfer commit <a name="commit"></a>

Once all the parameters have been assigned we can proceed with the actual commit to the blockchain.

```python
#parameters: amount, asset, memo, to, account
client.transfer_to_savings(float(amount), asset, '', username, username)

print('\n' + 'Transfer to savings balance successful')
```

The `memo` parameter is optional and can be left empty as in the above example. We also use the source account for the `to` parameter. This can be replace by any other valid user account. A simple confirmation of the transfer is printed on the UI.

As an added confirmation we check the balance of the user again and display it on the UI. This is not required at all but it serves as a more definitive confirmation that the transfer has been completed correctly.

```python
#get remaining account balance for STEEM and SBD
userinfo = client.get_account(username)
total_steem = userinfo['balance']
total_sbd = userinfo['sbd_balance']

print('\n' + 'REMAINING ACCOUNT BALANCE:' + '\n' + total_steem + '\n' + total_sbd + '\n')
```

We encourage users to play around with different values and data types to fully understand how this process works. You can also check the balances and transaction history on the [testnet portal](http://condenser.steem.vc/).

### To Run the tutorial

1.  [review dev requirements](https://github.com/steemit/devportal-tutorials-py/tree/master/tutorials/00_getting_started#dev-requirements)
1.  clone this repo
1.  `cd tutorials/33_transfer_steem_and_sbd_to_savings_balance`
1.  `pip install -r requirements.txt`
1.  `python index.py`
1.  After a few moments, you should see a prompt for input in terminal screen.