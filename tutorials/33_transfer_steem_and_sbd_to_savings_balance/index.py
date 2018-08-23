import steembase
import steem
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

#get account balance for STEEM and SBD
userinfo = client.get_account(username)
total_steem = userinfo['balance']
total_sbd = userinfo['sbd_balance']

print('CURRENT ACCOUNT BALANCE:' + '\n' + total_steem + '\n' + total_sbd + '\n')

input('Press enter to continue with the transfer' + '\n')


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

#parameters: amount, asset, memo, to, account
client.transfer_to_savings(float(amount), asset, '', username, username)

print('\n' + 'Transfer to savings balance successful')

#get remaining account balance for STEEM and SBD
userinfo = client.get_account(username)
total_steem = userinfo['balance']
total_sbd = userinfo['sbd_balance']

print('\n' + 'REMAINING ACCOUNT BALANCE:' + '\n' + total_steem + '\n' + total_sbd + '\n')