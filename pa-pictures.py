import requests
import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.qiushibaike.com/imgrank/page/7'
for i in range(3):
    req = requests.get(url)
    html = req.text

    soup = BeautifulSoup(html,'lxml')
    result = soup.find_all('div',class_="thumb")

    current_page = soup.find_all('span',class_="current")
    cur_page = int(current_page[0].text)
    next_page = cur_page - 1
    print('========this in the page %d========'%cur_page)

    for j in result:
        link = j.img['src']
        link = 'https:'+link
        filename = link.split('/')[-1]
        try:
            urllib.request.urlretrieve(link,'pics/'+filename)
        except:
            print(link,'fail')
        else:
            print(link,'succeed')
    url = 'https://www.qiushibaike.com/imgrank/page/%d'%next_page