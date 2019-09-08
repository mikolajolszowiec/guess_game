from random import randint 

def get_user_range():
	print("Podaj ziomeczku minimum zakresu")
	min_r = int(input())
	print("Podaj ziomeczku maksimum zakresu")
	max_r = int(input())
	return min_r, max_r

def random_from_range(min_d, max_d):
	return randint(min_d, max_d)

def get_user_hit():
	print("Podaj ziomeczku swoja liczbe")
	return int(input())


def app_run():
	min_int, max_int = get_user_range()
	random_int = random_from_range(min_int,max_int)
	while True:
		x = get_user_hit()
		if x == random_int:
			print("brawo wygrales")
			break
		elif x>random_int:
			print("za duzo")
		elif x<random_int:
			print("za malo")

app_run()