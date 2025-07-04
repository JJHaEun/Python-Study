# 가장 최근 회차 당첨번호와 보너스번호 크롤링.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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


# 4. 번호 가져오기
for i in range(1,7):
    rotto_num = driver.find_element(By.CSS_SELECTOR,'#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span:nth-child('+ str(i) +')').text
    print(f"당첨번호{i}: {rotto_num}")

bunus_num = driver.find_element(By.CSS_SELECTOR,'#article > div:nth-child(2) > div > div.win_result > div > div.num.bonus > p > span').text
print(f"보너스 번호: {bunus_num}")

driver.quit()
