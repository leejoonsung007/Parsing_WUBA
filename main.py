from multiprocessing import Pool
import channel_extract
import page_parsing

all_links = []
sort_links_list = []

def get_all_links_from(channel):
    # get page 1 item information
    for num in range(1,2):
        page_parsing.get_links_from(channel,num)

    # remove the overlap links
    #     sort_links_list = list(set(page_parsing.links_list))
    #     sort_links_list.sort(key=page_parsing.links_list.index)
        sort_links_list = list(set(page_parsing.links_list))
        all_links.append(sort_links_list)


# for i in range(0, len(channel_extract.channel_list)):
for i in range(0,2):
    get_all_links_from(channel_extract.channel_list.split()[i])

# print (all_links)


def get_all_items_info():
    for a in all_links:
        for b in a:
            page_parsing.get_item_info(b)


#
get_all_items_info()

# if __name__ == '__main__':
#     pool = Pool()
#     for a in range(0, len(channel_extract.channel_list)):
#         for b in range(0, len(all_links[a])):
#             pool.map(get_all_links_from,all_links[a])


