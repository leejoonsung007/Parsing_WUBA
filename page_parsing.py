from bs4 import BeautifulSoup
import requests
import time
import pymongo


client = pymongo.MongoClient('localhost',27017,connect = False)
ceshi = client['ceshi']
url_list = ceshi['url_list']
item_info = ceshi['item_info']

'''
spider 1:

get the link of every item

'''
links_list = []
all_links = []

def get_links_from(channel, pages, who_sells=0):
    #creat links like http://bj.58.com/diannao/0/pn2/
    list_view = '{}{}/pn{}/'.format(channel,str(who_sells),str(pages))
    wb_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    #check whether the page has sales information
    if soup.find('td','t'):
        # check the items are from 58 store or zhuanzhuan
        # if ignore one of them, lots of information will lose
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


# get_links_from('http://bj.58.com/diannao/',1)
# sort_links_list = list(set(links_list))
# sort_links_list.sort(key=links_list.index)
# print(sort_links_list)
# print(links_list)
# print(sort_links_list)

'''
spider 2:

enter the item page and get the information of each items

including item 'title', 'price', 'date', 'area'

'''


def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    check_error = soup.select('p')
    for x in range(0,len(check_error)):
        if check_error[x].text == 'ERROR':
            pass

    try:
        # check whether page is from 58 store or zhuanzhuan
        # key point: find their unique feature 
        check_zhuanzhuan = soup.select('div')
        for y in range(0, len(check_zhuanzhuan)):
            if check_zhuanzhuan[y].text == '58二手全新升级，新品牌，新服务':
                zhuanzhuan_title = soup.select('h1.info_titile')[0].text
                zhuanzhuan_price = soup.select('span.price_now > i')[0].text
                zhuanzhuan_area = soup.select('div.palce_li > span > i')[0].text.split('-') if soup.find_all('div', 'palce_li') else None
                item_info.insert_one({'title':zhuanzhuan_title,'price':zhuanzhuan_price,'area':zhuanzhuan_area})
                print({'title': zhuanzhuan_title, 'price': zhuanzhuan_price, 'area': zhuanzhuan_area})

        check = soup.select('span')
        for z in range(0, len(check)):
            if check[z].text == '收藏':
                title = soup.select('div.col_sub.mainTitle > h1')[0].text
                price = soup.select('span.price.c_f50')[0].text
                area = list(list(soup.select('.c_25d a')[0]) + list(soup.select('.c_25d a')[1])) \
                if soup.find_all('span','c_25d') else None
                item_info.insert_one({'title':title,'price':price,'area':area})
                print({'title':title,'price':price,'area':area})
    except:
        print("**************advertisement***************")
        pass

# for single_link in sort_links_list:
#     # print(single_link)
#     get_item_info(single_link)

# get_item_info('http://zhuanzhuan.58.com/detail/750567735711825924z.shtml')
# get_item_info('http://bj.58.com/diannao/24439862996659x.shtml')
# get_item_info('http://bj.58.com/diannao/30920286748108x.shtml')
# get_item_info('http://bj.58.com/diannao/32555626200502x.shtml')
# get_item_info('http://bj.58.com/diannao/32623493069740x.shtml')
# get_item_info('http://bj.58.com/diannao/32656067570495x.shtml')
# get_item_info('http://bj.58.com/diannao/32103957237948x.shtml') # advertisement
# get_item_info('http://bj.58.com/huishou/31384237015851x.shtml') # advertisement
# url = 'http://404.58.com/404.html?from=bj.58.com/shouji/246059546211114x.shtml'
# wb_data = requests.get(url)
# soup = BeautifulSoup(wb_data.text, 'lxml')
# print(soup.prettify())

