# Chapter04-2
# 파이썬 반복문
# for 실습

# 코딩의 핵심
"""
모든 자료형은 for문에서 사용할수 있다.
for in <collection> # collection은 집합의 모음.. 튜플 딕셔너리 리스트 등...
    <loop body>
"""

from binhex import REASONABLY_LARGE


for v1 in range(10): # 0 ~ n-1 까지 진행됨
    print('v1 is :', v1)

print()

for v2 in range(1, 11): # 1 부터 10까지 진행됨...
    print('v2 is :', v2)

print()

for v3 in range(1, 11, 2): # 1부터 10까지 2개 점프하면서 진행
    print('v3 is :', v3)

# 1 ~ 1000 까지의 합
sum1 = 0
for v4 in range(1, 1001):
    sum1 += v4
print('1 ~ 1000 sum :', sum1) # 들여쓰기 하면 for에 걸리는거고 아니면 한번만 진행됨..

print('1 ~ 1000 sum :', sum(range(1,1001)))

print('1 ~ 1000 4의 배수의 합 :', sum(range(4, 1001, 4)))
"""
Iterables(사전적 의미 : "반복가능한") 반복할수있는 객체를 뜻함, 자료형 반복
Iterable 대표적인 자료형 : 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
iterable 객체 종류(리턴 함수) : 
  - range(범위)
  - reversed(역순)
  - enumerate : 반복문 사용 시 몇번째 진행되는 반목문인지 인덱스 번호와 원소를 tuple 상태로 반환하는 함수.
  - filter : 
  - map
  - zip
  ...

"""
# 예제1 (List 붙이기)
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']
for name in names:
    print('You are : ', name)


# 예제2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print("Current number :", n)

# 예제3 (string 붙이기)
word = "Beautiful"
for s in word:
    print('word :', s)

# 예제 4 (dictionary 붙이기)
my_info = {
    "name" : "Lee",
    "Age" : 33,
    "City" : "Seoul"
}

for k in my_info:
    print('key :', k) # Key 값만 출력됨.
    print('key :', my_info[k]) # 속성으로 가져옴.., 단 정확해야하며 없는 속성값을 조회할경우 error 반환
    print('key :', my_info.get(k)) # get 함수로 가져옴.., 없어도 Error 반환하지 않음..

for v in my_info.values():
    print('values :', v)

# 예제5
name = 'PineApplE'

for n in name:
    if n.isupper(): # 대문자 확인
        print(n)
    else: # 소문자일 경우
        print(n.upper()) # 대문자로 변환


# break 구문 : break 만나면 반복문을 종료해버린다.

numbers = [14, 3, 4, 6, 7, 10, 55, 56, 20, 34, 36, 38 ]

for num in numbers:
    if num == 34:
        print('Found : 34 !!')
        break
    else:
        print('Not Found : ',num)

 # continue

lt = ["1", 2, 5, True, 3.14, complex(4)]

for v in lt:
    if type(v) is bool: # 자료형 대조할때는 is 를 사용한다.
        continue # 위 조건이 해당된다면 아래구문을 Skip 시킴..
    print("current type:", v, type(v))
    print("multiply by ", v * 2)



# for - else 구문

numbers = [14, 3, 4, 6, 7, 10, 55, 56, 20, 34, 36, 38]

for num in numbers:
    if num == 24:
        print("Find 24")
        break
else: # 반복문을 통해 조건문을 실행하였지만 해당 조건을 만족하지 못한다면 else 구문을 사용한다.
    print('Not Found 24')


# 구구단 출력

for i in range(2, 10):
    for j in range(1,10):
        print('{:4d}'. format(i*j), end='')
    print()

# 변환 예제
name2 = 'Aceman'

print('Reversed', reversed(name2)) # 해당 값에 대한 ID 값이 출력됨.
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', tuple(set(name2))) # 순서 X, 중복은 안되지만 소문자는 분류한다.