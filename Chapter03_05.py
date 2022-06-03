# Chapter03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서X, 키 중복X, 수정O, 삭제O)

# 선언(Key : Value 으로 구성)
# a = {'name' : 'Kim', 'name' : 'LEE'} 중복 안됨.
a = {'name' : 'Kim', 'phone' : '01012312314', 'birth' : '911116'}  
b = {0 : 'Hello Python'} # 키는 숫자로도 사용 가능..
c = {'arr' : [1, 2, 3, 4]} # Value 는 어떤것도 가져올수 있다.
d = {
    'Name' : 'Niceman',
    'City' : 'Seoul',
    'Age' : 33,
    'Grade' : 'A',
    'Status' : True
}

# 튜플로도 사용함
e = dict([  # 리스트안에 튜플방식으로 넣지만.. 잘 사용X
    ('Name','Niceman'),
    ('City','Seoul'),
    ('Age', 33),
    ('Grade', 'A'),
    ('Status', True)

]) # 잘 사용하지는 않음

f = dict(
    Name = 'NiceMan',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True
)
# d, f 방법으로 주로 사용한다!!!!!!

print('a -', type(a), a)
print('b -', type(b), b)
print('c -', type(c), c)
print('d -', type(d), d)
print('e -', type(e), e)
print('f -', type(f), f)
print()
# 출력
#print('a - ', a['name']) 확실할 경우는 속성으로 접근하지만, 키 존재하지 않는다면 에러를 발생시키며
print('a.get(\'name\') - ', a.get('name')) # 키 존재여부를 확인하기 위해 get을 주로 많이 사용한다. 키 존재하지 않으면 None 으로 처리
print('b[0] - ', b[0])
print('b.get(0) - ', b.get(0))
#print('f - ', f[0])
print('f.get(\'City\') - ', f.get('City'))



# 딕셔너리 길이
print('a - ', a)
a['address'] = 'seoul' # 동적으로도 값을 추가할수 있으며, 수정할수도 있다.
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))

# dict_keys, dict_values, dict_items : 반복분(__iter__)에서 사용..
print('a -', a.keys()) # key 값들만 가져옴..
print('b -', b.keys())
print('c -', c.keys())
print('d -', d.keys())

print('a -', list(a.keys()))
print('b -', list(b.keys()))

print('a -', list(a.values()))
print('b -', list(b.values()))
print('c -', list(c.values()))

print()

print('a -', a.items())
print('b -', b.items())
print('c -', c.items())



print('a -', list(a.items()))
print('b -', list(b.items()))

print('a -', a.pop('name'))
print('a -', a)

print('c -', c.pop('arr'))
print('c -', c)

print()

print('f -', f.popitem()) # 끝에 하나씩 사라짐
print('f -', f)
print('f -', f.popitem())
print('f -', f)
print('f -', f.popitem())
print('f -', f)
print('f -', f.popitem())
print('f -', f)

print()
print('a -', 'birth' in a ) # a에 존재하면 True, 없으면 False
print('d -', 'City' in d) 

# 수정
a['test'] = 'test_dict'
print('a -', a)

a['address'] = 'se'
print('a -', a)

a.update(birth = '911118')
print('a -', a)
temp = {'address' : 'busan'} # 명시적으로 다른 리스트를 넣는다.

a.update(temp)
print('a -', a)




