# 현재 기온 정보 얻기
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

url_front2 = "https://api.openweathermap.org/data/2.5/weather?"
url_lat = "lat="

url_lon = "&lon="

url2 = url_front2 + url_lat + str(y) + url_lon + str(x) + url_appid + appid
print(url2,"\n")

result2 = requests.get(url2)
json_data2 = result2.json()
print(json_data2, "\n")

temperature = int(json_data2['main']['temp'] - (273.15)) 
print(f"현재 {q}의 기온은 섭씨 {temperature}도 입니다.")