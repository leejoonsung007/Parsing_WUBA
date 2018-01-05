from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
ceshi = client['ceshi']
url_list = ceshi['url_list']
item_info = ceshi['item_info']

'''
spider 1:

get the link of every item

'''


def get_links_from(channel, pages, who_sells=0):
    #http://bj.58.com/diannao/0/pn2/
    list_view = '{}{}/pn{}/'.format(channel,str(who_sells),str(pages))
    wb_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    #check whether the page has sales information
    if soup.find('td','t'):
        for link in soup.select('td.t a.t'):
            item_link = link.get('href').split('?')[0]
            if item_link == 'http://jump.zhineng.58.com/jump':
                pass
            else:
                url_list.insert_one({'url': item_link})
                print(item_link)
    else:
        pass



'''
spider 2:

enter the item page and get the information of each items

including item 'title', 'price', 'date', 'area'

'''


def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    # check whether the page exists
    no_longer_exists = str('ERROR') in soup.find('p').text
    if no_longer_exists:
        pass
    else:
        title = soup.select('div.col_sub.mainTitle > h1')[0].text
        price = soup.select('span.price.c_f50')[0].text
        date = soup.select('.time')[0].text
        area = list(soup.select('.c_25d a')[0].stripped_strings) if soup.find_all('span', 'c_25d') else None
        item_info.insert_one({'title':title,'price':price,'date':date,'area':area})
        print({'title':title,'price':price,'date':date,'area':area})


#get_links_from('http://bj.58.com/shuma/',2)
# url = 'http://404.58.com/404.html?from=bj.58.com/shouji/246059546211114x.shtml'
# wb_data = requests.get(url)
# soup = BeautifulSoup(wb_data.text, 'lxml')
# print(soup.prettify())

