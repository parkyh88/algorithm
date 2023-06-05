#######################################1######################################
# 정수가 입력되었을 때, True/False 로 평가해주는 프로그램을 작성해보자.
# 예시
# n = int(input())
# print(bool(n))
# 참고
# bool( ) 을 이용하면 입력된 식이나 값을 평가해 불 형의 값(True 또는 False)을 출력해준다.
# 식이나 값을 계산해서 결과값이 만들어지는 것을 평가(evaluate)라고 한다. 
# python 언어에서 정수값 0은 False(거짓)로 평가되고, 그 외의 값들은 모두 True(참)로 평가된다.
# ** 불 대수(boolean algebra)는 수학자 불이 만들어낸 것으로 True(참)/False(거짓) 값만 가지는 논리값과 그 값들 사이의 연산을 다룬다.
number = int(input())
print(bool(number))

#######################################2######################################
# 정수값이 입력될 때,
# 그 불 값을 반대로 출력하는 프로그램을 작성해보자.
# 예시
# a = bool(int(input()))
# print(not a)
# 참고
# a = bool(int(input()))
# 와 같은 형태로 겹쳐 작성하면, 한 번에 한 단계씩 계산/처리/평가된다.
# 위와 같은 명령문의 경우 input( ), int( ), bool( ) 순서로 한 번에 한 단계씩 계산/처리/평가된다.
# 어떤 불 값이나 변수에 not True, not False, not a 와 같은 계산이 가능하다.
# 참 또는 거짓의 논리값을 역(반대)으로 바꾸기 위해서 not 예약어(reserved word, keyword)를 사용할 수 있다.
# 이러한 논리연산을 NOT 연산(boolean NOT)이라고도 부르고,
# 프라임 '(문자 오른쪽 위에 작은 따옴표), 바(기호 위에 가로 막대), 문자 오른쪽 위에 c(여집합, complement) 등으로 표시한다.
# 모두 같은 의미이다.
# 참, 거짓의 논리값 인 불(boolean) 값을 다루어주는 예약어는 not, and, or 이 있고,
# 불 값들 사이의 논리(not, and, or) 연산 결과도 마찬가지로 True 또는 False 의 불 값으로 계산 된다.
# 정수값 0은 False 이고, 나머지 정수 값들은 True 로 평가된다.
# 빈 문자열 "" 나 ''는 False 이고, 나머지 문자열들은 True 로 평가된다.
# ** 불 대수(boolean algebra)는 수학자 불이 만들어낸 것으로 True(참)/False(거짓) 값만 가지는 논리값과 그 값들 사이의 연산을 다룬다.
number = bool(int(input()))
print(not number)

#######################################3######################################
# 2개의 정수값이 입력될 때,
# 그 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.
# 예시
# a, b = input().split()
# print(bool(int(a)) and bool(int(b)))
# 참고
# and 예약어는 주어진 두 불 값이 모두 True 일 때에만 True 로 계산하고, 나머지 경우는 False 로 계산한다.
# 이러한 논리연산을 AND 연산(boolean AND)이라고도 부르고, · 으로 표시하거나 생략하며, 집합 기호 ∩(교집합, intersection)로 표시하기도 한다. 
# 모두 같은 의미이다.
# 참, 거짓의 논리값 인 불(boolean) 값을 다루어주는 예약어는 not, and, or 이 있고,
# 불 값들 사이의 논리(not, and, or) 연산 결과도 마찬가지로 True 또는 False 의 불 값으로 계산된다.
# ** 불 대수(boolean algebra)는 수학자 불이 만들어낸 것으로 True(참)/False(거짓) 값만 가지는 논리값과 그 값들 사이의 연산을 다룬다.
number_1, number_2 = input().split()
print(bool(int(number_1)) and bool(int(number_2)))

#######################################4######################################
# 2개의 정수값이 입력될 때,
# 그 불 값이 하나라도 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.
# 참고
# or 예약어는 주어진 두 불 값 중에서 하나라도 True 이면 True 로 계산하고, 나머지 경우는 False 로 계산한다.
# 이러한 논리연산을 OR 연산(boolean OR)이라고도 부르고, + 로 표시하거나, 집합 기호 ∪(합집합, union)로 표시하기도 한다.
# 모두 같은 의미이다.
# 참, 거짓의 논리값 인 불(boolean) 값을 다루어주는 예약어는 not, and, or 이 있고,
# 불 값들 사이의 논리(not, and, or) 연산 결과도 마찬가지로 True 또는 False 의 불 값으로 계산된다.
# ** 불 대수(boolean algebra)는 수학자 불이 만들어낸 것으로 True(참)/False(거짓) 값만 가지는 논리값과 그 값들 사이의 연산을 다룬다.
number_1, number_2 = input().split()
print(bool(int(number_1)) or bool(int(number_2)))

#######################################5######################################
# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자.
# 예시
# ...
# c = bool(int(a))
# d = bool(int(b))
# print((c and (not d)) or ((not c) and d))
# 참고
# 참 거짓이 서로 다를 때에만 True 로 계산하는 논리연산을 XOR(exclusive or, 배타적 논리합) 연산이라고도 부른다.
# 논리연산자는 사칙(+, -, *, /) 연산자와 마찬가지로 여러 번 중복해서 사용할 수 있는데, 
# 사칙 연산자와 마찬가지로 계산 순서를 표시하기 위해 괄호 ( )를 사용할 수 있다.
# 괄호를 사용하면 계산 순서를 명확하게 표현할 수 있다.
# 수학 식에서는 소괄호 (), 중괄호 {}, 대괄호 []를 사용하기도 하지만, 프로그래밍언어에서는 소괄호 ( ) 만 사용한다.
# ** 불 대수(boolean algebra)는 수학자 불이 만들어낸 것으로 True(참)/False(거짓) 값만 가지는 논리값과 그 값들 사이의 연산을 다룬다.
number_1, number_2 = input().split()
bool_number_1 = bool(int(number_1))
bool_number_2 = bool(int(number_2))
print((bool_number_1 and (not bool_number_2)) or ((not bool_number_1) and bool_number_2))

#######################################6######################################
# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 서로 같을 때에만 True 를 출력하는 프로그램을 작성해보자.
number_1, number_2 = input().split()
bool_number_1 = bool(int(number_1))
bool_number_2 = bool(int(number_2))
print(((bool_number_1 and bool_number_2) or (not bool_number_1 and not bool_number_2 )))

#######################################7######################################
# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력하는 프로그램을 작성해보자.
number_1, number_2 = input().split()
bool_number_1 = bool(int(number_1))
bool_number_2 = bool(int(number_2))
print(bool_number_1 == False and bool_number_2 == False)