# Chapter03-6
"""
파이썬 집합이란?
 - 집합에 관련된 것을 처리하기 위해 만들어진 자료형이다.
 - 수학시간에 배웠던 집합의 특징들을 메서드 혹은 연산자를 통해서 구할 수 있게 만들어져있다.
 - 
"""
# 집합(Set) 특징
# 집합(Set) 자료형(순서X, 중복X), 중복을 허용하지 않고 순서를 보장하지 않는다. 

# 선언
a = set()
b = set([1,2,3,4,4,4,4]) # List 형식으로도 넣을수 있다./ 중복'4' 는 허용하지 않는다.
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'} # dictonary 형식으로 들어갈수도 있으며, Key가 없이 원소만 넣어도 Set형태가 된다.,
f = {42, 'foo', (1, 2, 3), 3.14159} # 괄호로도 사용할수 있다. Key가 없으면 집합으로 볼수있다..

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 튜플 변환(set -> tuple)
t = tuple(b)
print('t -', type(t), t)
print('t - ', t[0], t[1:3])

# 리스트 변환(set -> list)
l = list(c)
l2 = list(e)

print('l -', type(l),l)
print('l2 -', type(l2), l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2 :', s1 & s2) # 교집합
print('s1 & s2 :', s1.intersection(s2)) # 교집합

print('s1 | s2', s1 | s2) #  합집합
print('s1 | s2', s1.union(s2)) #  합집합

print('s1 - s2', s1 - s2) # 차집합
print('s1 - s2', s1.difference(s2))  # 차집합


# 중복 원소 확인
print('s1 & s2', s1.isdisjoint(s2)) # 중복되는것이 있는가? True : 교집합 되는것 없음, False : 교집합 되는것 있음.. 왜냐하면 dis이기때문에 반대로 나온다.

# 부분 집합 확인
print(s1.issubset(s2)) # s1이 s2의 부분집합이냐.. 두집합은 서로가 어떠한 집합에 귀속되는 집합이 아니기 때문에 False 를 반환한다.
print(s1.issuperset(s2)) # s1이 s2를 포함하는 집합인지.. 이또한 위와 같다.

# 추가 & 제거
s1 = set([1, 2, 3, 4])
print('s1 - ', s1) 
# List 에서는 데이터 삽입을 append, insert 등 있지만..
# Set에서는 Method 가 있다.

s1.add(5)
print('s1 - ', s1)

s1.remove(2)
print('s1 - ', s1)

# s1.remove(10) # 없는 원소를 삭제한다면 Key Error 발생함.
s1.discard(3)
print('s1 - ', s1)

s1.discard(7) # remove 는 없는 수를 삭제할경우 Error 가 발생하지만, discard 는 에러 발생을 시키지 않음.. 딕셔너리에서 get 함수와 느낌이 비슷..
print('s1 - ', s1)

s1.clear() # 모든 원소 삭제..
print('s1 - ', s1)
