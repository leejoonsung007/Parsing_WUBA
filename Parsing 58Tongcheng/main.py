from multiprocessing import Pool
import channel_extract
import page_parsing


def get_all_links_from(channel):
    for num in range(1,101):
        page_parsing.get_links_from(channel,num)

if __name__ == '__main__':
    pool = Pool()
    pool.map(get_all_links_from,channel_extract.channel_list.split())