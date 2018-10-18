import steembase
import steem
from pick import pick
import random

# connect to testnet
steembase.chains.known_chains['STEEM'] = {
    'chain_id': '79276aea5d4877d9a25892eaa01b0adf019d3e5cb12a97478df3298ccdd01673',
    'prefix': 'STX', 'steem_symbol': 'STEEM', 'sbd_symbol': 'SBD', 'vests_symbol': 'VESTS'
}

#capture user information
username = input('Enter username: ') #demo account: demo01
wif = input('Enter private ACTIVE key: ') #demo account: 5HxTntgeoLm4trnTz94YBsY6MpAap1qRVXEKsU5n1v2du1gAgVH

#connect node and private active key
client = steem.Steem(nodes=['https://testnet.steem.vc'], keys=[wif])

#check for valid account and get account balance for STEEM and SBD
userinfo = client.get_account(username)
if(userinfo is None) :
    print('Oops. Looks like user ' + username + ' doesn\'t exist on this chain!')
    exit()
total_steem = userinfo['balance']
total_sbd = userinfo['sbd_balance']
savings_steem = userinfo['savings_balance']
savings_sbd = userinfo['savings_sbd_balance']

print('CURRENT ACCOUNT BALANCE:' + '\n' + total_steem + '\n' + total_sbd + '\n')
print('CURRENT SAVINGS BALANCE:' + '\n' + savings_steem + '\n' + savings_sbd + '\n')

input('Press enter to continue with the transfer' + '\n')


#choice of transfer/withdrawal
title1 = 'Please choose transfer type: '
options1 = ['Transfer', 'Withdrawal', 'Cancel']
#get index and selected transfer type
transfer_type, index = pick(options1, title1)

if transfer_type == 'Cancel':
    print('Transaction cancelled')
    exit()

#choice of currency
title2 = 'Please choose currency: '
options2 = ['STEEM', 'SBD']
# get index and selected currency
option, index = pick(options2, title2)

if option == 'STEEM':
    #get STEEM transfer amount
    amount = input('Enter amount of STEEM to transfer: ')
    asset = 'STEEM'
else:
    #get SBD transfer amount
    amount = input('Enter amount of SBD to transfer: ')
    asset = 'SBD'

if transfer_type == 'Transfer':
    #parameters: amount, asset, memo, to, account
    client.transfer_to_savings(float(amount), asset, '', username, username)
    print('\n' + 'Transfer to savings balance successful')
else:
    #create request ID random integer
    requestID = random.randint(1,1000000)
    #parameters: amount, asset, memo, request_id=None, to=None, account=None
    client.transfer_from_savings(float(amount), asset, '', requestID, username, username)
    print('\n' + 'Withdrawal from savings successful, transaction ID: ' + str(requestID))

#get remaining account balance for STEEM and SBD
userinfo = client.get_account(username)
total_steem = userinfo['balance']
total_sbd = userinfo['sbd_balance']
savings_steem = userinfo['savings_balance']
savings_sbd = userinfo['savings_sbd_balance']

print('\n' + 'REMAINING ACCOUNT BALANCE:' + '\n' + total_steem + '\n' + total_sbd + '\n')
print('CURRENT SAVINGS BALANCE:' + '\n' + savings_steem + '\n' + savings_sbd + '\n')