from tkinter import *

root = Tk()
root.title("CON GUI")   # 창 이름
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="gui_basic/image.png")
label2 = Label(root, image=photo)
label2.pack()



root.mainloop() # 창이 닫히지 않도록 설정
