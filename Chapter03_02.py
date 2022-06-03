# Chapter-03-2
# Python 문자형
# 문자형 중요

# 문자열 생성
from glob import escape
from posixpath import split


str1 = "I am Python"
str2 = 'I am Python'
str3 = """I am Python"""
str4 = '''I am Python'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용(탈출 문자)
"""
\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널문자
...
"""

# I'm Boy

print("I'm Boy")
print('I\'m Boy') # 작은 따옴표를 사용하면 I'am 에서 에러걸림.. 따라서 역슬래시 사용
print('a \t b') # tab Key
print('a\"\"b')

escape_str1 = "Do you have \"retro games\" ?"
print(escape_str1)

escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)

# Row String
# '\' 자체를 신경 안씀. 이스케이프 자체를 사용 안하겠다는 표시.. 즉 '\' 을 그대로 출력

raw_s1 = r'D:\python\test' # \t를 탭으로 인식X
print(raw_s1)

# 멀티라인 입력
# muti_str = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" .. 보기가 안좋음.. 잘라서 보기좋도록 처리하려고할때.

multi_str = \
'''
String
Multi Line
Test
'''

print(multi_str)

# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul!Daejoen!Busan!Jinju"

print(str_o1 * 3) # 3번 문장 반복
print(str_o1 + str_o2) # 문장 합침
print('y' in str_o1) # 사실 str_o1은 시퀀스라고 생각하면 된다. 즉 각 문장을 구성하는 단어중에 'y'의 존재여부를 확인한다.
print('n' in str_o1)
print('P' not in str_o2) # str_o2에 P라는 단어가 없니?

# 문자열 형 변환
print(str(66), type(str(66))) # 문자로 변형해서 문자66을 출력해주는것임!
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))

# 문자열 함수(uppper, isalnum, startswitch, count, endswitch, isalpha...)
print("Capitalize: ", str_o1.capitalize()) # 첫번째 시작 문자를 대문자로 형변환 시킴.
print("endswitch : ", str_o2.endswith("!")) # 마지막에 !으로 끝났는지 확인.
print("replace : ", str_o1.replace("thon", "Good")) # 문자열 대체
print("sorted :", sorted(str_o1)) # 기준에 맞게 정렬함
print("split : ", str_o4.split('!')) # '!' 느낌표 기준으로 분리해줌

# 반복(시퀀스)
im_str = "Good Boy!"
print(dir(im_str)) # __iter__ im_str에서 사용할수 있는 모든것을 나타내줌.

# 출력
for i in im_str:
    print(i)

# 슬라이싱 연습
'''
슬라이싱 or 슬라이스 : 연속적인 객체들에(예:문자열, 리스트, 튜플) 범위를 지정해 선택해서 객체들을 가져오는 방법 및 표기법을 의미한다.
                      슬라이싱을 하면 새로운 객체를 생성하게되면 일부분을 복사해서 가져온다고 생각하면 된다.
'''

# 음수는 오른쪽에서 왼쪽으로 간다.
str_s1 = "Nice Python"

print(str_s1[0:3]) # 0 1 2 까지 나옴..
print(str_s1[5:11]) # 5 ~ 10까지 나옴
print(str_s1[5:]) # 5 ~ 끝까지 나옴
print(str_s1[:len(str_s1)]) # str_s1[:11]
print(str_s1[1:9:1]) # 1 ~ 8 까지 2 자리씩 점프하면서 값들만 가져옴
print(str_s1[-5:]) # 오른쪽의 5자리 전부터 끝까지 나옴.
print(str_s1[1:-2]) # 첫째 자리부터 오른쪽에서 2자리 전까지 나옴.
print(str_s1[::2]) # 2자리씩 점프하면서 값들 가져옴
print(str_s1[::-1]) # 점프를 오른쪽에서 왼쪽으로 나온다. 결국 순서가 역으로 출력됨.

# # 아스키 코드(또는 유니코드)
# a = 'z'

# print(ord(a)) # 해당 아스키코드의 값을 알려준다.
# print(chr(122)) # chr <- 해당 번호의 아스키값을 보여준다. / 즉 해당 번호의 아스키 코드 문자를 보여준다.
