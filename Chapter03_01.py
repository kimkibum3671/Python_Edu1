# Chapter 03-1
# 숫자형

# 파이썬 지원 자료형
"""
int : 정수형
fload : 실수형
complex : 복소수
bool : boolean
str : 문자열(시퀀스 : 순서가 있는것)
list : 리스트(시퀀스 : 순서가 있는것, 값 변화O)
tuple : 튜플(시퀀스 : 순서가 있는것, 값 변화X)
set : 집합
dict : 사전

---------------------
tuple <> List 차이점.

얼핏보면 튜플과 리스트는 비슷한 역할을 하지만 프로그래밍을 할 때 튜플과 리스트는 구별해서 사용하는 것이 유리하다.
튜플과 리스트의 가장 큰차이는 값을 변화시킬수 있는가 여부이다.
즉 리스트의 항목 값은 변화가 가능하고 튜플의 항목 값은 변화가 불가능하다.
따라서 프로그램이 실행되는 동안 그 값이 항상 변하지 않기를 바란다거나 값이 바뀔까 걱정하고 싶지 않다면 튜플을 사용해야한다.

- 리스트는 []으로 둘러싸이지만 튜플은 ()으로 둘러싸인다.
- 리스트는 그 값의 생성, 삭제 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.
- 튜플은 1개의 요소만 가질때는 요소뒤에 콤마 'ex) t1 = (1,)' 를 반드시 붙여야한다는 것과 t1 = 1, 2, 3처럼 괄호를 생략해도 무관하다. 
"""

# 데이터 타입
from ctypes import BigEndianStructure
from turtle import Turtle


str1 = "Python"
bool = True
str2 = 'Anaconda'
float_v = 10.0 # 10.0 != 10
int_v = 7
list = [str1, str2]
dict = {
    "name":"Machine Learning", #"Machine Learning"(내용)을 꺼내기 위해서는 "name"(key)을 찾아야한다.
    "version" : 2.0 # '2.0'을 찾기 위해서는 "version"을 찾아야한다.
}
tuple = (7, 8, 9) 
set = {7, 8, 9}
test = (1) # 그냥 int으로 간주..

#데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))
print(type(test))

# 숫자형 연산자
"""
+
-
*
/ : 나누기
// : 몫 만 반환
% : 나머지
abs(x) : 절대값
power(x,y), x**y : x의 y제곱
"""

# 정수선언
i = 77;
i2 = -14
big_int = 77777777777777777777788888888888888888 # 큰수도 알아서 할당해서 갖고있는다


# 정수 출력
print(i)
print(i2)
print(big_int)
print()

# 실수 출력
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9
print(f)
print(f2)
print(f3)
print(f4)
print()

# 연산 실습
i1 = 39
i2 = 939
big_int = 777777777777777779999999999999999999
big_int2 = 88888888888888889999999999999999999
f1 = 1.234
f2 = 3.939

# +
print(">>>>+")
print("i1 + i2 : ", i1 + i2)
print("f1 + f2 : ", f1 + f2)
print("big_int1 + big_int2", big_int + big_int2)

#서로 다른형을 계산할 경우 형변환이 이루어짐
typecheck = 1 + 2.0
print(type(typecheck))

# *
print(">>>>+")
print("i1 * i2 : ", i1 * i2)
print("f1 * f2 : ", f1 * f2)
print("big_int1 * big_int2 : ", big_int * big_int2)

# 형 변환 실습
a = 3. # 3.0을 의미
b = 6
c = .7 # 0.7을 의미
d = 12.7
print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(type(a), type(b), type(c), type(d))

#형 변환
print(float(b)) # 실수형으로 형변환
print(int(c))
print(int(d)) # 정수형으로 형변환
print(int(True)) # True : 1, False : 0
print(float(False))
print(complex(3)) 
print(complex('3')) # 문자형 -> 숫자형 -> 복소수형 형변환
print()

# 수치 연산 함수
print(abs(-7))
x,y = divmod(100, 8) # 몫 과 나머지를 한번에 저장시켜줌
print(x,y)
print(pow(5,3), 5**3) # 5의 3제곱
print()

# 외부 모듈
import math # 외부에서 끌어서 쓰는것.

print(math.pi) # math에 있는 pi값을 가져와서 쓴다.
print(math.ceil(5.1)) # x이상의 수 중에서 가장 작은 정수, 즉 여기서는 6을 출력해줌.




