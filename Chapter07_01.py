# Chapter 07-1
# 파이썬 예외처리의 이해
"""
예외종류 [SyntaxError(문법 에러), TypeError, NameError(없는 변수 참조), IndexError, ValueError, KeyError...]
  : 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계)에서 발생하는 예외도 중요

1. 예외는 반드시 처리.
2. 로그는 반드시 남긴다.
3. 예외는 던져진다.(다른곳으로 처리를 위임할 수 있다.)
4. 예외 무시(추천X)

"""
"""
# 1. Sysntax Error : 문법 오류
print('error)
print('error'))
if True
   pass
"""


"""
 # 2. NameError : 참조 없음

 a = 10
 b = 15
 print(c)
"""

"""
# 3. ZeroDivisionError

a = 100 / 0

"""

"""
4. IndexError
x = [1, 2, 3]
print(x[5])

print(x.pop())
print(x.pop())
print(x.pop())
print(x.pop())

"""

"""
# 5. KeyError

dict = {'name':'Lee', 'Age' : 41}
print(dict['hobby'])
"""

# 예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리 권장(EEAFP)


"""
#6. AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
import time
print(time.time2()) 속성에 존재하지 않는 함수, 변수를 호출한다.
"""

"""
# 7. ValueError

x = [10, 50, 90]
x.remove(50)
print(x)
x.remove(200)

"""


"""
# 8. FileNotFoundError : 없는 파일을 불러온다.
f = open('test.txt')

"""


"""
# 9. TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
x = [1, 2]
y = (1, 2)
z =  'test'

print(x + y) 
print(x + list(y)) >> 이런식으로 강제 형변환을 통해 진행해야한다.

"""




