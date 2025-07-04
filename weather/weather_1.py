# 서울 위도, 경도 좌표 얻기
import requests


url_front = "http://api.openweathermap.org/geo/1.0/direct?"
url_q = "q="
q = "Seoul"
url_limit = "&limit=1"
url_appid = "&appid="
appid = "45bf7b3c369e907dab74f0f9544016c2"

url = url_front + url_q + q + url_limit + url_appid + appid
print(url,"\n")

result = requests.get(url)
json_data = result.json()
print(json_data, "\n")


x, y = json_data[0]["lon"], json_data[0]["lat"]
print(f"{q}의 위도(y),경도(x) 좌표: ({y},{x})")