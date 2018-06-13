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
posts = s.get_discussions_by_created(query)

title = 'Please choose post: '
options = []
#posts list
for post in posts:
	options.append(post["author"]+'/'+post["permlink"])
# get index and selected filter name
option, index = pick(options, title)

# posts[index] would also show post details
# but in this tutorial we are showing usage of get_content of post where author and permlink is known

details = s.get_content(posts[index]["author"],posts[index]["permlink"])

# print post details for selected post
pprint.pprint(details)
pprint.pprint("Selected: "+option)