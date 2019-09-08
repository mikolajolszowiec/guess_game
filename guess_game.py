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
		
def guess_numbers(number, min_r, max_r):
	counter = 0
	while True:
		x = get_user_hit()
		counter += 1
		if x>number:
			print("za duzo")
		elif x<number:
			print("za malo")
		elif x == number:
			print(f"Sekretna liczba to {number}, wygrales po {counter} probach")
			break

def app_run():
	min_int, max_int = get_user_range()
	random_int = random_from_range(min_int,max_int)
	guess_numbers(random_int, min_int, max_int)
	
app_run()