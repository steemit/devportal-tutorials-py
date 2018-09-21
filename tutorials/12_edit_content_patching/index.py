import steembase
import steem
from diff_match_patch import diff_match_patch

# connect to testnet
steembase.chains.known_chains['STEEM'] = {
    'chain_id': '79276aea5d4877d9a25892eaa01b0adf019d3e5cb12a97478df3298ccdd01673',
    'prefix': 'STX', 'steem_symbol': 'STEEM', 'sbd_symbol': 'SBD', 'vests_symbol': 'VESTS'
}

#capture user information
username = input('Enter username: ') #demo account: cdemo
wif = input('Enter private POSTING key: ') #demo account: 5JEZ1EiUjFKfsKP32b15Y7jybjvHQPhnvCYZ9BW62H1LDUnMvHz

#connect node and private active key
client = steem.Steem(nodes=['https://testnet.steem.vc'], keys=[wif])

#check valid username
userinfo = client.get_account(username)
if(userinfo is None) :
    print('Oops. Looks like user ' + username + ' doesn\'t exist on this chain!')
    exit()

post_author = input('Please enter the AUTHOR of the post you want to edit: ')
post_permlink = input('Please enter the PERMLINK of the post you want to edit: ')

#get details of selected post
details = client.get_content(post_author, post_permlink)

print('\n' + 'Title: ' + details['title'])
o_body = details['body']
print('Body:' + '\n' + o_body + '\n')

n_body = input('Please enter new post content:' + '\n')

#initialise the diff match patch module
# dmp = dmp_module.diff_match_patch()
dmp = diff_match_patch()

#Check for null input
if (n_body == '') :
    print('\n' + 'No new post body supplied. Operation aborted')
    exit()
else :
    # Check for equality
    if (o_body == n_body) :
        print('\n' + 'No changes made to post body. Operation aborted')
        exit()

#check for differences in the text field
diff = dmp.diff_main(o_body, n_body)
#Reduce the number of edits by eliminating semantically trivial equalities.
dmp.diff_cleanupSemantic(diff)
#create patch
patch = dmp.patch_make(o_body, diff)
#create new text based on patch
patch_body = dmp.patch_toText(patch)
#check patch length
if (len(patch_body) < len(o_body)) :
    new_body = patch_body
else :
    new_body = n_body
    
#commit post to blockchain with all old values and new body text
client.commit.post(title=details['title'], body=new_body, author=details['author'], permlink=details['permlink'],
    json_metadata=details['json_metadata'], reply_identifier=(details['parent_author'] + '/' + details['parent_permlink']))

print('\n' + 'Content of the post has been successfully updated')