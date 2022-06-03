# Chapter03-4
# 파이선 튜플
# 리스트와 비교 중요
# 튜플 자료형( 순서O, 중복O, 수정X, 삭제X) # 불변\
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
# 선언 

a = ()
b = (1,) # 그냥 b = (1) 으로 선언하게 된다면 타입이 INT 형으로 인식하게됨.. 따라서 1개만 선언할경우 반드시 ',' 선언을 해줘야 한다.
c = (11, 12, 13, 14)
d = (100, 10000, 'Ace', 'Base', 'Captine')
e = (100, 10000, ('Ace', 'Base', 'Captine'))

#인덱싱
print('>>>')
print('d - ',d[1])

print('d - ',d[0] + d[1] + d[1])
print('d - ',d[-1])
print('d - ',e[-1])
print('d - ',e[-1][1])
print('d - ',list(e[-1][1])) # 튜플을 리스트로 형변환 시킴..

# 수정해보기..
# d[0] = 1500 에러 발생

# 슬라이싱

print('>>>')
print('d - ',d[0:3])
print('d - ',d[2:])
print('d - ',e[2][1:3])

# 튜플 연산
print('>>>')

print('c + d', c + d)
print('c * 3', c * 3)

# 튜플 함수
a = (5, 2, 3, 1, 4)

print('>>>')
print('a - ',a)
print('a - ',a.index(3)) # 숫자 3의 인덱스를 알려줌
print('a - ',a.count(2))

# 팩킹 & 언팩킹()

# Pcaking
print('>>>')
t = ('foo', 'bar', 'baz', 'qux')
print(t)
print(t[0])
print(t[-1])

# UnPacking 1
(x1, x2, x3, x4) = t #패킹된 데이터들을 풀어서 정의된 변수에 저장.
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# Packing & UnPacking1
t2 = 1, 2, 3 # t2 = (1, 2, 3)  
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = (4, 5, 6)

print('>>>')
print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)

