# Chapter 08-2
"""
외장 함수(External Functions)
 - 실제 프로그램 개발 중 자주 사용
 - 종류 : sys, pickle, shutil, temfile, time,. random 등
 -

"""


"""
# 예제1

sys.argv에서 sys는 파이썬 인터프리터와 관련된 정보와 기능을 제공하는 모듈 혹은 라이브러리이며, argv는 argument를 의미
python script를 실행할때, 인자 값을 함께 전달 받을 수 있다.
"""
from code import InteractiveConsole
import sys
import webbrowser
print(sys.argv)

# 예제2(강제 종료)
# sys.exit()

# 예제 3(파이썬 패키지 위치 / 현재 모든 패키지들의 위치를 나타냄)
print(sys.path)

"""
pickle 모듈
 - 객체 파일 쓰기
 - 일반 텍스트를 파일로 저장할 때는 파일 입출력을 이용한다.
 - 하지만 리스트나 클래스 같은 텍스트가 아닌 자료형은 일반적인 파일 입출력 방법으로는 데이터를 저장하거나 불러올 수 없다.
 - 파이썬에서는 텍스트 이외의 자료형을 파일로 저장하기 위하여 pickle이라는 모듈을 제공한다.
"""

import pickle

#  예제 4(쓰기)
f= open("test.obj", 'wb') # 'wb' : w(write) + b('binary') / 바이너리로 쓰겠다 명시.
obj = {1 : 'python', 2 : 'study', 3 : 'basic'}
pickle.dump(obj, f) # obj를 쓸거고 f라는 오픈함수를 쓸거다..
f.close()

# 예제 5 (읽기)
f = open('test.obj', 'rb') # 'rb' : r(read) + b('binary') / 바이너리를 읽겠다는 명시.
data = pickle.load(f)
print(data, type(data))
f.close()


"""
#예제6
 os : (밀접한 운영체제 mac, window 에서 사용가능한 기능들을 제공) 환경변수, 디렉토리(파일), 처리 롼견, 운영체제 작업 관련
 mkdir, rmdir(내용이 없을 경우만 삭제), rename

"""
import os
print(os.environ)
print(os.environ["username"])

# 예제7(현재 경로)
print(os.getcwd()) 

# time : 시간 관련 처리
import time
print(time.time())
# 형태 변환
print(time.localtime(time.time()))

# 간단하게 호출
print(time.ctime())

# 예제 11(형식 표현)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) )

"""
# 예제12(시간 간격 발생)
for i in range(5):
    print(i)
    time.sleep(1) # sec 기준
"""


# random : 난수 리턴
import random

# 예제13
print(random.random()) # 0 ~ 1실수가 출력

# 예제14
print(random.randint(1, 45)) 
print(random.randrange(1, 45)) 

# 예제15(섞기)
d = [1,2,3,4,5]
for i in range(5):
    random.shuffle(d)  # 무작위로 섞는다
    print(d)

# 예제16(무작위 선택)
for i in range(5):
    c = random.choice(d)
    print(c)

# webbrowser : 본인의 OS의 웹 브라우저실행
import webbrowser

webbrowser.open("http://google.com") # 현재 열린 브라우저 창에서 실행됨
webbrowser.open_new("http://google.com") # 새롭게 브라우저 열기

