import requests
from bs4 import BeautifulSoup
import json
import time




url = 'https://www.ibiquge.cc/48/'
headerss = [
    
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'},
    {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}]
headers = headerss[0]
r =requests.get(url,headers=headers)
bs = BeautifulSoup(r.text,'lxml')
htmls = []
content = bs.find(name='div',attrs={'class':'listmain'})
BookName = bs.find(name='h1').text
chapters = content.find_all(name='dd')
for chapter in chapters:
    html = chapter.find(name='a').get('href')
    htmls.append('http://www.ibiquge.cc' + html)



res = []
cnt = 0

for page in htmls:
    str = ''
    cnt += 1
    print(f'{BookName}  {cnt}/{len(htmls)}',end='  ')
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    #print(page)
    i = 0
    while(True):
        if i>3:
            break
        try:
            headers = headerss[i]
            re = requests.get(page,headers=headers)
        except Exception as e:
            print(e)
            i += 1
            continue
        else:
            break
    bsoup = BeautifulSoup(re.text, 'lxml')
    #print(bsoup)
    content = bsoup.find(name='div',attrs={'class':'content'})
    title = content.find(name='h1').text
    context = content.find(name='div',attrs={'id':'content'}).get_text()

    #print(context)

    str += title
    str += '\n'
    str += context
    str += '\n'
    #print(str)
    time.sleep(1)
    
    with open(f'./books/test/{BookName}.txt','a',encoding='utf-8')as f:
        f.write(str)
        f.flush()