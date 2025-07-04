# 정규식 없이 주민번호 추출하기

with open('regex_test.txt','r') as File:
    data = File.readlines()

print(data);


rrn_list = []

for line in data:
    line_split = line.split('-')
    print(line_split)
    
    rrn_front = line_split[0][-6:]
    rrn_back = line_split[1][:7]
    rrn = rrn_front + "-" + rrn_back
    rrn_list.append(rrn)

print(rrn_list)