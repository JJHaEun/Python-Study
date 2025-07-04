# 번호별 당첨빈도 파악
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from collections import Counter
import time

# 1. 옵션 설정
chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
options = Options()
options.binary_location = chrome_path  # 브라우저 경로 명시
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

# 2. 드라이버 설정
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 3. 사이트 열기
url = 'https://dhlottery.co.kr/gameResult.do?method=byWin&wiselog=C_A_1_1'
driver.get(url)

num_list = []
# 4. 번호 가져오기
for j in range(601,1179):
    select = Select(driver.find_element(By.CSS_SELECTOR,"#dwrNoList"))
    select.select_by_visible_text(str(j))
    driver.find_element(By.CSS_SELECTOR,"#searchBtn").send_keys(Keys.ENTER)
    time.sleep(0.1)

    for i in range(1,7):
        rotto_num = driver.find_element(By.CSS_SELECTOR,'#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span:nth-child('+ str(i) +')').text
        num_list.append(rotto_num)

    bunus_num = driver.find_element(By.CSS_SELECTOR,'#article > div:nth-child(2) > div > div.win_result > div > div.num.bonus > p > span').text
    num_list.append(bunus_num)


frequent_num = Counter(num_list)
print(frequent_num)
frequent_num_dict = dict(frequent_num)
sorted_frequent_num = sorted(frequent_num_dict.items(),key=lambda x: x[1],reverse=True)
print(sorted_frequent_num)
driver.quit()
