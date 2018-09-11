import steembase
import steem
from pick import pick

# connect to testnet
# steembase.chains.known_chains['STEEM'] = {
#     'chain_id': '79276aea5d4877d9a25892eaa01b0adf019d3e5cb12a97478df3298ccdd01673',
#     'prefix': 'STX', 'steem_symbol': 'STEEM', 'sbd_symbol': 'SBD', 'vests_symbol': 'VESTS'
# }

#capture user information
username = input('Enter username: ') #demo account: cdemo
wif = input('Enter private ACTIVE key: ') #demo account: 5KaNM84WWSqzwKzY82fXPaUW43idbLnPqf5SfjGxLfw6eV2kAP3

#connect node and private active key
# client = steem.Steem(nodes=['https://testnet.steem.vc'], keys=[wif])

#connect to production server with active key
client = steem.Steem(keys=[wif])

#check valid user
userinfo = client.get_account(username)
if(userinfo is None) :
    print('Oops. Looks like user ' + username + ' doesn\'t exist on this chain!')
    exit()

#get account to authorise and check if valid
foreign_acc = input('Please enter the account name for POSTING authorisation: ')
if (foreign_acc == username) :
    print('Cannot allow or disallow posting permission to your own account')
    exit()
foreign_userinfo = client.get_account(foreign_acc)
if(foreign_userinfo is None) :
    print('Oops. Looks like user ' + foreign_acc + ' doesn\'t exist on this chain!')
    exit()

#check if foreign_account already has posting auth
_data = []
title = ''
for i in range(len(userinfo['posting']['account_auths'])) :
    _data.append(userinfo['posting']['account_auths'][i])
    if (_data[i][0] == foreign_acc) :
        title = (foreign_acc + ' already has posting permission. Please choose option from below list')
        options = ['DISALLOW', 'CANCEL']

if (title == '') :
    title = (foreign_acc + ' does not yet posting permission. Please choose option from below list')
    options = ['ALLOW', 'CANCEL']

#choice of action
# options = ['ALLOW', 'DISALLOW', 'CANCEL']
# get index and selected permission choice
option, index = pick(options, title)

if (option == 'CANCEL') :
    print('operation cancelled')
    exit()

if (option == 'ALLOW') :
    #allow(foreign, weight=None, permission='posting', account=None, threshold=None)
    client.allow(foreign=foreign_acc, weight=1, permission='posting', account=username, threshold=1)
    print(foreign_acc + ' has been granted posting permission')
else :
    #disallow(foreign, permission='posting', account=None, threshold=None)
    client.disallow(foreign=foreign_acc, permission='posting', account=username, threshold=1)
    print('posting permission for ' + foreign_acc + ' has been removed')