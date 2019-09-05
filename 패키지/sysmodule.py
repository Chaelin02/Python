import sys

print("실행 파일명 : ", sys.argv[0])   #.argv[0]는 우리가 입력을 안해도 기본적으로 출력이 된다. 
for i in range(1, len(sys.argv)):    #1부터 argv만큼 반복해라
    print("옵션",i,":",sys.argv[i])

# 하는 법 sysmodule 오른쪽 Open in terminal 누르고 터미널에서 python sysmodule.py 머 머 머 머 
sys.exit()

for i in range(1,100):
    print("여기는 실행되지 않습니다.")



    # dir은 도스 명령어임