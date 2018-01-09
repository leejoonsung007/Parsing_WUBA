# Parsing_WUBA

This program aim to parse http://bj.58.com/sale.shtml

# channel_extract.py
Extract the links of each channels

# page_parsing.py
1. Get the links of items in a channel
such as: I want to get all items links in http://bj.58.com/shouji/
stored in MongoDB

2. Based on the items links I get, get the items basic information
Stored in MongoDB

# main.py
Call channel_extract and page_parsing

# counts.py
Counting the number of item_list and item_info in DB

# visualisation page
use package charts to generate visualization
and it also concludes some operations for MongoDB

db.collection.update()
eg.item_info.update({'_id':i['_id']},{'$set':{'area':area}}) - update_database

db.aggregate(pipeline)
pipeline = [
    {'$match':{'publish_time':'2017-12-13'}},  - like find()
    {'$group':{'_id':'$price','counts':{'$sum':1}}}, change _id to price, and counts the times(each time +1)
    {'$sort':{'counts':-1}}, -1 represents from large to small, 1 represents small to large
    {'$limit':3}, get the first three
] - much more effective than 'for' statement in python

