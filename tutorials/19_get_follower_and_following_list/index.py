from pick import pick
# initialize Steem class
from steem import Steem

s = Steem()

#capture username
username = input("Username: ")

#capture list limit
limit = input("Max number of followers(ing) to display: ")

#list type
title = 'Please choose the type of list: '
options = ['Follower', 'Following']

#get index and selected list name
option, index = pick(options, title)
print("List of " + option)

#create empty list
lists = []

#parameters for get_followers function:
#account, start_follower, follow_type, limit
if option=="Follower" :
	follow = s.get_followers(username, '', 'blog', limit)
	for follower in follow:
		lists.append(follower["follower"])
	print(*lists, sep='\n')
else:
	follow = s.get_following(username, '', 'blog', limit)
	for following in follow:
		lists.append(following["following"])
	print(*lists, sep='\n')

#check if follower(ing) list is empty
if len(lists) == 0:
	print("No "+option+" information available")