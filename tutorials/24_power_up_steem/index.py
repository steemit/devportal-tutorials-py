import steembase
import steem
from steem.amount import Amount

# connect to testnet
steembase.chains.known_chains['STEEM'] = {
    'chain_id': '79276aea5d4877d9a25892eaa01b0adf019d3e5cb12a97478df3298ccdd01673',
    'prefix': 'STX', 'steem_symbol': 'STEEM', 'sbd_symbol': 'SBD', 'vests_symbol': 'VESTS'
}

#capture user information
username = input('Enter username: ') #demo account: cdemo
wif = input('Enter private ACTIVE key: ') #demo account: 5KaNM84WWSqzwKzY82fXPaUW43idbLnPqf5SfjGxLfw6eV2kAP3

#connect node and private active key
client = steem.Steem(nodes=['https://testnet.steem.vc'], keys=[wif])

#get account balance
userinfo = client.get_account(username)
balance = userinfo['balance']

print('Available STEEM balance: ' + balance + '\n')

#account to power up to
to_account = input('Please enter the ACCOUNT to where the STEEM will be transferred: ')
#check valid username
result = client.get_account(to_account)
if (not result) :
    print('Invalid username')
    exit()

#amount to power up
amount = float(input('Please enter the amount of STEEM to power up: '))

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

#get new account balance
userinfo = client.get_account(username)
balance = userinfo['balance']
print('New STEEM balance: ' + balance)