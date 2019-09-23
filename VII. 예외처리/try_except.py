l = [1,2,3]
try:
    print(l[2])
    print(l[3])       #IndexError: list index out of range 인덱스에러:리스트에 인덱스를 범위에서 벗어났다.
except:
    print("리스트의 요소에 접근하지 못했습니다.")

# print(l[3])
# print(l[2])

