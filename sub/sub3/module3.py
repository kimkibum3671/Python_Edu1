# Chapter 06-2
# 파이썬 모듈
"""
Module : 특정 기능이 정의된 파일
         (함수, 변수, 클래스 등 파이썬 구성 요소등을 모아놓은 파일)


"""

def add(x, y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def power(x, y):
    return x**y

# print('-' * 15)
# print('called! inner!!')
# print(add(5,5))
# print(subtract(15,5))
# print(multiply(5,5))
# print(divide(10, 5))
# print(power(2, 10))
# print('-' * 15)

if __name__ == "__main__": # 메인 영역을 따로 지정해 놓음으로 다른 프로젝트에서 import할때 예제로 확인할 수 있도록 따로 빼논다.
    print('-' * 15)
    print('called! __main__!!')
    print(add(5,5))
    print(subtract(15,5))
    print(multiply(5,5))
    print(divide(10, 5))
    print(power(2, 10))
    print('-' * 15)