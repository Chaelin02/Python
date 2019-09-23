f = open("file.txt","w")

try:
    f.write("Hello world")
    f.write(100)      # f.write("100") 문자열은 에러..?
except TypeError:
    print("타입 예외 ,발생( 100 을 쓸수 없음)")
finally:
    print("예외 여부와 상관없이 무조건 실행")
    f.close()
