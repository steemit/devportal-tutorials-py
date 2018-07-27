import random
import string
import steembase
import steem

# connect to testnet
steembase.chains.known_chains['STEEM'] = {
    'chain_id': '79276aea5d4877d9a25892eaa01b0adf019d3e5cb12a97478df3298ccdd01673',
    'prefix': 'STX', 'steem_symbol': 'STEEM', 'sbd_symbol': 'SBD', 'vests_symbol': 'VESTS'
}

#capture variables
parentAuthor = input('Parent author: ')
parentPermlink = input('Parent permlink: ')
author = input('Username: ')
wif = input('Private posting key: ')
body = input('Comment Body: ')

#combining parent values to create reply identifier
reply_identifier = '/'.join([parentAuthor,parentPermlink])

#random generator to create post permlink
permlink = ''.join(random.choices(string.digits, k=10))

#connect node and private posting key
client = steem.Steem(nodes=['https://testnet.steem.vc'], keys=[wif])

#commit post to blockchain
client.commit.post(title='', body=body, author=author, permlink=permlink, reply_identifier=reply_identifier)

print("Comment created successfully")
print(permlink)