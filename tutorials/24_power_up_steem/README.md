# Power up STEEM

How to power up your STEEM to STEEM POWER using Python.

In this tutorial we will explain and show you how to power up your STEEM into STEEM POWER on the **Steem** blockchain using the `commit` class found within the [steem-python](https://github.com/steemit/steem-python) library.

## Intro

The Steem python library has a built-in function to transmit transactions to the blockchain. We are using the `transfer_to_vesting` method found within the `commit` class in the library. When you power up you convert your STEEM into STEEM POWER to increase your influence on Steemit. Before we do the conversion, we check the current balance of the account to check how much STEEM is available. This is not strictly necessary as the process will automatically abort with the corresponding error, but it does give some insight into the process as a whole. We use the `get_account` function to check for this. The `transfer_to_vesting` method has 3 parameters:

1.  _amount_ - The amount of STEEM to power up. This must be of the `float` data type
1.  _to_ - The account to where the STEEM will be powered up
1.  _account_ - The source user account for the transfer

## Steps

1.  [**App setup**](#setup) - Library install and import. Connection to testnet
1.  [**User information and steem node**](#userinfo) - Input user information and connection to Steem node
1.  [**Check balance**](#balance) - Check current vesting balance of user account
1.  [**Conversion amount**](#convert) - Input power up amount and check valid transfer
1.  [**Commit to blockchain**](#commit) - Commit transaction to blockchain

#### 1. App setup <a name="setup"></a>

In this tutorial we only use 1 package:

- `steem` - steem-python library and interaction with Blockchain

We import the libraries and connect to the `testnet`.

```python
import steembase
import steem

# connect to testnet
steembase.chains.known_chains['STEEM'] = {
    'chain_id': '79276aea5d4877d9a25892eaa01b0adf019d3e5cb12a97478df3298ccdd01673',
    'prefix': 'STX', 'steem_symbol': 'STEEM', 'sbd_symbol': 'SBD', 'vests_symbol': 'VESTS'
}
```

Because this tutorial alters the blockchain we connect to the testnet so we don't create spam on the production server.

#### 2. User information and steem node <a name="userinfo"></a>

We require the `private active key` of the user in order for the conversion to be committed to the blockchain. This is why we have to specify this alongside the `testnet` node. The values are supplied via the terminal/console before we initialise the steem class. There is a demo account available to use with this tutorial but any account that is set up on the testnet can be used.

```python
#capture user information
username = input('Enter username: ') #demo account: cdemo
wif = input('Enter private ACTIVE key: ') #demo account: 5KaNM84WWSqzwKzY82fXPaUW43idbLnPqf5SfjGxLfw6eV2kAP3

#connect node and private active key
client = steem.Steem(nodes=['https://testnet.steem.vc'], keys=[wif])
```

#### 3. Check balance <a name="balance"></a>

In order to give the user enough information to make the conversion we check the current balance of the account using the `get_account` function.

```python
#get account balance
userinfo = client.get_account(username)
balance = userinfo['balance']

print('Available STEEM balance: ' + balance + '\n')
```

The results of the query are displayed in the console/terminal.

#### 4. Conversion amount <a name="convert"></a>

Both the `amount` and the `to` parameters are assigned via input from the terminal/console. The amount has to be greater than zero and no more than the total available STEEM of the user. We also check the `to account` to make sure it's a valid account name.

```python
#account to power up to
to_account = input('Please enter the ACCOUNT to where the STEEM will be transferred: ')
#check valid username
result = client.get_account(to_account)
if (not result) :
    print('Invalid username')
    exit()

#amount to power up
amount = float(input('Please enter the amount of STEEM to power up: '))
```

#### 5. Commit to blockchain <a name="commit"></a>

Now that all the parameters have been assigned we can continue with the actual transmission to the blockchain. The output and commit is based on the validity of the amount that has been input.

```python
#parameters: amount, to, account
if (amount == 0) :
    print('\n' + 'No STEEM entered for powering up')
    exit()
else :
    if (amount > Amount(balance).amount) :
        print('\n' + 'Insufficient funds available')
        exit()
    else :
        client.transfer_to_vesting(amount, to_account, username)
        print('\n' + str(amount) + ' STEEM has been powered up successfully')
```

The result of the power up transfer is displayed on the console/terminal.

As an added check we also display the new STEEM balance of the user on the terminal/console

```python
#get new account balance
userinfo = client.get_account(username)
balance = userinfo['balance']
print('New STEEM balance: ' + balance)
```

We encourage users to play around with different values and data types to fully understand how this process works. You can also check the balances and transaction history on the [testnet portal](http://condenser.steem.vc/).

### To Run the tutorial

1.  [review dev requirements](https://github.com/steemit/devportal-tutorials-py/tree/master/tutorials/00_getting_started#dev-requirements)
1.  clone this repo
1.  `cd tutorials/24_power_up_steem`
1.  `pip install -r requirements.txt`
1.  `python index.py`
1.  After a few moments, you should see a prompt for input in terminal screen.