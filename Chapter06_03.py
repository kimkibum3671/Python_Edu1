# Chapter 06-3
# 파이썬 패키지

"""
Chapter02_01 ~ Chapter... 까지의 파일들을 가지고 있는 폴더를(묶음) 패키지라고 한다.
파이썬은 패키지로 분할 된 개별적인 모듈로 구성
상대경로 : ..(부모 디렉토리), .(현재디렉토리) -> 모듈 내부에서만 사용..

__init__py : Python 3.3 부터는 없어도 패키지로 인식 -> 단, 하위버전 호환을 위해 작성 추천. / 폴더마다 기본적으로 따라다님..
__all__ = ['module2'] 이런식으로 정의되어 있고 이 의미는 'module2' 이름으로만 접근할 수 있음을 의미한다. 정확성이 높아짐.. 사용 제한을 구현한다.
"""

# 예제1
# 같은 경로라서 바로 sub으로 찾아갈수 있다.

import sub.sub1.module1 
import sub.sub2.module2

# 사용
print()
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()
print()
print()

# 예제2
# 보통 from 절로 가져온다.
# import 되어 가져올 패키지의 하위경로가 너무 길경우 alias 처리를 할 수 있다.

from sub.sub1 import module1
from sub.sub2 import module2 as m2
from sub.sub3 import module3 as m3

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()
print(m3.add(1,2))

# 예제3
from sub.sub1 import * # 패키지 내의 파일들 다 갖고 온다.
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()
