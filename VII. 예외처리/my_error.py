# 219p
class OddError(Exception):
    def __init__(self,message = "홀수는 ㄴㄴ"):
        self.message = message

    def __str__(self):
        return self.message
    
n = 11
try:
    if n % 2 != 0:                  #에러발생
        raise OddError
    else:
        print("짝수에요. 짝짝짝")
except OddError as e:               #에러처리
    print(e)
