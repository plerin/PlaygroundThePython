#. Q. 표준 체중을 구하는 프로그램을 작성하시오.
'''
    성별에 따른 공식
        남자 : 키 * 키 * 22
        여자 : 키 * 키 * 21

    조건 1. 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)
    조건 2. 표준 체중은 소수점 둘째자리까지 표시
'''

#. 조건 2. 소수점 둘째자리 => round(값,2) 사용하기

def std_weight(height, gender):
    if gender == "여자":
        weight = height*height*21*0.0001
    elif gender == "남자":
        weight = height*height*22*0.0001
    return weight

height = 161
gender = "여자"
weight = round(std_weight(height,gender),2)

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))