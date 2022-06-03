# Chapter 02-2
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
from typing import TypeVar


n = 700

#출력
print(n)
print(type(n)) #type(n) : n의 자료형을 알려준다.

#동시선언
x = y = z = 700
print(x, y, z)

# 선언
var = 75

# 재선언
var = "Change Value"

#출력
print(var)
print(type(var))

# Object References
# 변수 값이 할당된 상태일때

# 1. type에 맞는 오브젝트를 생성
# 2. 값 생성
# 3. 콘솔 출력


# 예1)
print(int(300)) # int형으로 300을 만들고 콘솔로 출력해준다.
print(300) # 위 과정 생략됨..

# 예2)
# n -> 777
n = 777

print(n, type(n))
print()

m = n
print(m , n)
print(type(m), type(n))

# id(identity) 확인 : 객체의 고유값 확인(포인터와 같은 개념의 주소)

m = 800
n = 600

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

m = n = z = i =800 # 똑같은 하나의 인스턴스로 생성함(하나의 객체로 사용함). 파이썬 엔진이 굳이 분리해서 변수를 관리할 필요 없다.
print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 다양한 변수 선언
# Camel Case : numberOfColleageGraduate, 처음에 소문자로 시작하고 단어마다 대문자로 시작함.(주로 함수명 선언시 사용함)
# Pascal Case : NumberOfColleageGraduate, 처음부터 대문자로 시작하며 단어마다 대문자로 시작함.(주로 클래스 선언시 사용함)
# Snake Case : number_of_colleage_graduates, 전단어 모두 소문자로 하며 뱀처럼 '_'으로 연결한다.(주로 변수명에서 사용함)

# 허용하는 변수 선언법

age = 1
Age = 1
aGe = 1
AGE = 1 
a_g_e = 1
_age = 1
age_ = 1
_AGE = 1


# 예약어는 변수명으로 불가능
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pass	
"""
# for = 3 / as = 3 / class = 3, python reserved word

