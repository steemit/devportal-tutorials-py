from steem import Steem
from pick import pick

# initialize Steem class

s = Steem()

#choose list type
title = 'Please select type of list:'
options = ['Active Account names', 'Trending tags']

#get index and selected list name
option, index = pick(options, title)

if option=='Active Account names' :
	#capture starting account
	account = input("Enter account name to start search from: ")
	#input list limit
	limit = input("Enter max number of accounts to display: ")
	lists = s.lookup_accounts(account, limit)
	print('\n' + "List of " + option + '\n')
	print(*lists, sep='\n')
else :
	#capture starting tag
	aftertag = input("Enter tag name to start search from: ")
	#capture list limit
	limit = input("Enter max number of tags to display: ")
	lists = s.get_trending_tags(aftertag, limit)
	print('\n' + "List of " + option + '\n')
	for names in lists :
		print(names["name"])