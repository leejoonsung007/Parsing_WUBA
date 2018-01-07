import time
from page_parsing import url_list
from page_parsing import item_info

while True:
    # count the number of url_list and item_info
    print('The number of url list',url_list.find().count())
    print('The number of items information',item_info.find().count())
    time.sleep(10)
