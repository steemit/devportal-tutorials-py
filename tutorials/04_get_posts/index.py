import pprint
from pick import pick
# initialize Steem class
from steem import Steem

s = Steem()

title = 'Please choose filter: '
#filters list
options = ['trending', 'hot', 'active', 'created', 'promoted']
# get index and selected filter name
option, index = pick(options, title)

query = {
	"limit":2, #number of posts
	"tag":"" #tag of posts
	}
#post list for selected query
posts = {0: s.get_discussions_by_trending(query),
		 1: s.get_discussions_by_hot(query),
		 2: s.get_discussions_by_active(query),
		 3: s.get_discussions_by_created(query),
		 4: s.get_discussions_by_promoted(query)
}

# print post list for selected filter
pprint.pprint(posts[index])

pprint.pprint("Selected: "+option)