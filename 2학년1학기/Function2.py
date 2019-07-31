#p107

# n = random.randint(1,6)  #1 <= n <= 6 랜덤수 6도 포함 range는 6포함 ㄴㄴ
# print("6면 주사위 굴린 결과 : ",n)

# n = random.randint(1,6) 
# print("6면 주사위 굴린 결과 : ",n)

# n = random.randint(1,6) 
# print("6면 주사위 굴린 결과 : ",n)
#p109 ~ 112
import random
# def rolling_dice():
#     n = random.randint(1,6) 
#     print("6면 주사위 굴린 결과 : ",n)


# def rolling_dice(pip):
#     n = random.randint(1,pip)   #1<=n<=pip
#     print(pip,"면 주사위 굴린 결과 : ",n)

def rolling_dice(pip, repeat):
    for r in range(1,repeat+1):
     n = random.randint(1,pip)   #1<=n<=pip
     print(pip,"면 주사위 굴린 결과 : ", r , ":",n)

rolling_dice(6,1)
rolling_dice(5,3)
rolling_dice(12,-4)
rolling_dice(10,5)

def star():
    print("*"*5)

star()
star()
star()

#p113
print("♡")
print("♡","♪")
print("♡","♪","♣")
print("♡","♪","♣","♠")
print("♡","♪","♣","♠","★")

# def p(*args):   #튜플형식
#     string = ""
#     for a in args:
#         string += " "+a
#     print(string.strip())

# print("♡")
# print("♡","♪")
# print("♡","♪","♣")
# print("♡","♪","♣","♠")

#114
def p(space, space_num, *args):
    string = args[0]
    for i in range(1,len(args)):
        string += (space * space_num)+args[i]
    print(string)


p(",",3,"♥","♬")
p("★",2,"♥","♬","♣")
p("_",3,"♥","♬","♣","♠")

def star2(ch , *nums): # (*nums) 만 해도 ㄱㅊ음 numx[0]하면 돼서
  for i in range(len(nums)):
    print(ch*nums[i])

#range(len(nums)) range가 있으면 인덱스로 접근한다고 알기.
# for n in nums:  더 간단하게   
#     print(ch*n)

# def star2(*nums):  이것도 가능
#   for i in range(1,len(nums)):
#     print(nums[0]*nums[i])
star2("♪",3)
star2("♡",1,2,3)


def fn(a,b,c,d,e):
    print(a,b,c,d,e)

fn(1,2,3,4,5)
fn(10,20,30,40,50)
fn(5,6,7,8,9)
fn(a=1,b=2,c=3,d=4,e=5)
fn(e=5,d=4,c=3,b=2,a=1)
fn(1,2,c=3,e=5,d=4)
# fn(d=4,e=5,1,2,3)   1,2,3이 지정을 안해줘서 안쓸거면 앞에서 지정을 안해줘야됨 지정하기 시작하면 그 뒤는 쭉 해야함


def star3(mark, repeat, space, space_repeat,line):
  for _ in range(line):
    string = (mark * repeat) + (space * space_repeat)+(mark * repeat) # "*" * 3 + "_" * 2 + "*" * 3 
    print (string)
star3("*",3,"_",2,3)

#119
def hello(msg="안녕하세요") :
  print(msg+"!")

hello("하이")
hello("hi")
hello()  #기본 값 안녕하세요가 들어감

#p120
def hello2(name, msg="안녕하세요"):  
  print(name+"님,"+msg+"!")

hello2("김가영","오랜만이에요")
hello2("김선옥")
# hello2()  #에러name인자 없음

def fn2(a,b=[]):
  b.append(a)
  print(b)

fn2(3)  #[].append(3) => [3]
fn2(5)  #[].append(5) => [5]
fn2(10)
#fn2(7,[1]):    #[1,7]
 # print([1].append(7))


#123p
def gugudan(dan = 2):
  for i in range(1,9+1):
    #print(dan , "X", i ,"=", dan*i )
    print(str(dan) + "X" + str(i) + "=" +str(dan*i))   #띄어쓰기 없음
    
gugudan(3)    #3단출력
gugudan(2)    #2단출력
gugudan()     #2단출력

#125
def sum(*numbers):
  sum_value = 0
  for number in numbers:
    sum_value += number

  return sum_value
print("1 + 3 =",sum(1,3))
print("1 + 3 + 5 + 7 = ",sum(1,3,5,7))


def min(*numbers):
  min_value = numbers[0]
  for number in numbers:
    if min_value > number:
        min_value = number
  return min_value
print("min(3,6,-2) = ",min(3,6,-2))

def max(*numbers):
  max_value = numbers[0]
  for number in numbers:
    if max_value < number:
        max_value = number
  return max_value
print("max(3,6,-2) = ",max(3,6,-2))

def multi_num(multi,start,end):
  result = []
  for n in range(start, end):
    if n % multi == 0:
      result.append(n)
  return result
print("multi_num(17,1,200) = ",multi_num(17,1,200))   #16의 배수가 들어감
print("multi_num(3,1,100) = ",multi_num(3,1,100))     #3의 배수가 들어감


def min_max(*args):
  min_value = args[0]
  max_value = args[0]
  for a in args:
    if min_value > a:
        min_value = a
    if max_value < a:
        max_value = a
  return min_value,max_value

min,max = min_max(52,-3,23,89,-21)
print("최솟값:",min,"최댓값:",max)