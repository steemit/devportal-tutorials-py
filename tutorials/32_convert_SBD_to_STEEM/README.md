# Convert SBD to STEEM

How to convert your SBD to STEEM using Python.

In this tutorial we will explain and show you how to convert some or all of your available SBD balance into STEEM on the **Steem** blockchain using the `commit` class found within the [steem-python](https://github.com/steemit/steem-python) library.

## Intro

The Steem python library has a built-in function to transmit transactions to the blockchain. We are using the `convert` method found within the `commit` class in the library. Any conversion of SBD to STEEM will not show instantly on your STEEM balance as it takes a week to settle. Before we do the conversion, we check the current balance of the account to check how much SBD is available. This is not strictly necessary as the process will automatically abort with the corresponding error, but it does give some insight into the process as a whole. We use the `get_account` function to check for this. The `convert` method has 3 parameters:

1.  _amount_ - The amount of SBD that will be converted
1.  _account_ - The specified user account for the conversion
1.  _request-id_ - An identifier for tracking the conversion. This parameter is optional

## Steps

1.  [**App setup**](#setup) - Library install and import. Connection to testnet
1.  [**User information and steem node**](#userinfo) - Input user information and connection to Steem node
1.  [**Check balance**](#balance) - Check current STEEM and SBD balance of user account
1.  [**Conversion amount and commit**](#convert) - Input of SBD amount to convert and commit to blockchain

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
#get account balance for STEEM and SBD
userinfo = client.get_account(username)
total_steem = userinfo['balance']
total_sbd = userinfo['sbd_balance']

print('CURRENT ACCOUNT BALANCE:' + '\n' + total_steem + '\n' + total_sbd + '\n')
```

The result of the query is displayed in the console/terminal.

#### 4. Conversion amount and commit <a name="convert"></a>

The final step before we can commit the transaction to the blockchain is to assign the `amount` parameter. We do this via a simple input from the terminal/console.

```python
#get recipient name
convert_amount = input('Enter the amount of SBD to convert to STEEM: ')
```

This value must be greater than zero in order for the transaction to execute without any errors. Now that we have all the parameters we can do the actual transmission of the transaction to the blockchain.

```python
#parameters: amount, account, request_id
client.convert(float(convert_amount), username)

print('\n' + convert_amount + ' SBD has been converted to STEEM')
```

If no errors are encountered a simple confirmation is printed on the UI.

As an added confirmation we check the balance of the user again and display it on the UI. This is not required at all but it serves as a more definitive confirmation that the conversion has been completed correctly.

```python
#get remaining account balance for STEEM and SBD
userinfo = client.get_account(username)
total_steem = userinfo['balance']
total_sbd = userinfo['sbd_balance']

print('\n' + 'REMAINING ACCOUNT BALANCE:' + '\n' + total_steem + '\n' + total_sbd)
```

The STEEM balance will not yet have been updated as it takes a week to settle. The SBD will however show the new balance.

We encourage users to play around with different values and data types to fully understand how this process works. You can also check the balances and transaction history on the [testnet portal](http://condenser.steem.vc/).

### To Run the tutorial

1.  [review dev requirements](https://github.com/steemit/devportal-tutorials-py/tree/master/tutorials/00_getting_started#dev-requirements)
1.  clone this repo
1.  `cd tutorials/32_convert_SBD_to_STEEM`
1.  `pip install -r requirements.txt`
1.  `python index.py`
1.  After a few moments, you should see a prompt for input in terminal screen.