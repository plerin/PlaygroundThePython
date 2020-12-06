#. Q. 50명의 숭객과 매칭되는 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램 작성.
'''
    조건 1. 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
    조건 2. 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
'''

#. 조건 1. 50명 승객의 소요시간 => 리스트에  반복문을 이용하여 난수를 담는다.
#. 조건 2. 반복문을 돌면서 조건 '5분 ~ 15분' 일 때와 아닐 때를 구분하여 출력, count도 늘려주기 

from random import *

passenger = [randint(5,50) for i in range(1,51)]
count = 0

for i in range(0,50):
    if 5 <= passenger[i] & passenger[i] <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(str(i+1),passenger[i]))
        count += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(str(i+1),passenger[i]))

print("총 탑승 승객 : {0} 분".format(count))