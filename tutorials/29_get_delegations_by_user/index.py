from pick import pick
from steem import Steem

import pprint

client = Steem()

#capture username
username = input('Username: ')

#check username
result = client.get_account(username)
if not result:
	print('Invalid username')
	exit()

#capture list limit
limit = input('Max number of vesting delegations to display: ')

#list type
title = 'Please choose the type of list: '
options = ['Active Vesting Delegations', 'Expiring Vesting Delegations']

#get index and selected list name
option, index = pick(options, title)
print('\n' + 'List of ' + option + ': ' + '\n')


#parameters: account, from_account, limit
if option=='Active Vesting Delegations' :
	delegations = client.get_vesting_delegations(username, '', limit)
	if len(delegations) == 0:
		print('No ' + option)
	else:
		pprint.pprint(delegations)
else: #parameters: account, start: steembase.types.PointInTime, limit
	delegations = client.get_expiring_vesting_delegations(username, "2018-01-01T00:00:00", limit)
	if len(delegations) == 0:
		print('No ' + option)
	else:
		pprint.pprint(delegations)