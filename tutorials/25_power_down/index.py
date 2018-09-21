import steembase
import steem
from pick import pick
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

#get account balance for vesting shares
userinfo = client.get_account(username)
delegated_vests = userinfo['delegated_vesting_shares']
vesting_shares = userinfo['vesting_shares']
to_withdraw = float(userinfo['to_withdraw'])
withdrawn = float(userinfo['withdrawn'])

available_vests = (Amount(vesting_shares).amount - Amount(delegated_vests).amount - 
     ((to_withdraw - withdrawn)/1000000))

print('VESTS currently powering down: ' + str(to_withdraw/1000000) + ' VESTS' +
    '\n' + 'Available VESTS: ' + str(available_vests) + ' VESTS')

input('\n' + 'Press enter to continue' + '\n')

#choice of transfer
title = 'Please choose an option: '
options = ['Power down ALL', 'Power down PORTION', 'Cancel Transaction']
# get index and selected transfer type
option, index = pick(options, title)

#parameters: amount, account
if (option == 'Cancel Transaction') :
    print('transaction cancelled')
    exit()
else :
    if (option == 'Power down ALL') :
        if (available_vests == 0) :
            print('No change to withdraw amount')
        else :
            amount = to_withdraw/1000000 + available_vests
            client.withdraw_vesting(amount, username)
            print(str(amount) + ' VESTS now powering down')
    else :
        amount = float(input('Please enter the amount of VESTS you would like to power down: '))
        if (amount < (to_withdraw/1000000 + available_vests)) :
            client.withdraw_vesting(amount, username)
            print(str(amount) + ' VESTS now powering down')
        else :
            if (amount == to_withdraw/1000000) :
                print('No change to withdraw amount')
            else :
                print('insufficient funds available')