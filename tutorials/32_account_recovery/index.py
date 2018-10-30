import beembase
from beem.account import Account
from beem import Steem
from beemgraphenebase.account import PasswordKey
from beembase.objects import Permission

#capture user information
username = 'ndemo'#input('Enter username: ')
old_owner_key = '5HwBVJ4BwkMr8snV17Yx1MBJCsuPVd9pFMWg2unFcCH42MedwYL'#input('Enter recent owner key: ')
new_password = 'password'#input(Enter new password: ')

recovery_account = 'initminer'
recovery_account_key = '5JNHfZYKGaomSFvd4NUdQ9qMcEAC43kujbfjueTHpVapX1Kzq2n'

s = Steem(node=['https://testnet.steemitdev.com'], keys=[recovery_account_key])

new_owner_priv_key = PasswordKey(username, new_password, 'owner').get_private_key()
print('new owner private key: ' + str(new_owner_priv_key))
new_owner_pub_key = str(new_owner_priv_key.pubkey)
print('new owner public key: ' + new_owner_pub_key)

new_owner_auth = {
    "key_auths": [
        [new_owner_pub_key, 1]
    ],
    "account_auths": [],
    "weight_threshold": 1
}

request_op_data = {
    'recovery_account': recovery_account,
    'account_to_recover': username,
    'new_owner_authority': new_owner_auth,
    'extensions': []
}

request_op = beembase.operations.Request_account_recovery(**request_op_data)

input('press enter for request transmit')

request_result = s.finalizeOp(request_op, recovery_account, "active")

print('request result: ')
print(request_result)

input('press enter for recovery process')

s = Steem(node=['https://testnet.steem.vc'], keys=new_owner_priv_key)

new_priv = str(new_owner_priv_key)

new_owner_auth_priv = {
    "key_auths": [
        [new_priv, 1]
    ],
    "account_auths": [],
    "weight_threshold": 1
}

recent_owner_authority = {
    "key_auths": [
        [old_owner_key, 1]
    ],
    "account_auths": [],
    "weight_threshold": 1
}

op_data = {
    'account_to_recover': username,
    'new_owner_authority': new_owner_auth_priv,
    'recent_owner_authority': recent_owner_authority,
    'extensions': []
}

op = beembase.operations.Recover_account(**op_data)

input('press enter for recovery transmit')

result = s.finalizeOp(op, username, "owner")

print("Result:")
print(result)
