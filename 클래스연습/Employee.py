#Employee.p
#p.200
class Person:
    def __init__(self,name,age):  #init에서 변수가 그냥 만들어짐.
        self.name = name
        self.age = age

    def eat(self,food):   #생성자
        print(self.name+"가"+food+"을 먹습니다.")

    def __str__(self):  #특수함구
        return self.name + " 는 " + str(self.age)+"살입니다."  #self.name생성자 접근방법. 셀프를 왜 

class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)   #부모생성. 
        self.salary = salary

    def work(self):
        print("열심히 일을 합니다.")

    def get_salary(self):
        print("급료를 받습니다.")
        return self.salary

e= Employee("임현진",18,300)
print(e)
e.eat("에그타르트")
e.work()
r = e.get_salary()
print("급료는"+str(r)+"만원입니다.")