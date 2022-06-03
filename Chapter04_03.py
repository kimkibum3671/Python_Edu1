# Chapter 04-3
# 파이썬 반복문
# while 실습
"""
whie <expression> :
    code...
"""

# 예제1
# 무한 반복을 주의해야한다.
n = 5
while n > 0:
    print(n)
    n -= 1

# 예제 2
a = ['foo', 'bar', 'baz']

while a: 
    print(a.pop()) # print(a.pop(-1)) 동일 결과

# 예제 3
# break, continue

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print("Loop End.")

#예제 4

m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
    
print("Loop End.")

# if 중첩
# 예제 5

i = 1
while i <= 10:
    print('i :', i)
    if i == 6:
        break
    i += 1


# while else
# 예제 6

n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out')

# 예제 7

a = ['foo', 'bar', 'baz', 'qux']
s = 'qux'

i = 0
while i < len(a):
    if a[i] == s:
        print('found a{} - "{}"'.format(i, a[i])) 
        break    
    i += 1
else:
    print('not found in list.')

# 무한 반복
# while True:
#   print('Foo')

# 예제 8
a = ['foo', 'bar', 'baz']
while True:
    if not a : # a가 False 이면 True로 변환되어 종료된다.
        break
    print(a.pop())