# Get account replies

_By the end of this tutorial you would know how to get replies made on particular account's content._

This tutorial will explain and show you how to access the **Steem** blockchain using the [steem-python](https://github.com/steemit/steem-python) library to fetch list of comments made on a specific accounts contect, in this case, `@steemitblog`.

## Intro

All python tutorials will be in Python3 and developers following these tutorials should have sufficient knowlegde to use pip/pip3 package manager. Your development environment should be set up properly to test these tutorials.

In Steem there are built-in functions in the official library `steem-python` that we are going to use throughout all Python tutorials. For this one we are using the `get_content_replies` function.


## Steps

1.  [**App setup**](#app-setup) - Library install and import
1.  [**Post list**](#post-list) - List of filters to select from
1.  [**Comment details**](#comment-details) - Form a query
1.  [**Print output**](#print-output) - Print results in output

#### 1. App setup <a name="app-setup"></a>

In this tutorial we use 3 packages, `pick` - helps us to select filter interactively. `steem` - steem-python library, interaction with Blockchain. `pprint` - print results in better format.

First we import all three library and initialize Steem class

```python
    import pprint
    from pick import pick
    # initialize Steem class
    from steem import Steem

    s = Steem()
```

#### 2. Post list <a name="post-list"></a>


Next we will fetch and make list of posts and setup `pick` properly.

```python
    query = {
        "limit":5, #number of posts
        "tag":"" #tag of posts
        }
    #post list for selected query
    posts = s.get_discussions_by_created(query)

    title = 'Please choose post: '
    options = []
    #posts list options
    for post in posts:
        options.append(post["author"]+'/'+post["permlink"])
    # get index and selected filter name
    option, index = pick(options, title)
```

This will show us list of posts to select in terminal/command prompt. And after selection we will get index and post name to `index` and `option` variables.

#### 3. Comment details <a name="comment-details"></a>

Next we will fetch post details with `get_content`. By default `get_discussions_by_created` function already contains post details, but for this tutorial purpose we will ignore all other fields but only use `author` and `permlink` fields to fetch fresh post details.

```python
# in this tutorial we are showing usage of get_content of post where author and permlink is known

details = s.get_content_replies(posts[index]["author"],posts[index]["permlink"])
```

Above code shows example of query and simple list of function that will fetch comments list with user selected filter.

#### 4. Print output <a name="print-output"></a>

Next, we will print result, details of selected post.

```python
    # print post details for selected post
    pprint.pprint(details)
    pprint.pprint("Selected: "+option)
```

### To Run the tutorial

1.  clone this repo
1.  `cd tutorials/1_get_posts`
1.  `pip install -r requirements.txt`
1.  `python index.py`
1.  After a few moments, you should see output in terminal/command prompt screen.