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
author = input('Author to follow: ')

#check author status
result = s.get_account(author)

if result :
	#check current follow status of specified author
	follow = s.get_following(username, author, 'blog', 1)
	if len(follow) > 0 and follow[0]['following'] == author :
		title = "Author is already being followed, please choose action"
	else:
		title = "Author has not yet been followed, please choose action"
else:
	print('Author does not exist')
	exit()

#get index and selected action
options = ['Follow', 'Unfollow', 'Exit']
option, index = pick(options, title)

#parameters: author, what=['blog'], account=user)
if option == 'Follow' :
	s.commit.follow(author, ['blog'], username)
	print(author + ' is now being followed')
else:
	if option == 'Unfollow' :
		s.commit.unfollow(author, ['blog'], username)
		print(author + ' has now been unfollowed')
	else:
		print('Action Cancelled')