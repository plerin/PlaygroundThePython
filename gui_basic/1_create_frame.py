from tkinter import *

root = Tk()
root.title("CON GUI")   # 창 이름
root.geometry("640x500")    # 창 크기
# root.geometry("640x500+100+300")    # 가로 * 세로 + x좌표 + y좌표
root.resizable(False, False)    # x(너비), y(높이) 값 변경 불가 (창 크기 불가)





root.mainloop() # 창이 닫히지 않도록 설정
