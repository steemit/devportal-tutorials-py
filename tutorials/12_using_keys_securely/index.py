# initialize Steem class
from steem import Steem

# defining private keys inside source code is not secure way but possible
s = Steem(keys=['<private_posting_key>', '<private_active_key>'])

# above will allow accessing Commit methods such as
# demo account sending 0.001 STEEM to demo1 account

s.commit.transfer('demo','0.001','STEEM','memo text','demo1')

# if private keys are not defined
# accessing Wallet methods are also possible and secure way
s.wallet.get_active_key_for_account('demo')

