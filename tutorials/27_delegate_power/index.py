import steembase
import steem
from pick import pick
import pprint
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

#connect to production server with active key
# client = steem.Steem(keys=[wif])

#check valid user
userinfo = client.get_account(username)
if(userinfo is None) :
    print('Oops. Looks like user ' + username + ' doesn\'t exist on this chain!')
    exit()

#display active delegations (refer to tutorial #29_get_delegations_by_user)
delegations = client.get_vesting_delegations(username, '', 100)
if len(delegations) == 0:
	print('No active delegations')
else:
	pprint.pprint(delegations)

#available VESTS
avail_vests = (Amount(userinfo['vesting_shares']).amount - 
    ((userinfo['to_withdraw']-userinfo['withdrawn'])/1000000)-
    Amount(userinfo['delegated_vesting_shares']).amount)
print('\n' + 'Available VESTS : ' + str(avail_vests))

input('Press enter to continue' + '\n')

#choice of action
title = ('Please choose action')
options = ['DELEGATE POWER', 'UN-DELEGATE POWER', 'CANCEL']
# get index and selected permission choice
option, index = pick(options, title)

if (option == 'CANCEL') :
    print('operation cancelled')
    exit()

#get account to authorise and check if valid
delegatee = input('Please enter the account name to ADD / REMOVE delegation: ')
delegatee_userinfo = client.get_account(delegatee)
if(delegatee_userinfo is None) :
    print('Oops. Looks like user ' + delegatee + ' doesn\'t exist on this chain!')
    exit()

# delegate_vesting_shares(to_account: str, vesting_shares: str, account=None)
if (option == 'DELEGATE POWER') :
    vesting_value = input('Please enter the amount of VESTS to delegate: ')
    vesting_shares = (str(vesting_value) + ' VESTS')
    client.delegate_vesting_shares(to_account=delegatee, vesting_shares=vesting_shares, account=username)
    print('\n' + str(vesting_shares) + ' have been successfully been delegated to ' + delegatee)
else :
    vesting_shares = '0 VESTS'
    client.delegate_vesting_shares(to_account=delegatee, vesting_shares=vesting_shares, account=username)
    print('Delegated VESTS have been successfully removed from ' + delegatee)