import steem
import steembase
from steembase.account import PasswordKey
from steembase.account import PrivateKey
from steembase import operations

account = input('Account: ')
old_password = input('Current password: ')
new_password = input('New password: ')

old_owner_key = str(
    PasswordKey(account, old_password, "owner").get_private_key()
)

client = steem.Steem(keys=[old_owner_key])

#client = steem.Steem(nodes=['https://testnet.steem.vc'], keys=[wif])

new_public_keys = {}

for role in ["owner", "active", "posting", "memo"]:
    private_key = PasswordKey(account, new_password, role).get_private_key()
    new_public_keys[role] = str(private_key.pubkey)

new_data = {
    "account": account,
    "json_metadata": {},
    "owner": {
        "key_auths": [
            [new_public_keys["owner"], 1]
        ],
        "account_auths": [],
        "weight_threshold": 1
    },
    "active": {
        "key_auths": [
            [new_public_keys["active"], 1]
        ],
        "account_auths": [],
        "weight_threshold": 1
    },
    "posting": {
        "key_auths": [
            [new_public_keys["posting"], 1]
        ],
        "account_auths": [],
        "weight_threshold": 1
    },
    "memo_key": new_public_keys["memo"]
}

print("New data:")
print(new_data)

op = operations.AccountUpdate(**new_data)

result = client.commit.finalizeOp(op, account, "owner")

print("Result:")
print(result)
