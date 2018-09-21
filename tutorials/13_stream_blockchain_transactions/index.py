from steem.blockchain import Blockchain

blockchain = Blockchain()
stream = blockchain.stream()

for post in stream:
	print(post)
    
