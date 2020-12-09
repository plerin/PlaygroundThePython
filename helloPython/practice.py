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
# gun = 10
# def checkpoint(soldiers):
#     global gun  # 전역공간의 gun을 사용하겠다.
#     gun = gun - soldiers

# def chcekpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     return gun

# gun = chcekpoint_ret(gun, 2)
# print("남은 총 {0}".format(gun))

##. 표준입출력
# import sys
# print("Python", "Java" , "Javascript", sep=",", end="?") 
# print("Python", "Java" , "Javascript", file=sys.stdout) 
# print("P:ython", "Java" , "Javascript", file=sys.stderr) 
# print("무엇이 더 재미있을까요?")

# 시험 성적, ljust, rjust
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순서표
# 001, 002, 003, ...
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3))        #. 3크기만큼 채우기 빈 칸은 0으로 채워

# answer = input("아무 값이나 입력하세요 : ")     #. 항상 문자열로만 받아와
# print("입력하신 값은 " + answer + "입니다")


##. 다양한 형태의 포맷
# print("{0: >10}".format(500))

# #. 양수일 땐 +, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))

# #. 왼쪽정렬, 빈칸을 _로 채움
# print("{0:_<+10}".format(500))

# #. 3자리마다 콤마를 찍어주기
# print("{0:,}".format(1000000000000))

# #. 3자리마다 콤마를 찍어주기
# print("{0:+,}".format(-1000000000000))

# #. 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기, 빈자리는 ^로 채워주기
# print("{0:^<+30,}".format(1000000000000))

# #. 소수점 출력
# print("{0:f}".format(5/3))

# #. 소수점 특정 자리수 까지만 표시
# print("{0:.2f}".format(5/3))


##. 파일 입출력
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# for i in range(0,4):
#     print(score_file.readline(), end="") # 줄 별로 읽기 동작 수행, 한 줄읽고 커서는 다음 줄로 이동

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()

# for line in lines:
#     print(line, end="")

# score_file.close()


##. pickle -> 데이터를 pickle로 저장하고 이를 통해 load 해서 사용할 수 있도록 
import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름": "박명수", "나이":30, "취미":["축구","골프","야구"]}
# print(profile)

# pickle.dump(profile, profile_file)  # profile의 정보를 file에 저장

# profile_file.close()

# profile_file = open("profile.pickle", "rb") 
# profile = pickle.load(profile_file) # file에 있는 정보를 profile 에 불러오기
# print(profile)

# profile_file.close()


##. with 따로 닫아줄 필요 없다(close) 

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고있어요")

# with open("study.txt" , "r", encoding="utf8")


##. 클래스

# # 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# name = "마린"
# hp = 40
# damage = 5

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력{1}\n".format(hp,damage))

# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있으며 일반모드 / 시즈모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력{1}\n".format(tank_hp,tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)

# class Unit:
#     def __init__(self, name, hp):       # 생성자
#         self.name = name
#         self.hp = hp

# marine1 = Unit("마린",40, 5)    # marine1 = instance
# marine2 = Unit("마린",40, 5)
# tank = Unit("탱크", 150, 35)

# wraith1 = Unit("레이스", 80, 5)

# wraith2 = Unit("빼앗긴 레이스", 80, 5)
# wraith2.clocking = True     # 클래스 외부에서 메소드 확장할 수 있고 기존 클래스로 만든 인스턴스에는 적용이 안된다.

# if wraith2.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# from random import *

# class Unit:
#     def __init__(self, name, hp, speed):       # 생성자
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name,location, self.speed))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))    

# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):       # 생성자
#         Unit.__init__(self,name,hp,speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)
    
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않았습니다.".format(self.name))

# class Tank(AttackUnit):
#     seize_develped = False

#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_develped == False:
#             return
        
#         if self.seize_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *= 2
#             self.seize_mode = True
#         else:
#             print("{0} : 시즈모드로 해제합니다.".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False

#     def clocking(self):
#         if self.clocked == True:
#             print("{0} : 클로킹 모드 해제합니다.".format(self.name))
#             self.clocked = False
#         else:
#             print("{0} : 클로킹 모드 설정합니다.".format(self.name))
#             self.clocked = True

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     print("Player : gg")
#     print("[Player] 님이 게임에서 퇴장하셨습니다.")

# # 실제 게임 진행
# game_start()

# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# t1 = Tank()
# t2 = Tank()

# w1 = Wraith()

# # 유닛 일괄 관리
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")

# Tank.seize_develped = True
# print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()

# # 전군 공격
# for unit in attack_units:
#     unit.attack("1시")

# for unit in attack_units:
#     unit.damaged(randint(5,21))

# # 게임 종료
# game_over()


# try:
#     print("나누기 전용 계산기입니다")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 :")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 :")))
#     nums.append(int(nums[0]  / nums[1])))

#     print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
# except ValueError:
#     print("에러! 잘못된 값을 입력했습니다.")
# except ZeroDivisionError as err:
#     print(err)

# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg


# try:
#     print("한 자리 숫자 나누기 전용 계산기")
#     num1 = int(input("첫 번째 숫자를 입력하세요"))
#     num2 = int(input("두 번째 숫자를 입력하세요"))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력 값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력했습니다.")
# except BigNumberError as err:
#     print("에러가 발생했습니다. 한 자리 숫자만 입력하세요")
#     print(err)
# finally:
#     print("계산기를 이용해주셔서 감사합니다.")

##. 모듈(module)

# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(3)

# import theater_module as mv
# mv.price(3)
# mv.price_morning(3)
# mv.price_soldier(3)

# from theater_module import *
# price(3)
# price_morning(3)
# price_soldier(3)

# from theater_module import price, price_morning

# price(3)
# price_morning(3)
# price_soldier(3)

# from theater_module import price_soldier as price
# price(5)


# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from travel import *
# # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# dir : 어떤 객체를넘겨줬을 대 그 객체가 어떤 변수오 ㅏ함수를 갖고있는지 표시

# glob : 경로 내의 폴더 / 파일 목록 조회

# import glob
# print(glob.glob("*.py"))    # 확장자가 .py인 모든 파일

# import os
# print(os.getcwd())

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())

today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은", today+ td)