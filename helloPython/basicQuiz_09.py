#. Q. 치킨 자동 주문 시스템
'''
    조건 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때 ValueError 로 처리
    출력 메시지 : "잘못된 값을 입력하엿습니다."
    조건 2 : 치킨은 총 10마리, 치킨 소진시 사용자 정의 에러 SoldOutError를 발생, 프로그램 종료
    출력 메시지 : 재고가 소진되어 더 이상 주문을 받지 않습니다.

'''

# 숫자가 아닌걸 어떻게 판단하지? type(order) == 

class SoldOutError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

chicken = 10
waiting = 1

while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")
        elif order < 1:
            raise ValueError
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
            if chicken == 0:
                raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError as err:
        print("{0}".format(err))
        break

