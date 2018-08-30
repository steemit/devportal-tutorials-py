import steembase
import steem
from steem.amount import Amount
from pick import pick

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

#check valid user and get account balance
userinfo = client.get_account(username)
if(userinfo is None) :
    print('Oops. Looks like user ' + username + ' doesn\'t exist on this chain!')
    exit()
balance = userinfo['balance']

print('Available STEEM balance: ' + balance + '\n')

input('Press any key to continue')

#choice of account
title = 'Please choose an option for an account to transfer to: '
options = ['SELF', 'OTHER']
# get index and selected transfer type
option, index = pick(options, title)

if (option == 'OTHER') :
    #account to power up to
    to_account = input('Please enter the ACCOUNT to where the STEEM will be transferred: ')
    #check valid username
    result = client.get_account(to_account)
    if (not result) :
        print(to_account + ' doesn\'t exist on this chain!')
        exit()
else :
    print('\n' + 'Power up STEEM to own account' + '\n')
    to_account = username

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
        print('\n' + str(amount) + ' STEEM has been powered up successfully to ' + to_account)

#get new account balance
userinfo = client.get_account(username)
balance = userinfo['balance']
print('New STEEM balance: ' + balance)