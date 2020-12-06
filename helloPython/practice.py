'''
animal = "강아지"
name = "연탄이"
age = 4
is_adult = age >= 3


print("우리집 " + animal + "의 이름은 " + name + "입니당")
print(name + "는 " + str(age) + "살입니당")
print(name + "는 어른일까요? " + str(is_adult))
'''

'''
print(not(1 != 3))
print(10//3)
print((3> 0) & (3 < 5))
print((3> 0) | (7 < 5))
'''

#. 랜덤함수

from random import *

#print(random()) # 0.0 ~ 1.0 미만 임의의 값 생성 
#print(random() * 10) # 0.0 ~ 10.0 미만의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 이하의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 이하의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 이하의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 이하의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 이하의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 이하의 값 생성

# print(int(random() * 45) + 1) # 1~ 45 이하의 값 생성
# print(int(random() * 45) + 1) # 1~ 45 이하의 값 생성
# print(int(random() * 45) + 1) # 1~ 45 이하의 값 생성
# print(int(random() * 45) + 1) # 1~ 45 이하의 값 생성
# print(int(random() * 45) + 1) # 1~ 45 이하의 값 생성
# print(int(random() * 45) + 1) # 1~ 45 이하의 값 생성

# print(randrange(1,46)) # 1 ~ 46미만의 임의의 값 생성
# print(randrange(1,46)) # 1 ~ 46미만의 임의의 값 생성
# print(randrange(1,46)) # 1 ~ 46미만의 임의의 값 생성
# print(randrange(1,46)) # 1 ~ 46미만의 임의의 값 생성
# print(randrange(1,46)) # 1 ~ 46미만의 임의의 값 생성
# print(randrange(1,46)) # 1 ~ 46미만의 임의의 값 생성

# print(randint(1,45)) # 1 ~ 45이하의 임의의 값 생성
# print(randint(1,45))
# print(randint(1,45))
# print(randint(1,45))
# print(randint(1,45))
# print(randint(1,45))

# #. 문자열
# sentence3 = """
# 나는 김기훈입니다.
# 감사합니다.
# """

# print(sentence3)


# con = "940321-1235123"

# print("연 : " + con[0:2]) #. 0부터 2직전까지 , 0,1 == 94
# print("연 : " + con[:6]) #. 처음부터 7직전까지
# print("연 : " + con[7:]) #. 7부터 끝가지
# print("연 : " + con[-7:]) #. 맨뒤에서 7부터 끝가지

# #. 문자열 처리

# python = "Python is Amaging"
# print(python.lower())
# print(python.upper())
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)
# index = python.index("n",index + 1)
# print(index)

# print(python.find("n"))
# print(python.count("n"))


#. 문자열 포맷

# print("나는 %s살입니다. " % 20)
# print("나는 %s을 좋아해요 " % "파이썬")
# print("나는 %s색과 %s색을 좋아해요 " % ("빨간","파란"))

# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요 ".format("빨간","파란"))
# print("나는 {1}색과 {0}색을 좋아해요 ".format("빨간","파란"))
# print("나는 {age}살이고 {color}색을 좋아해요 ".format(age =27, color="초록"))

# age = 20
# color = "빨간"

# print(f"나는 {age}살이고 {color}색을 좋아해요 ")


#. 탈출문자 = escape letter 


##. 리스트 []

# subway = [10, 20, 30]
# print(subway)
# subway.append("김기훈")
# print(subway.index("김기훈"))
# subway.insert(2,"김철수")
# subway.pop()
# print(subway)

# subway = ["김기훈","박경남","김기훈"]
# print(subway)
# print(subway.count("김기훈"))

# num_list = [5,1,2,3,76,2,34,6,1]
# num_list.sort()
# print(num_list)

#. 사전(dictionary)

# cabinet = {3:"김기훈", 100:"김호중"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(5))
# print(cabinet.get(5,"사용 가능"))

# print(3 in cabinet)

# cabinet = {"A-3":"김기훈", "A-100":"김호중"}
# print(cabinet["A-3"])

# del cabinet["A-100"]
# print(cabinet)

# print(cabinet.keys())

##. 튜플(tuple) , 변경할 수 없지만 list보다 빨라
# menu = ("돈까스", "치즈까스")
# print(menu[0])

# # name = "김종국"
# # age = 20
# # hobby = "코딩"
# # print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")

# my_set = {1,2,3,4,4,4,5,6}
# print(my_set)

# java = {"김기훈","박경남","박현아"}
# python = {"김기훈","김우진"}

# print(java & python)

# print(java | python)

# print(java - python)

# python.add("박경남")
# print(python)

# java.remove("박현아")
# print(java)

# menu = {"커피","우유","주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu)) 

# weather = input("오늘 날씨는 어때요? " )
# if weather == "비" or weather == "눈ㄴ":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 없어요")

# temp = int(input("기온은 어때요 ? "))
# if 30 <= temp:
#     print("너무 더우니까 나가지마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨입니당")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추우니까 나가지 마세요")

##. for문

# for waiting_no in list(range(1,5)):
#     print("대기번호 {0}".format(waiting_no))

# starbucks = ["아이언맨","토르","그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

##. while문
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았아요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")


# customer = "토르"
# person = "Unknown"

# while person != customer :
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")

# absent = [2,5]
# for student in range(1,11):
#     if student in absent :
#         continue
#     print("{0}야 책을 읽어봐".format(student))

# students = ["IRON MAN", "THOR" ," AM GROOT"]
# #students = [len(i) for i in students]
# print(students);
# students = [i.lower() for i in students]
# print(students);


##. 함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다")

# def deposit(balance, money):    # 입금
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance+money))
#     return balance+money

# def withdraw(balance, money):   # 출금
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance-money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commission = 100 # 수수료 100원
#     return commission, balance - money - commision  # 반납 값이 여러 개일 경우 튜플형태로 반환됨

# balance = 0
# balance = deposit(balance, 1000)
# commission, balance = withdraw_night(balance, 500)  

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}".format(name, age, main_lang))
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}".format(name, age, main_lang))

# profile("김기훈")
# profile("박경남", 20)

# def profile2(name, age, lang1, lang2, lang3):
#     print("이름 : {0}\t 나이 : {1}\t".format(name,age), end=" ")
#     print(lang1, lang2, lang3)

##. 가변인자
# def profile2(name, age, *language):
#     print("이름 : {0}\t 나이 : {1}\t".format(name,age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile2("김기훈", 27, "Python","java","C","Swift","Kotlin")
# profile2("박경남",20,"java")


##. 지역변수와 전역변수
gun = 10
def checkpoint(soldiers):
    global gun  # 전역공간의 gun을 사용하겠다.
    gun = gun - soldiers

def chcekpoint_ret(gun, soldiers):
    gun = gun - soldiers
    return gun

gun = chcekpoint_ret(gun, 2)
print("남은 총 {0}".format(gun))

