import pprint
from pick import pick
# initialize Steem class
from steem import Steem
from steem.commit import Commit

s = Steem()

query = {
	"limit":5, #number of posts
	"tag":"" #tag of posts
}
# post list from trending post list
posts = s.get_discussions_by_trending(query)

title = 'Please choose post to reblog: '
options = []
# post list
for post in posts:
	options.append('@'+post["author"]+'/'+post["permlink"])

# get index and selected post
option, index = pick(options, title)
pprint.pprint("You selected: "+option)

account = input("Enter your username? ")
wif = input("Enter your Posting private key? ")

# commit or build transaction
c = Commit(steem=Steem(keys=[wif]))

# broadcast transaction
c.resteem(option, account=account)
