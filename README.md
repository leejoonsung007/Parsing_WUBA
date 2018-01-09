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

# Main.py
Call channel_extract and page_parsing

# counts.py
Counting the number of item_list and item_info in DB


