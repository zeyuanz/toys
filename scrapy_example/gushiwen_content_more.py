import requests # 导入网页请求库
from bs4 import BeautifulSoup # 导入网页解析库
import json
import time

def request_get(url, headers):
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def parse_content(url, headers, result_list):
    content_list = request_get(url, headers).find_all('div', attrs = {'class': 'cont'})
    for content in content_list:
        if content.find('div', attrs = {'class': 'contson'}):
            dic = {}
            # get all infos
            title = content.find('a', attrs = {'target': '_blank'})
            author_dynasty = content.find('p', attrs = {'class': 'source'})
            author = author_dynasty.find_all('a')[0].text
            dynasty = author_dynasty.find_all('a')[1].text
            sons = content.find('div', attrs = {'class': 'contson'})
            dic['title'] = title.text
            print('scrapy %s' %(title.text))
            dic['author'] = author
            dic['dynasty'] = dynasty
            dic['main'] = sons.text.strip('\n').strip(' ')

            # go to secondary page
            possible_links = request_get(title['href'], headers).find_all('a')
            cnt = 0
            others = []
            for l in possible_links:
                if l.text == '展开阅读全文 ∨':
                    script = l['href']
                    id_start = script.find("'")
                    id_end = script.find("'", id_start+1)
                    id_translation_notation = script[id_start+1:id_end]
                    url = 'https://so.gushiwen.cn/nocdn/ajaxfanyi.aspx?id='+id_translation_notation
                    if cnt > 0:
                        url = 'https://so.gushiwen.cn/nocdn/ajaxshangxi.aspx?id='+id_translation_notation
                    others.append(request_get(url, headers).text)
                    cnt += 1
            dic['others'] = others 
            result_list.append(dic)
    return result_list

def main():
    result_list = []
    cookie = 'ASP.NET_SessionId=kdtzhj3gkzn3kh0wquioc3dm; login=flase; \
    Hm_lvt_9007fab6814e892d3020a64454da5a55=1632906772,1632968539,1632968565,1632986300; \
    Hm_lpvt_9007fab6814e892d3020a64454da5a55=1632988072; wxopenid=defoaltid'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    headers = {'user-agent': user_agent, 'cookie': cookie}

    for i in range(1,2):
        url = 'https://so.gushiwen.cn/shiwen/default_0AA'+str(i)+'.aspx'
        result_list = parse_content(url, headers, result_list)

    sons = json.dumps(result_list, indent = 4, ensure_ascii=False)
    with open('sons.json', 'w', encoding = 'utf-8') as f:
        f.write(sons)

if __name__ == '__main__':
    main()
