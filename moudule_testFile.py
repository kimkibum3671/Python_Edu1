# 모듈 사용 실습

import sys
import time

print(sys.path)
print(time.time())

print(type(sys.path))

# # 모듈 경로 삽입
# sys.path.append('C:\python_math')

# print(sys.path)

# import test_module

# # 모듈 사용
# # 영구적으로 등록하고 싶다면 '파이썬 파일 영구적 등록'으로 검색하면 된다.
# print(test_module.power(10, 3))


import Chapter06_02 # 불필요 한것들도 출력될수 있다. 따라서 해당 파일에서 조건문으로 필터링 해준다.

print(Chapter06_02.add(1,2))