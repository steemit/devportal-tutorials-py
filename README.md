# devportal-tutorials-py

_Python Tutorials for the Developer Portal_

These examples/tutorials will familiarize you with the basics of operating on the steem blockchain.

Each tutorial is located in its own folder, and has a README.md with an outline of the basic concepts
and operations it intends to teach.

The tutorials build on each other. It's suggested you go through them in-order.

## Tutorial List

1.  [Get posts](tutorials/01_get_posts) - Pull the list of posts from different tags and filters
1.  [Get post details](tutorials/02_get_post_details) - Pull details of selected post
1.  [Get voters list](tutorials/03_get_voters_list) - Fetch list of voters on selected post
1.  [Get post replies](tutorials/04_get_post_replies) - Get replies made on selected post


## To Run one of the tutorials

Use the command line/terminal for the following instructions

1.  clone this repo

    `git clone git@github.com:steemit/devportal-tutorial-py.git`

1.  cd into the tutorial you wish to run

    ex: `cd tutorials/01_get_posts`

1.  Use pip to install dependencies

    ex: `pip install -r requirements.txt`

1.  Run the tutorial

    `python index.py`

1.  After a few moments, results should show up in terminal

## Contributing

If you're interested in contributing a tutorial to this repo. Please have a look at
[the guidelines](./tutorials/tutorial_structure.md) for the text portion of the tutorial. For general guideline please refer to [Developers Portal](https://github.com/steemit/devportal/blob/master/CONTRIBUTING.md).