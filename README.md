# Coolmarks

Evolving browser bookmarks.


### What?

Coolmarks is a tool that allows you to save relevant web links and easily organize them to find the one you need, the moment you need it. Traditional bookmarks from web browser are still the best choice for those common websites that you want to access quickly.


### Why?

When I do intensive web surfing to research and learn about a new software library, or whatever, I often end up with lots of tabs open in my web browser and it becomes hard to keep track of them. An easy exit is to save all the tabs in a folder, but then it's not funny to browse a messed up bag of links.

Sometimes I find myself researching my own bookmarks collected during some research, trying to figure out which of them is that one I remember I found, say, a month ago. The re-research process would be easier using some metadata, like date added, and tagging the links to categorize them.


### How?

Coolmarks consists of a simple web API that receives the links of interest from the users to store the appropriate data, and a web dashboard to interact with the collected items.

It's built with [Django](https://www.djangoproject.com/) and a bunch of plugins.


## Models

### Link

An object that represents a saved link. The only required value to create a Link is the URL to be stored. Some fields are automatically calculated. The fields are:
- owner (fk)
- dt (auto)
- location
- domain (auto)
- title (auto)
- tags (fks, optional)


### Tag

Simple, few-word descriptive labels that may be related to one or more Links. New rows in this table may be created by any user. Tags are shared across users (it reduces the amount of data). The fields:
- name
- link_set (fks)
