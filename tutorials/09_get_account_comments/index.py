import pprint
from pick import pick
# initialize Steem class
from steem import Steem

s = Steem()

query = {
	"limit":5, #number of posts
	"tag":"" #tag of posts
}
#author list from created post list to randomize account list
posts = s.get_discussions_by_created(query)

title = 'Please choose account: '
options = []
#accounts list
for post in posts:
	options.append(post["author"])

# get index and selected account name
option, index = pick(options, title)

query2 = {
	"limit":5, #number of comments
	"start_author":option #selected user
}

# get comments of selected account
comments = s.get_discussions_by_comments(query2)

# print comment details for selected account
pprint.pprint(comments)
pprint.pprint("Selected: "+option)