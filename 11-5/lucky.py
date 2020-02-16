import requests
import sys
import webbrowser
import bs4

print('Googling...')#Googleページをダウンロード中にテキストを表示
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

print(res.text)

#リンクを取得する
soup = bs4.BeautifulSoup(res.text)
link_elems = soup.select('.r a')

#タブで開く
num_open = min(5, len(link_elems))
for i in range(num_open):
    webbrowser.open('http://google.com/' + link_elems[i].get('href')) 

