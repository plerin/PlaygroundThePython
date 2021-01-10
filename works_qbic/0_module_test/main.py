# from person import Person as p # 모듈에서 Person(class)를 p라는 변수로 사용하겠다

# con = p('콘',28,'부천시 원미구')
# con.greeting()

from calpkg import *    # calcpkg 패키지의 모든 변수, 함수, 클래스를 가져옴
 
# print(dir())
print(add(10, 20))    # operation 모듈의 add 함수 사용
print(mul(10, 20))    # operation 모듈의 mul 함수 사용
 
print(triangle_area(30, 40))    # geometry 모듈의 triangle_area 함수 사용
print(rectangle_area(30, 40))   # geometry 모듈의 rectangle_area 함수 사용