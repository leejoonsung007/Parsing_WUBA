# from bs4 import BeautifulSoup
# import requests
#
# url = 'http://404.58.com/404.html?from=bj.58.com/shouji/246059546211114x.shtml'
# wb_data = requests.get(url)
# soup = BeautifulSoup(wb_data.text, 'lxml')
# no_longer_exists = str('ERROR') in soup.find('p').text
#
# if no_longer_exists:
#     print("not exists")
# else:
#     print("what")

# A = 'http://jump.zhineng.58.com/jump?target=szqLIL08PH98mvqVTHDQnHDQnHDQnHDQnHDQnHDQnHDQnHDQnHDQnEDYPHbkPHNdnHmdP10YPEDYTHcOP1DdnWEvnjmLnHNzTHcYnTDzPjTKn1mKnEDQPjb1nH03nWmQn1mdTHDKUA-1IAQ-uMEKnEDQTyRz0v6fIRtznjDLnjnkP-q-XZKtnEDVnEDKnTDkTE7hmyQ1uEDLmWK-nW6BmzdbnWTksHEkPycVrHN1PiY3mW-WuHubPv7brjnKn1cQnHmvn1mKnWTOnHDdPHbknWnOPHc3TED1P9DQTHD8PH03n1mOPjTkPHEQnWTOPTDKTEDKpZwY0jCfsvFJsWN3shPfUiq1pAqdphbfTyndsvO8nyGB0-9znAP20N6HEhwWEy0q5EDQnWn8nHcdsWcdna3QPWNKnTDkTiYKnjD3njNzrjD3njnYnjEkuE&psid=188468044195713861067956766&entinfo=29715246067152_0&type=fenqi'
# B = 'http://jump.zhineng.58.com/jump?target=szqLIL08PH98mvqVTHDQnHDQnHDQnHDQnHDQnHDQnHDQnHDQnHDQnEDYPHbkPHNdnHmdP10YPEDYTHcOP1DdnWEvnjmLnHNzTHcYnTDzPjTKn1mKnEDQPjb1nH03nWmQn1mdTHDKUA-1IAQ-uMEKnEDQTyRz0v6fIRtznjDLnjnkP-q-XZKtnEDVnEDKnTDkTE7hmyQ1uEDLmWK-nW6BmzdbnWTksHEkPycVrHN1PiY3mW-WuHubPv7brjnKn1cQnHmvn1mKnWTOnHDdPHbknWnOPHc3TED1P9DQTHD8PH03n1mOPjTkPHEQnWTOPTDKTEDKpZwY0jCfsvFJsWN3shPfUiq1pAqdphbfTyndsvO8nyGB0-9znAP20N6HEhwWEy0q5EDQnWn8nHcdsWcdna3QPWNKnTDkTiYKnjD3njNzrjD3njnYnjEkuE&psid=188468044195713861067956766&entinfo=29715246067152_0&type=fenqi'
# if A == B:
#     print("good")
# else:
#     print("what")

a = []
b = ['b','p']
c = ['c','a','6']
a.append(b)
a.append(c)
print(a)

for i in a:
    for j in i:
        print(j)
