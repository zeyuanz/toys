import requests # 导入网页请求库
from bs4 import BeautifulSoup # 导入网页解析库
import json

def scrapy_all_pages():
    result_list = []
    for i in range(1, 3):
        url = 'https://movie.douban.com/top250?start=' +str((i-1) * 25)+ '&filter='
        content_list = request_content(url)
        result_list += parse_douban(content_list)
    return result_list

def request_content(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    headers = {'user-agent': user_agent}
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    content_list = soup.find_all('div', attrs = {'class': 'item'})
    return content_list

def parse_douban(content_list):
    result_list = []
    for movie in content_list:
        dic = {}
        dic['title'] = movie.find('span', class_ = 'title').text
        dic['score'] = movie.find('span', class_ = 'rating_num').text
        try:
            dic['quote'] = movie.find('span', class_ = 'inq').text
        except:
            dic['quote'] = ''
        star = movie.find('div', class_ = 'star')
        dic['comment_num'] = star.find_all('span')[-1].text[:-3]
        result_list.append(dic)
    return result_list

def write_to_json(filename, result_list):
    movies = json.dumps(result_list, indent = 4, ensure_ascii=False)
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write(movies)

def main():
    filename = 'movie.json'
    write_to_json(filename, scrapy_all_pages())

if __name__ == '__main__':
    main()

