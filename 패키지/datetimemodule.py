from datetime import datetime

print('현재 날짜 시각 객체 얻기')
today = datetime.now()
print('today = datetime.now() :',today)
print('연 ,월 ,일 :',today.year, today.month, today.day)
print('시, 분 ,초 :', today.hour,today.minute,today.second)
print('요일 : ',today.weekday())
print('특정 날짜 시각 개체 만들기')
day = datetime(2019,1,1,0,0,0)
print('day = datetime(2019,1,1,0,0,0) :',day)
print('2019년 부터 지나온 시간 구하기')
print('today - day :',today - day)

#내가 태어난 날 무슨 요일?
brithday = datetime(2002,6,22,0,0,0)
print("가나다"[0])
print('월화수목금토일'[brithday.weekday()],"요일")

#나는 며칠 살았을까?
print('today - brithday :', day - brithday)

#올애 2019의 크리스마스 며칠 남았을까?
christmas= datetime(2019,12,25,0,0,0)
print(christmas - today)