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
rotto_num1 = driver.find_element(By.CSS_SELECTOR,'#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span:nth-child(1)').text
print(f"당첨번호1: {rotto_num1}")

driver.quit()
