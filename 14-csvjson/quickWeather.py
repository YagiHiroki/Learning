import json, requests, sys

#コマンドライン引数から地名を組み立てる
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ''.join(sys.argv[1:])

APPID = '1234567890'
#OpenWeatherMap.orgのAPIからJSONデータをダウンロードする
url='   daily?q={}cnt=3&appid={}'.format(location, APPID)
response = requests.get(url)
response.raise_for_status()

#JSONデータからPython変数に読み込む
weather_data = json.loads(response.txt)
#天気予報の情報を表示
w = weather_data['list']
print('{}の現在の天気:'.format(location))
print(w[0]['weaher'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('明日:')
print(w[1]['weaher'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('明後日:')
print(w[2]['weaher'][0]['main'], '-', w[2]['weather'][0]['description'])


