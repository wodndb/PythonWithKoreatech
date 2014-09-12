#!/usr/local/bin/python
# coding: utf-8
import sys, os, math


#<---------- 주요 변수 선언 ---------->#

max_int = 100000	# 입력할 수 있는 정수 최대값. 이 값 이상으로도 프로그램을 돌릴 수는 있으나 굉장히 오래 걸리므로 임의로 입력 값의 상한치를 결정하였다.
MAX_INT = str(100000)	# 입력할 수 있는 정수 최대값을 문자열 형식으로 저장한 변수
prime_num = [1, 2]	# 1부터 입력받은 숫자 사이의 소수를 저장하는 변수이자 에라토스테네스의 체


#<---------- 표준 입력 ---------->#

num = input('2 이상 ' + MAX_INT + '이하의 정수를 입력해주십시오 : ')

# 입력에 대한 예외 처리 코드
while num < 2 or num > max_int or type(num) == float:
	if type(num) == float :
		print '*입력된 값이 실수입니다. 정수로 입력해주십시오.\n(범위는 1 이상 ' + MAX_INT + ' 이하의 정수입니다.)'
	elif num < 1 :
		print '*입력된 값이 1보다 작습니다. 다시 입력해주십시오.\n(범위는 1 이상 ' + MAX_INT + ' 이하의 정수입니다.)'
	else:
		print '*입력된 값이 ' + MAX_INT + ' 보다 큽니다. 다시 입력해주십시오.\n(범위는 1 이상 ' + MAX_INT + ' 이하의 정수입니다.)'
	num = input(': ')

#<---------- 소수 구하기 ---------->#

# Key-Point! 에라토스테네스의 체를 이용하면 된다.

for i in range(2, num+1):
	for j in range(1, len(prime_num)):
		if i % prime_num[j] == 0:	#소수로 나누어 떨어진다, 즉 소수가 아니다.
			j = len(prime_num) + 1
			break
		elif math.sqrt(num) < prime_num[j]:	#소수 판별할 수의 제곱근보다 나눗셈으로 피연산할 소수가 더 크다, 즉 반복문을 빠져나온다.
			break
	if j != len(prime_num) + 1:	
		prime_num.append(i)
print prime_num[1:]
