# 주민등록번호
# 901201-1111111

# 이메일 주소 
# zborisz@naver.com
# zborisz@naver@google.com

# 차량 번호 
# 11가 1234
# 123가 1234

# ip 주소
# 192.168.40.94
# 1000.2000.3000.4000

import re
# abcd, book, desk
# ca?e

p = re.compile("ca.e") 
# . (ca.e) : 하나의 문자를 의미 > care, cafe
# ^ (^de) : 문자열의 시작 > desk, destination
# $ (se$) : 문자열의 끝 > case base, 



def print_match(m):
    if m:
        print("m.group() : ", m.group())    # 일치하는 문자열 반환
        print("m.string : " , m.string)     # 입력받으 문자열, 함수가 아닌 변수 
        print("m.start() : " , m.start())   # 일치하는 문자 시작 index
        print("m.end() : " , m.end())       # 위와 반대
        print("m.span() : " , m.span())
    else:
        print("매칭되지않았습니다.")

# m = p.match("careless") # 주어진 문자열의 처음부터 일지하는지 확인
# print_match(m)

# m = p.search("good care")
# print_match(m)

lst = p.findall("good care cafe")
print(lst)

# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열")
# 4. lst = p.findall("비교할 문자열")