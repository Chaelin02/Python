User = input("숫자를 입력하세요")
#같은 글자를 옆에 바로 쓰고싶으면 짝*2

list = []
sum = 0
for a in User:
    list += a

for i in range(0, len(User)):
    sum += int(list[i])
print(sum)