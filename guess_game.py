from random import randint 

def get_user_range():
	print("Podaj ziomeczku minimum zakresu")
	min_r = int(input())
	print("Podaj ziomeczku maksimum zakresu")
	max_r = int(input())
	return min_r, max_r

def random_from_range(min_d, max_d):
	return randint(min_d, max_d)
