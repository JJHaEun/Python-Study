# 정규식으로 주민번호 추출

import re

with open('regex_test.txt','r') as File:
    data = File.read()

print(data);


p = re.compile(r'\d{6}[-]\d{7}')
rrn_list = re.findall(p, data)
print(rrn_list)