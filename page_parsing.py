from bs4 import BeautifulSoup
import requests
import time
import pymongo
import re

# app.mongo = MongoClient(host='0.0.0.0',port=27017,connect=False)
client = pymongo.MongoClient('localhost',27017,connect = False)
wuba = client['wuba']
url_list = wuba['url_list1']
item_info = wuba['item_info']

'''
spider 1:

get the link of every item

'''
links_list = []
all_links = []

def get_links_from(channel, pages, who_sells=1):
    #create links link http://bj.58.com/diannao/0/pn2/
    list_view = '{}{}/pn{}/'.format(channel,str(who_sells),str(pages))
    wb_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    #check whether the page has sales information
    if soup.find('td','t') or soup.find('a','title t'):
        # check the items are from 58 store or zhuanzhuan
        # if ignore one of them, lots of information will lose
        if soup.select('div.left > a.title.t'):
            for single_item_link in soup.select('a.title.t'):
                stuff_link = single_item_link.get('href')
                links_list.append(stuff_link)
                url_list.insert_one({'url':stuff_link})

        if soup.select('td.t.t_b > a'):
            for link in soup.select('td.t.t_b > a'):
                item_link = link.get('href')
                links_list.append(item_link)
                url_list.insert_one({'url': item_link})

        if soup.select("td.t a.t"):
            for zhuanzhuan_link in soup.select("td.t a.t"):
                zhuanzhuan_item_link = zhuanzhuan_link.get('href')
                links_list.append(zhuanzhuan_item_link)
                url_list.insert_one({'url': zhuanzhuan_item_link})
        # print(links_list)
    else:
        pass

# get_links_from('http://bj.58.com/shouji/',1)
# print(links_list)
# sort_links_list = list(set(links_list))
# sort_links_list.sort(key=links_list.index)
# print(sort_links_list)

# print(sort_links_list)

'''
spider 2:

enter the item page and get the information of each items

including item 'title', 'price', 'date', 'area'

'''


def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    # for test in cate:
    #     print(test.text)
    check_error = soup.select('p')
    for x in range(0,len(check_error)):
        if check_error[x].text == 'ERROR':
            pass

    try:
        # check whether page is from 58 store or zhuanzhuan
        # key point: find their unique feature
        # use try ... exception to avoid some strange pages
        check_zhuanzhuan = soup.select('div')
        for y in range(0, len(check_zhuanzhuan)):
            if check_zhuanzhuan[y].text == '58二手全新升级，新品牌，新服务':
                zhuanzhuan_title = soup.select('h1.info_titile')[0].text
                zhuanzhuan_price = soup.select('span.price_now > i')[0].text
                zhuanzhuan_area = soup.select('div.palce_li > span > i')[0].text.split('-') if soup.find_all('div', 'palce_li') else None
                zhuanzhuan_cate = soup.select('.breadCrumb > span')[-1].text
                zhuanzhuan_cate_handling = re.sub("\s","",zhuanzhuan_cate)
                item_info.insert_one({'title':zhuanzhuan_title,'price':zhuanzhuan_price,'area':zhuanzhuan_area,
                                      'publish_time':None,'cate':zhuanzhuan_cate_handling})
                print({'title': zhuanzhuan_title, 'price': zhuanzhuan_price, 'area': zhuanzhuan_area,'cate':zhuanzhuan_cate_handling, 'publish_time':None})

        check = soup.select('span')
        for z in range(0, len(check)):
            if check[z].text == '收藏':
                title = soup.select('div.col_sub.mainTitle > h1')[0].text
                price = soup.select('span.price.c_f50')[0].text
                area = list(soup.select('.c_25d a')[0].stripped_strings) if soup.find_all('span', 'c_25d') else None
                publish_time= soup.select('li.time')[0].text
                cate = soup.select('.breadCrumb > span')[-1].text
                cate_handling = re.sub("\s","",cate)
                item_info.insert_one({'title':title,'price':price,'area':area,'publish_time':publish_time, 'cate':cate_handling})
                print({'title':title,'price':price,'area':area,'cate':cate_handling,'publish_time':publish_time})

    except:
        print("**************广告***************")
        pass

# for single_link in sort_links_list:
#     # print(single_link)
#     get_item_info(single_link)

# get_item_info('http://zhuanzhuan.58.com/detail/750567735711825924z.shtml')
# get_item_info('http://bj.58.com/diannao/24439862996659x.shtml')
# get_item_info('http://bj.58.com/shouji/32514620978483x.shtml')
# get_item_info('http://bj.58.com/diannao/32555626200502x.shtml')
# get_item_info('http://bj.58.com/diannao/32623493069740x.shtml')
# get_item_info('http://bj.58.com/diannao/32656067570495x.shtml')
# get_item_info('http://bj.58.com/diannao/32103957237948x.shtml') #广告
# get_item_info('http://bj.58.com/huishou/31384237015851x.shtml') #广告
# url = 'http://404.58.com/404.html?from=bj.58.com/shouji/246059546211114x.shtml'
# wb_data = requests.get(url)
# soup = BeautifulSoup(wb_data.text, 'lxml')
# print(soup.prettify())

