# Chapter 06-1
# 파이썬 클래스
"""
OOP(객체 지향 프로그래밍), self, 인스턴스 매소드, 인스턴스 변수

클래스('붕어빵틀') and 인스턴스('만들어진 붕어빵') 차이 이해

클래스란?
 1. 사용 목적 : 변수와 함수를 묶어서 하나의 새로운 객체(타입)으로 만드는것.
 2. '정의' 의미 : 새로운 데이터 타입을 정의하는 것. 이를 실제로 사용하려면 인스턴스를 생성해야 한다.
 3. self 의미 : 클래스 내에 정의된 self는 클래스 인스턴스임(클래스 주소 == self 주소)을 알 수 있다.

네임스페이스 : 객체를 인스턴스화 할 때 자기만의 저장된 공간
클래스 변수 : 직접 접근 가능, 모든 인스턴스가 공통으로 갖는 변수값
인스턴스 변수 : 객체마다 별도 존재

"""

# 예제1
class Dog(object): # class Dog() 이렇게 선언해도된다. 어차피 object를 상속 받는다.
    # 클래스 속성
    species = 'firstdog' # 인스턴스마다 같은 값 공유

    # 초기화/인스턴스 속성
    def __init__(self, name, age): # 인스턴스마다 선언된 다른값을 가짐.
        self.name = name
        self.age = age

# 클래스 정보 출력
print(Dog)

# 인스턴스화
a = Dog("Mikky", 2)
b = Dog("Baby", 3)
c = Dog("Baby", 3) # b와 다른 인스턴스. 또다른 객체를 생성한것임!!

#  비교
print(a == b, id(a), id(b), id(c))

# 네임스페이스 (각각의 인스턴스가 갖고있는 속성값을 확인할수 있다.)
print('dog', a.__dict__) # dictionary 형태를 갖는다.
print('dog', b.__dict__)

 # 인스턴스 속성 확인 및 접근
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.age))

print(Dog.species) # 공유하는 공간도 갖고있다.
print(a.species)
print(b.species)
print(Dog.species == a.species == b.species) # id가 같음..


# 예제2
# self의 이해
# self가 붙으면 나만의 속성을 갖는다는 뜻

class SelfTest:
    
    def func1(): # 클래스 메소드
        print('Func1 Called')
    
    def func2(self): # 인스턴스 메소드. 인스턴스 고유의 속성값 부분.
        print(id(self))
        print("Func2 Called")
    
    """
    아래 초기화 함수가 없다면 클래스가 알아서 내부적으로 생성해서 진행함..
    def __init__(self) -> None:
        pass
    """
    
f = SelfTest()

# print(dir(f)) dir 함수로 클래스 내부를 드려다봄.
print(id(f))
"""
f.func1() 오류..
>> 함수가 self 로 정의되지 않았다면 f의 인스턴스 객체에 대한 id 값이 입력되지 않아 오류남.
>> 따라서 진행하기 위해서는 클래스에서 직접 접근해야함.
>> SelfTest.func1()

f.func2() 정상..
>> self로 입력받은 함수로 구성되어있다면, f 인스턴스 객체의 id 값이 self로 들어가서 동작하게됨..

SelfTest.func2() 오류..
>> self 입력값에 매개변수 id가 입력되어야 하는데 인스턴스가 아닌 클래스로 바로 접근하였기에 오류가 발생한다.

"""
#f.func1()
f.func2()

SelfTest.func1()
SelfTest.func2(f)

# 예제3
# 클래스 변수, 인스턴스 변수
class WareHouse:
    # 클래스 변수
    stock_num = 0 # 재고
    def __init__(self, Name):
        # 인스턴스 변수
        self.name = Name
        WareHouse.stock_num += 1
    
    def __del__(self): # 클래스가 소멸할떄
        WareHouse.stock_num -= 1

user1 = WareHouse('Lee')
user2 = WareHouse('Cho')

print(WareHouse.stock_num) # 붕어빵 기계로 두번 구웠음.
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(WareHouse.__dict__)
 

del user1
print('>> after', WareHouse.__dict__)

# 예제 4

class Dog(object): # class Dog() 이렇게 선언해도된다. 어차피 object를 상속 받는다.
    # 클래스 속성
    species = 'firstdog' # 인스턴스마다 같은 값 공유

    # 초기화/인스턴스 속성
    def __init__(self, name, age): # 인스턴스마다 선언된 다른값을 가짐.
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return '{} says {} !!'.format(self.name, sound)

# 인스턴스 생성
c = Dog('Jully', 4)
d = Dog('Marry', 10)
# 메소드 호출
print(c.info())

print(c.speak('Boo Boo'))
print(c.speak('Mung Mung'))


