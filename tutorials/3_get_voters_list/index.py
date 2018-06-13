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
posts = s.get_discussions_by_active(query)

title = 'Please choose post: '
options = []
#posts list
for post in posts:
	options.append(post["author"]+'/'+post["permlink"])
# get index and selected filter name
option, index = pick(options, title)

# posts[index] would also have active voters info
# but in this tutorial we are showing usage of get_active_votes of post where author and permlink is known/selected

voters = s.get_active_votes(posts[index]["author"],posts[index]["permlink"])

# print post details for selected post
pprint.pprint(voters)
pprint.pprint("Selected: "+option)