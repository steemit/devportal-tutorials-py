import pprint
from pick import pick
# initialize Steem class
from steem import Steem

s = Steem()

query = {
	"limit":5, #number of posts
	"tag":"" #tag of posts
	}
#post list for selected query
posts = s.get_discussions_by_hot(query)

title = 'Please choose post: '
options = []
#posts list
for post in posts:
	options.append(post["author"]+'/'+post["permlink"])
# get index and selected filter name
option, index = pick(options, title)

# get replies for given post
replies = s.get_content_replies(posts[index]["author"],posts[index]["permlink"])

# print post details for selected post
pprint.pprint(replies)
pprint.pprint("Selected: "+option)
pprint.pprint("Number of replies: "+str(len(replies)))