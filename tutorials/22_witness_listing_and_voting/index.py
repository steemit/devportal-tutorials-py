import steembase
import steem
from pick import pick
import pprint

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

#print list of active witnesses
print('ACTIVE WITNESSES')
witness_list = client.get_active_witnesses()
pprint.pprint(witness_list)

#print list of currently voted for witnesses
print('\n' + 'WITNESSES CURRENTLY VOTED FOR')
vote_list = userinfo['witness_votes']
pprint.pprint(vote_list)

input('Press enter to continue')

#choice of action
title = ('Please choose action')
options = ['VOTE', 'UNVOTE', 'CANCEL']
# get index and selected permission choice
option, index = pick(options, title)

if (option == 'CANCEL') :
    print('\n' + 'operation cancelled')
    exit()

if (option == 'VOTE') :
    # vote process
    witness_vote = input('Please enter the witness name you wish to vote for: ')
    if witness_vote not in witness_list :
        print('\n' + witness_vote + ' does not appear on the available witness list')
        exit()
    if witness_vote in vote_list :
        print('\n' + witness_vote + ' cannot be voted for more than once')
        exit()
    client.approve_witness(witness=witness_vote, account=username, approve=True)
    print('\n' + witness_vote + ' has been successfully voted for')
else :
    # unvote process
    witness_unvote = input('Please enter the witness name you wish to remove the vote from: ')
    if witness_unvote not in vote_list :
        print('\n' + witness_unvote + ' is not in your voted for list')
        exit()
    client.disapprove_witness(witness=witness_unvote, account=username)
    print('\n' + witness_unvote + ' has been removed from your voted for list')