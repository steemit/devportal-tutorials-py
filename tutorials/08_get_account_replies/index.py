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
#we are merely using this to display the most recent posters
#the 'author' can easily be changed to any value within the 'get_replies' function

posts = s.get_discussions_by_created(query)

title = 'Please choose author: '
options = []
#posts list
for post in posts:
	options.append(post["author"]+'/'+post["permlink"])
# get index and selected filter name
option, index = pick(options, title)
# option is printed as reference
pprint.pprint("Selected: "+option)

# in this tutorial we are showing usage of get_replies of post where the author is known

# allocate variables
_author = posts[index]["author"]
_limit = 1

# get replies for specific author
details = s.get_replies(_author)

# print specified number of comments

pprint.pprint(details[:_limit])