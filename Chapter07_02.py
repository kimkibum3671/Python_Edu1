# Chapter 07-2
# 파이썬 예외처리의 이해2

"""
예외 처리 기본

try : 에러가 발생 할 가능성이 있는 코드 실행

except 에러명1:
except 에러명2:
except 에러명3:
else : try 블록의 에러가 없을 경우 실행
finally : 항상 마지막에 실행

"""

"""
name = ['Kim', 'Lee', 'Park']

# 예제1

try:
    z = 'Choi'
    x = name.index(z)
    print('{}Found it! {} in name'.format(z, x + 1))

except ValueError:
    print('Not found it! - Occured ValueError!')
else:
    print('Ok! else.')
"""
name = ['Kim', 'Lee', 'Park']

# 예제2
try:
    z = 'Kim'
    x = name.index(z)
    print('{}Found it! {} in name'.format(z, x + 1))

except : # ValueError을 지운다면 모든 에러를 다 잡는다.
    print('Not found it! - Occured Error!')
else:
    print('Ok! else.')

print()

# 예제3
try:
    z = 'Ki'
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))

except Exception as e: # 모든 에러를 포괄적으로 다잡는다.
    print(e) # 어떤에러인지 e를 통해서 표현해줌.
    print('Not found it! - Occured Error!')
else:
    print('Ok! else.')

finally:
    print('Ok finally') # 예외가 발생하던 안하던 무조건 실행시켜준다.

print()


# 예제4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Park'
    if a == 'Park':
        print('Ok! Pass!')
    else: 
        raise ValueError # 내부 정책에 의해 강제로 에러 발생시킨다.
except ValueError:
    print('Occured! Exception!')
else: # 에러 발생이 안되었을경우
    print('Ok! else!')