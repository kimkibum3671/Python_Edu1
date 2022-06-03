# Chapter09-2

"""
CSV 파일 읽기 및 쓰기

CSV : MEME - text/csv

"""

import csv
from dataclasses import fields
from ntpath import join

# 예제1
with open('./resource/test1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # 최상위 정보(header) Skip!!
    # 객체 확인
    print(reader)

    print('-----------------------')
    # 타입 확인
    print(type(reader))

    # 속성 확인
    print(dir(reader)) # __iter__ 존재 유무 확인. for 사용 가능..
    print('-----------------------')
    
    for c in reader:
        # print(c) 
        # 타입 확인(리스트)
        # print(type(c))
        # list to str
        print('_' .join(c))
        
        """
        join : 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 변환하는 함수.
        - join(List) : ['a', 'b', 'c'] 유형의 리스트를 'abc'문자열로 합쳐서 반환해주는 함수이다,
        - '구분자'.join(List) : 리스트 값들 사이에 구분자를 넣어 문자열로 합해준다.
                               '_'. join(['a', 'b', 'c']) 이라 한다면 "a_b_c"와 같은 형태로 문자열을 만들어서 반환해준다.
        """

# 예제2
with open('./resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter = '|') # '|'구성되어 있는 구분자의 형태를 ','으로 변형하여 가져온다.

    for c in reader:
        print(c)

print('----------------')

# 예제3
with open('./resource/test1.csv', 'r') as f:
    # 기존 Reader으로 호출하여 가져올 경우 List 형태로 정보만 가져오지만, DictReader은 단어 그대로 Dictionary 형태로 가져오기에 출력시 Dictionary형태로 출력해준다.
    reader = csv.DictReader(f) 
    # 확인
    print(f)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        for k,v in c.items(): # Key 와 Value 값을 가져온다.
            print(k, v)
        print('----------------')

# 예제4
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21]]
# 한개의 리스트가 한개의 레코드로 기록됨..
with open('./resource/write.csv', 'wt') as f:
    print(dir(csv))
    wt = csv.writer(f) # 쓰기 직전 준비작업

    # dir 확인
    # print(dir(wt))
    # 타입확인
    # print(type(wt))

    for v in w:
        wt.writerow(v) # 한줄 단위로 기재

# 예제5
with open('./resource/write2.csv', 'wt') as f:
    # 필드 명
    fields = ['One', 'Two', 'Three']

    # Dict Writer  
    wt = csv.DictWriter(f, fieldnames=fields)

    # Header Writer, 헤더를 먼저 작성
    wt.writeheader()

    for v in w: # 헤더와 일치해야 기재된다.
        wt.writerow({'One' : v[0], 'Two' : v[1], 'Three' : v[2]})

