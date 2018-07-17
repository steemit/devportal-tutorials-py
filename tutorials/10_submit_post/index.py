import random
import string
import steembase
import steem

# connect to testnet
steembase.chains.known_chains['STEEM'] = {
    'chain_id': '79276aea5d4877d9a25892eaa01b0adf019d3e5cb12a97478df3298ccdd01673',
    'prefix': 'STX', 'steem_symbol': 'STEEM', 'sbd_symbol': 'SBD', 'vests_symbol': 'VESTS'
}

#connect node and private posting key
client = steem.Steem(nodes=['https://testnet.steem.vc'], keys=['5JEZ1EiUjFKfsKP32b15Y7jybjvHQPhnvCYZ9BW62H1LDUnMvHz'])

#capture variables
author = input('Username: ')
title = input('Post Title: ')
body = input('Post Body: ')

#capture list of tags and separate by " "
taglimit = 2 #number of tags 1 - 5
taglist = []
for i in range(1, taglimit+1):
	print(i)
	tag = input(' Tag : ')
	taglist.append(tag)
" ".join(taglist) #create string joined with empty spaces

#random generator to create post permlink
permlink = ''.join(random.choices(string.digits, k=10))

client.commit.post(title=title, body=body, author=author, tags=taglist, permlink=permlink)

print("Post created successfully")