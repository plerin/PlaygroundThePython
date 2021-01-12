import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) # sys.path에 test_pkg 상위 폴더를 추가한다. == qbic_pkg를 추가하니까 하위 모든 패키지 사용할 수 있다.

from process.navigation import addZero as az

# print(os.path.dirname(__file__)) # os.path.dirname : __file__ 이 위치한 디렉토리 경로 얻기
# print(os.path.abspath(os.path.dirname(__file__))) # os.path.abspath : 경로의 절대경로 얻는다. 
# print(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))




con = az.func().getZero()

print(con)