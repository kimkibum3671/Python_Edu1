# Chapter02-1
# 파이썬 완전 기초
# Print 사용법

#기본 출력
print('python start')
print("Python Start!")
print("""Python Start!""")
print()

#Seperator 옵션
#단위마다 어떻게 처리하여 연결할지 정의해준다.
print('P','Y','T','H','O','N', sep=',')

#End
# 기본값으로 print 구문에는 개행(\n)이 들어가 있으며, end를 사용해 개행을 없애거나 문자를 입력 할 수 있다.
print('Welcome to', end='')
print('IT', end='')
print('Web Site')
print()

# file 옵션
import sys
print('Learn Python', file=sys.stdout)
print()

#format 사용(d'정수', s'문자열', f'실수(소수)')
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one','two'))
print('{1} {0}'.format('one', 'two'))

# %s, 문자열은 {}사용시 's' 생략해도 된다.
print('%10s' % ('nice')) #10자리를 갖으며 오른쪽끝에서 글자수 만큼 채운다.
print('{:>10}'.format('nice')) # 10자리를 갖으며 오른쪽 끝에 글자수 만큼 채운다.

print('%-10s' % ('nice')) #10자리를 갖으며 왼쪽끝에서 글자수 만큼 채운다.
print('{:_>10}'.format('nice')) #왼쪽부터 '_'으로 채우고 나머지 글자를 'nice'로 채워 총 10자리를 만든다.
print('{:^10}'.format('nice')) # 10자리를 만들고 가운데 정렬로 글을 채운다.

print('%.5s' % ('nice Python')) # 5글자만 출력되도록 제한한다.(제한)
print('%5s' % ('nice Python')) # 5글자만 출력되도록 제한하는 구문이지만, '.'이 없기에 모든 글자 출력, 강제 제한은 못함.
print('{:10.5}' .format('pythonstudy')) #10칸을 만들고 그중 5글자만 제한

# %d, 정수형은 {}사용시 'd' 생략하면 안된다.
print('%d %d' %(1,2))
print('{} {}'.format(1,2))

print('%4d' %(42)) #오른쪽 부터 채운다.
print('{:_>4d}'.format(42)) # 오른쪽에 원하는 수를 입력하고 왼쪽에 남는 공간에 '_'를 넣는다.
print('{:_<4d}'.format(42)) # 왼쪽에 원하는 수를 입력하고 오른쪽에 남는 공간에 '_'를 넣는다.


# %f ,실수형은 {}사용시 'f' 생략하면 안된다.
print('%f' % (3.141592))
print('{:f}'.format(3.141592))
print('%06.2f' % (3.141592)) #6자리 만들고 소수는 두자리 나머지는 정수자리 만든다.
print('{:06.2f}'.format(3.141592))

