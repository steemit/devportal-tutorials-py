# devportal-tutorials-py

_Python Tutorials for the Developer Portal_

These examples/tutorials will familiarize you with the basics of operating on the steem blockchain.

Each tutorial is located in its own folder, and has a README.md with an outline of the basic concepts
and operations it intends to teach.

The tutorials build on each other. It's suggested you go through them in-order. 

*Note: You'll notice the tutorial directories skip numbers in their prefixes. This is deliberate; we're mirroring our curriculum as much as possible accross languages, and getting to the less critical tutorials per-language later.*

## Tutorial List

1.  [Using keys securely](001_using_keys_securely) - Learn how Steem-Python library handles transaction signing with user's key and how to securely manage your private keys.
1.  [Dev requirements](tutorials/00_getting_started) - Environment requirements for developers
1.  [Get posts with filters](tutorials/04_get_posts) - How to query for posts with specific filters & tags.
1.  [Get post details](tutorials/05_get_post_details) - How to get details of each post.
1.  [Get voters list on content](tutorials/06_get_voters_list_on_post) - How to get voters info on post/comment.
1.  [Get post comments](tutorials/07_get_post_comments) - How to fetch all comments made on particular post.
1.  [Get account replies](tutorials/08_get_account_replies) - How to get list of latest comments made on content of particular account.
1.  [Get account comments](tutorials/09_get_account_comments) - How to get list of comments made by particular account.
1.  [Submit post](tutorials/10_submit_post) - How properly format and submit post.
1.  [Submit comment](tutorials/11_submit_comment_reply) - How to submit reply to particular post.
1.  [Edit content](tutorials/12_edit_content_patching) - How to properly patch edited content and submit edits.
1.  [Reblog/Resteem a post](tutorials/14_reblogging_post) - How to reblog/resteem a post
1.  [Search accounts](tutorials/15_search_accounts) - Search for user accounts by partial username.
1.  [Search for tags](tutorials/16_search_tags) - Search for trending tags.
1.  [Vote on content](tutorials/17_vote_on_content) - Create a weighted up or down vote on a comment/post.
1.  [Follow a user](tutorials/18_follow_a_user) - Follow and unfollow a user / author.
1.  [Get follower & following list](tutorials/19_get_follower_and_following_list) - Get the followers of a user/author & the authors that user is following.
1.  [Account reputation](tutorials/20_account_reputation) - Learn how to interpret account reputation.
1.  [Transfer STEEM & SBD](tutorials/21_transfer_STEEM_and_SBD) - Transfer both STEEM and SBD from one account to another.
1.  [Witness listing & voting](tutorials/22_witness_listing_and_voting) - Create a list of available witnesses as well as vote for and remove your vote for a witness.
1.  [Claim rewards](tutorials/23_claim_rewards) - Learn how to claim rewards from unclaimed reward balance using Steemconnect as well as client signing method.
1.  [Power up](tutorials/24_power_up_steem) - Power up an account's Steem using either Steemconnect or a client-side signing.
1.  [Power down](tutorials/25_power_down) - Perform a power down on all or part of an account's VESTS using either Steemconnect or client-side signing.
1.  [Delegate steem power](tutorials/27_delegate_power) - Delegate power to other users using Steemconnect or Client-side signing.
1.  [Get delegations by user](tutorials/29_get_delegations_by_user) - View the vesting delegations made by a user as well as the delegations that are expiring.
1.  [Grant posting permission](tutorials/30_grant_posting_permission) - How to grant and revoke posting permission to another user.
1.  [Grant active permission](tutorials/31_grant_active_permission) - How to grant and revoke active permission to another user.
1.  [Change password and keys](tutorials/33_grant_active_permission) - How to change your accounts password and keys.


## To Run one of the tutorials

Use the command line/terminal for the following instructions

1.  clone this repo

    `git clone git@github.com:steemit/devportal-tutorial-py.git`

1.  cd into the tutorial you wish to run

    ex: `cd tutorials/04_get_posts`

1.  Use pip to install dependencies

    ex: `pip install -r requirements.txt`

1.  Run the tutorial

    `python index.py`

1.  After a few moments, results should show up in terminal

## Contributing

If you're interested in contributing a tutorial to this repo. Please have a look at
[the guidelines](./tutorials/tutorial_structure.md) for the text portion of the tutorial. For general guideline please refer to [Developers Portal](https://github.com/steemit/devportal/blob/master/CONTRIBUTING.md).
