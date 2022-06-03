import sys
import inspect
# from ..sub2 import module2

# module2.py
def mod1_test1():
	print ("Module1 -> Test1")
	print("Path : ", inspect.getfile(inspect.currentframe())) # 현재 파일의 실행 위치를 표기해줌.

def mod1_test2():
	print ("Module1 -> Test2")
	print("Path : ", inspect.getfile(inspect.currentframe()))

	# inspect.currentframe()
	# 호출자의 스택 프레임에 대한 프레임 개체를 반환

	# inspect.getfile()
	# 객체가 정의된 파일의 이름을 반환한다.