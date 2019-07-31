#학번입력 받아서 학과 출력하기

majors = [
    ["뉴미디어 소프트웨어과","뉴미디어웹솔루션과","뉴미디어디자인과"],
    ["뉴미디어 소프트웨어과","뉴미디어웹솔루션과","뉴미디어디자인과"],
     ["인터랙티브미디어","뉴미디어디자인과","뉴미디어솔루션"]
    ]
    # for start
student_number = input("학번을 입력하세요")

grade = student_number[0]
grade = int(grade)
classroom = student_number[1]
classroom = int(classroom)

print(majors[grade-1][(classroom-1)//2])
#for end

#if grade == 1 or grade == 2 :
 #   print(majors12학년[classroom-1//2]) #/2를 하면 0.5로 되니까 //해야함.
#elif grade ==3 :
 #   print(majors3학년[classroom-1//2])


# if grade == "1" or grade == "2":
   # if classroom =="1" or classroom == "2":
        #  print("뉴미디어 소프트웨어과")

    #elif classroom == "3" or classroom == "4" :
     #   print("뉴미디어 웹솔류션과")
    #elif classroom == "5" or classroom == "6" :
     #   print("뉴미디어 디자인과")

# elif grade == "3" :
    #if classroom == "1" or classroom == "2" :
     #   print("인터랙티브미디어과")
    #elif classroom == "3" or classroom == "4" :
     #   print("뉴미디어 디자인과")
    #elif classroom == "5" or classroom == "6" :
     #   print("뉴미디어웹솔루션과")


#if x[0:1] == 3:
 #   if x[1:2] == 1 and x[1:2] ==2:
  #      print("인터랙티브 미디어과")
   # elif x[1:2] == 3 and x[1:2] == 4:
    #    print("뉴미디어 디자인과")
    #elif x[1:2] == 5 and x[1:2] == 6:
     #   print("뉴미디어 솔루션과")

#if x[0:1] == 1 or x[0:1] == 2:
    #if x[1:2] == 1 and x[1:2] == 2 :
     #   print("뉴미디어 소프트웨어과")
    #elif x[1:2] == 3 and x[1:2] == 4:
     #   print("뉴미디어 웹솔루션과") 
    #elif x[1:2] == 5 and x[1:2] == 6:
     #   print("뉴미디어 디자인과")
