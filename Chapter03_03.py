# Chapter 03-3
# 파이썬 리스트(List)
# 자료구조에 중요
# 리스트 자료형(순서, 중복, 수정, 삭제 모두 가능...)
"""
tuple <> List 차이점.

얼핏보면 튜플과 리스트는 비슷한 역할을 하지만 프로그래밍을 할 때 튜플과 리스트는 구별해서 사용하는 것이 유리하다.
튜플과 리스트의 가장 큰차이는 값을 변화시킬수 있는가 여부이다.
즉 리스트의 항목 값은 변화가 가능하고 튜플의 항목 값은 변화가 불가능하다.
따라서 프로그램이 실행되는 동안 그 값이 항상 변하지 않기를 바란다거나 값이 바뀔까 걱정하고 싶지 않다면 튜플을 사용해야한다.

- 리스트는 []으로 둘러싸이지만 튜플은 ()으로 둘러싸인다.
- 리스트는 그 값의 생성, 삭제 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.
- 튜플은 1개의 요소만 가질때는 요소뒤에 콤마 'ex) t1 = (1,)' 를 반드시 붙여야한다는 것과 t1 = 1, 2, 3처럼 괄호를 생략해도 무관하다. 
"""
print("Chapter 3-3")
print('')
# 선언
a = [] # 비어있는 리스트
print(type(a))

b = list()
c = [70, 75, 80, 85] # len
print(len(c))

d= [1000, 10000, 'Ace', 'Base', 'Captine'] # 서로 다른 자료형을 가진 데이터들을 담을 수 있다.
e = [1000, 10000, ['Ace', 'Base', 'Captine']] # 리스트 안의 리스트
f = [21.42, 'foobar', 3, 4, False, 3.141592]
print()

# 인덱싱 
# 원하는 데이터만 뽑아서 가져옴,
print('>>>')
print('d -',type(d), d)
print('d -', d[1])
print('d -', d[0] + d[1] + d[1])
print('d -', d[-1])
print('e -', e[-1])
print('e -', e[-1][1])
print('e -', list(e[-1][1])) # list 문자를 한글자씩 분리해서 표현해줌..
print('e -', type(e[-1][1]))

# 슬라이싱
print('>>>')
print('d -',d[0 : 3])
print('d -',d[2 : ])
print('e -',e[-1][1:3])

# 리스트 연산
print('>>>')
print('c + d', c + d) # list + list
print('c * 3', c * 3)
print("'Test' + c[0]", 'Test' + str(c[0]))


# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3])
print(c[3:])

print()
# Identity(id)
temp = c # 리스트도 하나의 주소값을 사용한다.
print(temp, c)
print(id(temp))
print(id(c))

# c = [70, 75, 80, 85] # len
# 리스트 수정, 삭제
print('>>>')
c[0] = 4
print('c -', c)
c[1:2] = ['a', 'b', 'c'] # list 안에 원소를 넣은것이고
print('c -', c)
c[1] = ['a', 'b', 'c'] # list 안에 리스트를 넣은것
print('c -', c)
c[1:2] = [['a', 'b', 'c']] # 리스트안에 리스트 넣기
print('c -', c)
c[1:3] = [] # 1부터 2개의 원소를 삭제한다.
print('c -', c)
del c[2] # c List의 2번째 원소를 삭제한다.
print('c -', c)

# 리스트 함수
print('>>>')
a = [5, 2, 3, 1, 4]
print('a -', a)
# a[5] = 10 이렇게 해서는 값이 추가되지 않는다
a.append(10) # append 는 마지막 인덱스에 값을 추가한다,
print('a -', a)

a.sort() # 오름차순 정렬
print('a -', a)

a.reverse() # 내림차순 정렬
print('a -', a)

print('a -', a.index(3), a[3]) # index로 가져오는 방법이 있지만 굳이 저렇게 사용 안해도됨...

a.insert(2,7) # a 의 2번째 자리에 7을 밀어넣을거야
print('a -', a)

a.sort() # 오름차순 정렬
print('a -', a)

a.reverse() # 내림차순 정렬
print('a -', a)

#del a[6] 데이터가 몇만개일수록 세어서 넣을수가 없다.
#print('a -', a)

a.remove(10) # 따라서 원하는 값을 사용하고 싶다면 remove 함수를 사용한다.
print('a -', a)

print('a -', a.pop()) # 마지막 리스트에 존재하는 값을 가져오고 삭제한다.

print('a -', a)

print('a -', a.count(4)) # 리스트의 값 양이 많을때 원하는 값의 갯수를 찾을때 사용한다.


# 삭제 : remove, pop, del

# 반복문 활용
while a: # 데이터가 비어있을때 까지 반복한다.
    data = a.pop()
    print(data)


