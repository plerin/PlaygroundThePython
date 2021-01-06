'''
크레온 plus 접속을 자동화하는 코드
coStart.exe 경로 id / pwd / pwdcert 변경필요
'''

from pywinauto import application
import time
import os

os.system('taskkill /IM coStarter* /F /T')
os.system('taskkill /IM CpStart* /F /T')
os.system('wmic process where "name like \'%coStarter%\'" call terminate')
os.system('wmic process where "name like \'%CpStart%\'" call terminate')
time.sleep(5)        

app = application.Application()
app.start('C:\dev\\0_TOOL\CREON\STARTER\coStarter.exe /prj:cp /id:PLERIN /pwd:con2@ /pwdcert:skshboris2@ /autostart')
time.sleep(60)