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
username = input('Enter username: ') #demo account: demo01
wif = input('Enter private ACTIVE key: ') #demo account: 5HxTntgeoLm4trnTz94YBsY6MpAap1qRVXEKsU5n1v2du1gAgVH

#connect node
client = steem.Steem(nodes=['https://testnet.steem.vc'], keys=[wif])

#get account reward balances
userinfo = client.get_account(username)

if(userinfo is None) :
    print('Oops. Looks like user ' + username + ' doesn\'t exist on this chain!')
    exit()

reward_steem = userinfo['reward_steem_balance']
reward_sbd = userinfo['reward_sbd_balance']
reward_sp = userinfo['reward_vesting_steem']
reward_vests = userinfo['reward_vesting_balance']

print('Reward Balances:' + '\n' + 
    'STEEM: ' + reward_steem + '\n' + 
    'SBD: ' + reward_sbd + '\n' + 
    'STEEM POWER: ' + reward_sp + '\n' +
    'VESTS: ' + reward_vests
    )

input('\n' + 'Press enter to continue to claim selection')

#choice of claim
title = 'Please choose claim type: '
options = ['ALL', 'SELECTED', 'CANCEL']
# get index and selected claim type
option, index = pick(options, title)

#commit claim based on selection
if option == 'ALL':
    if Amount(reward_steem).amount + Amount(reward_sbd).amount + Amount(reward_vests).amount == 0:
        print('\n' + 'No rewards to claim')
        exit()
    else:
        client.claim_reward_balance(reward_steem, reward_sbd, reward_vests, username)
        print('\n' + 'All reward balances have been claimed. New reward balances are:' + '\n')
else:
    if option == 'CANCEL':
        print('\n' + 'Operation cancelled')
        exit()
    else:
        claim_steem = input('\n' + 'Please enter the amount of STEEM to claim: ') + ' STEEM'
        claim_sbd = input('Please enter the amount of SBD to claim: ') + ' SBD'
        claim_vests = input('Please enter the amount of VESTS to claim: ') + ' VESTS'
        if Amount(claim_steem).amount + Amount(claim_sbd).amount + Amount(claim_vests).amount == 0:
            print('\n' + 'Zero values entered, no claim to submit')
            exit()
        else:
            if claim_steem > reward_steem or claim_sbd > reward_sbd or claim_vests > reward_vests:
                print('\n' + 'Requested claim value higher than available rewards')
                exit()
            else:
                client.claim_reward_balance(claim_steem, claim_sbd, claim_vests, username)
                print('\n' + 'Claim has been processed. New reward balances are:' + '\n')
        

#get updated account reward balances
input("Press enter for new account balances")

userinfo = client.get_account(username)

reward_steem = userinfo['reward_steem_balance']
reward_sbd = userinfo['reward_sbd_balance']
reward_sp = userinfo['reward_vesting_steem']
reward_vests = userinfo['reward_vesting_balance']

print('STEEM: ' + reward_steem + '\n' + 
    'SBD: ' + reward_sbd + '\n' + 
    'STEEM POWER: ' + reward_sp + '\n' +
    'VESTS: ' + reward_vests
    )