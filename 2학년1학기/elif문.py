Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = int(input())
10
>>> if
SyntaxError: invalid syntax
>>> if X % 2 ==0:
	print("짝수")
else:
	print("홀수")

	
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    if X % 2 ==0:
NameError: name 'X' is not defined
>>> if x % 2 ==0:
	print("짝수")
else:
	print("홀수")

	
짝수
>>> password = input()
암호
>>> if password == "암호";
SyntaxError: invalid syntax
>>> if password == "암호":
	print("언락")
else:
	print("락")

	
언락
>>> password == input()
1234
False
>>> if password == "암호":
	print("언락")
else:
	print("락")

	
언락
>>> password == input()
1234
False
>>> x = int(input())
30
>>> if x % 4 == 0:
	print("4의 배수")
elif x % 3 == 0:
	print("3의 배수")
elif x % 2 == 0:
	print("2의 배수")

	
3의 배수
>>> x = int(input())

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    x = int(input())
ValueError: invalid literal for int() with base 10: ''
>>> x = int(input())
18
>>> if 10 <= x < 20:
	print("10대")
elif 30 <= x <40 :
	print("30대")
elif :
	print("10 , 30대가 아님")
	
SyntaxError: invalid syntax
>>> if 10 <= x < 20:
	print("10대")
elif 30 <= x <40 :
	print("30대")
else :
	print("10 , 30대가 아님")

	
10대
>>> x = int(input())
18
>>> if x > 10 and x % 2 ==0:
	print("10 초과 짝수")

	
10 초과 짝수
>>> x = int(input())
17
>>> if x > 10:
	if x % 2 == 0:
		print("10초과 짝수")
	else :
		print("10 초과 홀수")
else:
	print("10이하")

	
C
>>> x = float(input())
80.3
>>> if x >= 90.5 :
	print("A")
elif x >= 80.5:
	print("B")
elif x >= 70.5:
	print("C")
else :
	print("F")

	
C
>>> 80.5
80.5
>>> x = float(input())
80.5
>>> if x >= 90.5 :
	print("A")
elif x >= 80.5:
	print("B")
elif x >= 70.5:
	print("C")
else :
	print("F")

	
B
>>> if 90 < x <= 100 :
	print("A")
elif 80 < x <= 90 :
	print("B")
elif 70 < x <= 80 :
	print("C")
elif x < 70:
	print("F")

	
B
>>> x = float(input())
80.3
>>> if 90 < x <= 100 :
	print("A")
elif 80 < x <= 90 :
	print("B")
elif 70 < x <= 80 :
	print("C")
elif x < 70:
	print("F")

	
B
>>> 
