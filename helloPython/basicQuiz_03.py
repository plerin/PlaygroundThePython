#. Q. 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
'''
    예) http://naver.com
    규칙 1. http:// 부분은 제외 => naver.com
    규칙 2. 처음 만는 점(.) 이후 부분은 제외 => naver
    규칙 3. 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
'''

# 1. replace('http://','') 하고 변수에 저장
# 2. index(.)으로 '.'의 index를 찾고  1번 변수 [0,index] 결과 변수 저장
# 3. [:3] + 2번변수명.count() + 2번변수명.count('e') + !

#input_site = "http://naver.com"
input_site = "http://daum.com"
rule_1 = input_site.replace('http://','') 

idx_dot = rule_1.index('.')
rule_2 = rule_1[:idx_dot]

rule_3 = rule_2[:3] + str(len(rule_2)) + str(rule_2.count('e')) + "!"

#print("{first3}".format(first3 = rule_2[:3]))

#print("%s%d%d%s" %(rule_2[:3],len(rule_2),rule_2.count('e'),"!"))
# print("{first3}{word_len}{count_e}!" .format(first3 = rule_2[:3], word_len = len(rule_2), count_e = rule_2.count('e')))
print("{0}의 비밀번호는 {1} 입니다.".format(input_site, rule_3))