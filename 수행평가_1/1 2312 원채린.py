majors = [
    ["뉴미디어 소프트웨어과","뉴미디어웹솔루션과","뉴미디어디자인과"],
    ["뉴미디어 소프트웨어과","뉴미디어웹솔루션과","뉴미디어디자인과"],
     ["인터랙티브미디어","뉴미디어디자인과","뉴미디어솔루션"]
    ]

    # for start
student_number = input("학번을 입력하세요")

grade = student_number[0:1]
grade = int(grade)
classroom = student_number[1]
classroom = int(classroom)
#//2를 하는 이유..

print(grade, "학년", majors[grade-1][(classroom-1)//2],student_number[1:2],"반",student_number[2:4],"번 입니다.")
print()
#반
#1,2 -1=>0,1=> 0
#3,4 -1=>2,3=>1
#5,6 -1=>4,5=>2