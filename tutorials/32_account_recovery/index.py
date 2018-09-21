import random
import string
import steembase
import steem
from steembase import operations
from steembase.transactions import SignedTransaction

# connect to testnet
steembase.chains.known_chains['STEEM'] = {
    'chain_id': '79276aea5d4877d9a25892eaa01b0adf019d3e5cb12a97478df3298ccdd01673',
    'prefix': 'STX', 'steem_symbol': 'STEEM', 'sbd_symbol': 'SBD', 'vests_symbol': 'VESTS'
}

#connect node and private posting key
client = steem.Steem(nodes=['https://testnet.steem.vc'], keys=['5JEZ1EiUjFKfsKP32b15Y7jybjvHQPhnvCYZ9BW62H1LDUnMvHz'])

client.operations.change_recovery_account(account_to_recover="cdemo", new_recovery_account="ddemo", extensions=[])
print(ops)
#tx = SignedTransaction(
#    ref_block_num=ref_block_num,
#    ref_block_prefix=ref_block_prefix,
#    expiration=expiration,
#    operations=ops)
#tx = tx.sign([wif], chain=self.steem.chain_params)

#capture variables
#author = input('Username: ')
#title = input('Post Title: ')
#body = input('Post Body: ')

