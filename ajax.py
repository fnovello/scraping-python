import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest'
}

s = requests.Session()
login_url='https://testvuejs-44f38.firebaseio.com/datos.json'
login_data='{"clave":" python","email":"fucking python ","fecha":"17/05/python 01:43","nombre":"python"}'
s.post(login_url, data=login_data)

content = s.post(url, data=data_video, headers=headers)