#!/usr/bin/python3

def print_last_digit(number):
	if number < 0:
		num = abs(num)
	else:
		num = number
	last_digit = num % 10
	print(last_digit)
