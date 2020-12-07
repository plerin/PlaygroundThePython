#. Q. 매주 1회 작성해야하는 보고서를 작성하시오.
'''
    - x 주차 주간보고 -
    부서 : 
    이름 : 
    업무 요약 :

    1주차~50주차까지 보고서 파일을 만드는 프로그램을 작성하시오

    조건 : 파일명은 '1주차.txt', '2주차.txt', .. 와 같이 만든다.

'''

for i in range(1,51):
    with open(str(i)+"주차.txt", "w", encoding="utf8") as report:
        report.write("- {0} 주차 주간보고 -".format(i))
        report.write("\n부서 : ")
        report.write("\n이름 : ")
        report.write("\n업무 요약 : ")
    report.close()

