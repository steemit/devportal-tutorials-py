import steembase
import steem
from pick import pick

# connect to testnet
steembase.chains.known_chains['STEEM'] = {
    'chain_id': '79276aea5d4877d9a25892eaa01b0adf019d3e5cb12a97478df3298ccdd01673',
    'prefix': 'STX', 'steem_symbol': 'STEEM', 'sbd_symbol': 'SBD', 'vests_symbol': 'VESTS'
}

#capture user information
username = input('Please enter your username: ')
postingkey = input('Please enter your private posting key: ')

#connect node and private posting key, demo account being used: cdemo, posting key: 5JEZ1EiUjFKfsKP32b15Y7jybjvHQPhnvCYZ9BW62H1LDUnMvHz
s = steem.Steem(nodes=['https://testnet.steem.vc'], keys=[postingkey])

#capture variables
author = input('Author of post/comment that you wish to vote for: ')
permlink = input('Permlink of the post/comment you wish to vote for: ')

#check vote status
result = s.get_active_votes(author, permlink)

if result:
	x=0
	while x<(len(result)+1):
		if result[x]['voter'] == username:
			title = "This post/comment has already been voted for"
			break
		else:
			title = "No vote for this post/comment has been submitted"
else:
	title = "No vote for this post/comment has been submitted"

#option to continue
options = ['Add/Change vote', 'Cancel voting process']
option, index = pick(options, title)

#voting commit
if option == 'Add/Change vote':
	weight = input('\n'+'Please advise weight of vote between -100.0 and 100 (not zero): ')
	identifier = (author+'/'+permlink)
	s.commit.vote(identifier, float(weight), username)
else:
	print('Voting has been cancelled')
	exit()

print('\n'+'Vote has been submitted')