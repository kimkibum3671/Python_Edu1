# Chapter 09-1
# 파일 읽기 및 쓰기
"""
 읽기 모드 : r(read), 쓰기모드 : w(write), 추가모드 : a(append), 텍스트 모드 : t, 바이너리 모드 : b

 상대 경로(../ , ./), 절대 경로 ('C:/Python/example..')
"""
# 예제1) 파일 읽기
# f = open('C:\\python_basic\\resource\\it_news.txt')
f = open('./resource/it_news.txt', 'rt', encoding='UTF-8')
# 속성 확인
print(dir(f))

# 인코딩 확인
print(f.encoding)

# 파일 이름
print(f.name)

# 모드 확인
print(f.mode)

cts = f.read()
print(cts)

# 반드시 close
f.close()

# 예제2
with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f: # alias 사용
    c = f.read()
    print(c)
    print(iter(c)) 
    print(list(c))
    # f.close() with를 사용한다면 굳이 close 안써도 된다.

print()

# 예제3 
# read() : 전체읽기, read(10) : 10 Byte 수만큼 읽어온다.

with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f: # alias 사용
    c = f.read(20)
    print(c)
    c = f.read(20) # 이전에 어디까지 읽었는지 기억함(마지막 커서)
    print(c)
    c = f.read(20) # 이전에 어디까지 읽었는지 기억함(마지막 커서)
    print(c)
    f.seek(0,0) # from, to 으로 커서 위치를 옮긴다.
    c = f.read(20)
    print(c)

    # f.close() with를 사용한다면 굳이 close 안써도 된다.

print()

# dPwp4
# readline : 한줄씩 읽기
with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f: # alias 사용
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)

print()

# 예제5
# readlines : 전체를 읽은 후 라인 단위로 리스트 저장!! 많이 사용!!

with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f: # alias 사용
    cts = f.readlines()
    print(cts)
    print()

    for c in cts:
        print(c, end='')

print()

# 파일 쓰기(write)

# 예제1
with open('./resource/contents1.txt', 'wt') as f:
    f.write('I love Python \n')

# 예제2
# with open('./resource/contents1.txt', 'wt') as f: 
#   f.write('I love Python2 \n')  기존 위에 내용 지워짐..
with open('./resource/contents1.txt', 'at') as f:
    f.write('I love Python2 \n')

#  예제3
# writelines : 리스트 -> 파일
with open('./resource/contents1.txt', 'wt') as f:
    list = ['Orange \n', 'Allpe \n', 'Melon \n']
    f.writelines(list)

# 예제4
with open('./resource/contents1.txt', 'wt') as f:
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f) # file 에다가 출력해준다!!, 콘솔에서 출력 안됌..