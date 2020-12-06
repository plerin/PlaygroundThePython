#. Q. 추첨 프로그램을 작성하시오
'''
    조건 1. 편의상 댓글은 20명이 작성, 아이디는 1~20이라고 가정
    조건 2. 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
    조건 3. random 모듈의 shuffle과 sample 을 활용
'''

#. 조건 1. 20을 list / tuple / set에 담아
#. 조건 2. shuffle로 섞고 sample로 뽑아
#. 변수 : 치킨은 1명이니까 담을 필요 없고 커피는 리스트에 담자(add)

from random import *

# people =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]    # list(range(1,21))
people = list(range(1,21))
shuffle(people)

chicken = sample(people,1)
coffee = sample(people,3)
#. 아 .. coffee 랑 chicken이랑 중복되면 안되니까 처음 뽑을 때 4개를 봅아야 해!
#. winners = sample(people,4)

print('-- 당첨자 발표 --')
print('치킨 당첨자 : %d' %(chicken[0]))
print('커피 당첨자 : {coffee}'.format(coffee = coffee))
print('-- 축하합니다 --')