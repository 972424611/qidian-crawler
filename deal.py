import requests
from bs4 import BeautifulSoup
import pandas
from requests.exceptions import ReadTimeout, ConnectionError, RequestException
from datetime import datetime
import threading

def sum(map):
    books = []
    books.append(map)
    newsdf = pandas.DataFrame(books)
    #不要列头, 不要索引, mode='a'续写
    newsdf.to_csv('D:/test6.csv', header=False, index=False, mode='a')

def target(soup):
    for li in soup.select('.all-img-list li'):
        pp = li.select('p')[1].text.replace('\n\r', '')
        pp = pp.strip()
        h4 = li.find('h4')
        a = h4.find('a')
        url2 = 'https:' + a['href']
        print(threading.current_thread().name + "  " + url2)
        try:
            res2 = requests.get(url2)
        except ReadTimeout:
            print("timeout")
        except ConnectionError:
            print("connection Error")
        except RequestException:
            print("RequestException error")
        except requests.excepitons:
            print("error")
        soup2 = BeautifulSoup(res2.text, 'html.parser')
        for book in soup2.select('.book-info '):
            #now = datetime.now()
            time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sum({'title':book.select('em')[0].text, 'name':book.select('span a')[0].text,
                 'describe':pp, 'wordcount':book.select('p')[2].select('em')[0].text,
                 'click':book.select('p')[2].select('em')[1].text, 'time':time})
            break