import os

answer=input("1.새로운 목표작성하기  2.내 목표 불러오기 \n")

if int(answer)==1:

    while True:
        print("※본인의 이름을 파일명으로 해주세요※")
        filename = input("파일명을 입력하세요(exit입력시 종료) :")

        if filename == 'exit':  # 반복문을 빠져나오는 조건문

            print("one_List 서비스를 종료합니다..\n")
            
            break

        elif os.path.exists(filename):  # 파일 있을 때 에러발생

            print("파일이 존재합니다. 다시입력해 주세요\n")

            continue

        else:  # 파일이 없으면 생성

            f = open(filename,"w",encoding="utf8")

            string = input("본인의 목표를 작성해 주세요:")

            f.write(string)

            f.close()

            print("파일이 생성되었습니다.\n")

elif int(answer)==2:
        while True:

            file = input("불러올 파일명을 입력하세요(exit입력시 종료):")

            if file == 'exit':  # 반복문을 빠져나오는 조건문

                print("종료합니다.\n")
                print("첫 메뉴로 돌아갑니다...\n")
                break

            elif os.path.exists(file):

                f = open(file, "r",encoding="utf8")
                text = f.readlines()
                print(text)
                print("\n")
                f.close()

                f = open(file,"a+",encoding="utf8")
                moc = input("목표를 이루기 위하여 해야할 일 3가지를 사용하여 적어주세요(,로 구분)")
                f.write(moc)
                f.close()
                print("파일이 저장되었습니다.\n")
                
            else:
                print("해당파일이 존재하지않습니다... 다시입력해 주세요\n")
                continue

# 목표를 적은 글과 해야할 일 3가지 적은 글 구분하기
# 한 5초가 지나면 실천했냐고 물어보고 Y면 삭제하고 N 면 계속 남기기