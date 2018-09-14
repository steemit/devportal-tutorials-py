import steembase
import steem
from pick import pick
from steembase.exceptions import RPCError, RPCErrorRecoverable

# connect to testnet
steembase.chains.known_chains['STEEM'] = {
    'chain_id': '79276aea5d4877d9a25892eaa01b0adf019d3e5cb12a97478df3298ccdd01673',
    'prefix': 'STX', 'steem_symbol': 'STEEM', 'sbd_symbol': 'SBD', 'vests_symbol': 'VESTS'
}

#capture user information
username = input('Please enter your username: ') #'cdemo'
postingkey = input('Please enter your private posting key: ') #'5JEZ1EiUjFKfsKP32b15Y7jybjvHQPhnvCYZ9BW62H1LDUnMvHz'

#connect node and private posting key, demo account being used: cdemo, posting key: 5JEZ1EiUjFKfsKP32b15Y7jybjvHQPhnvCYZ9BW62H1LDUnMvHz
s = steem.Steem(nodes=['https://testnet.steem.vc'], keys=[postingkey])

#capture variables
author = input('Author of post/comment that you wish to vote for: ')
permlink = input('Permlink of the post/comment you wish to vote for: ')

#check vote status
# noinspection PyInterpreter
print('checking vote status - getting current post votes')
result = s.get_active_votes(author, permlink)
print(len(result), ' votes retrieved')

if result:
	for vote in result :
		if vote['voter'] == username:
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
	identifier = ('@'+author+'/'+permlink)
	try:
		print('Sending vote. You may see \'ERROR:root:Downgrade-retry... \' below. This does not necessarily mean the vote failed. Just that the node you are connected to was expected to support appbase but does not. A different error, however, is a problem.')
		s.commit.vote(identifier, float(weight), username)
		print('\n'+'Vote sent.')
	except (RPCErrorRecoverable, RPCError) as err: #not printing the error, as we expect it to have been output by steem-python already.
		print('\n'+'Exception encountered. Unable to vote')

else:
	print('Voting has been cancelled')

exit()

