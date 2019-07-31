User = input("숫자를 입력하세요")
#같은 글자를 옆에 바로 쓰고싶으면 짝*2

list = []
sum = 0
for a in User:
    list += a

for i in range(0, len(User)):
    sum += int(list[i])
print(sum)

# sum = 0
# for i in User:
#     sum += int(i)
# print(sum)
#  for문은 숫자를 적어도 문자열로 보기 때문에 한글자씩 꺼내서 int로바꾸고 sum 에 더함ㅂ34