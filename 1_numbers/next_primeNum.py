#Have the program find prime numbers until the user chooses to stop asking for the next one.
def is_prime(x):
	if x==2:
 		return True
	if x%2==0:
 		return False
	for i in range(3, int(x**0.5)+1, 2):
 		if x%i==0:
 			return False
	return True
	
def main():
	number=2
	g=True
	while g==True:
		if is_prime(number)==True:
			print("Your Prime number is: ", number)
			insert=input("Do you want the next prime number? (yes/no): ")
			if insert.lower().startswith("y"):
				number=number+1
			else:
				print("Thank you!")
				g=False	
		else:
			number=number+1		

 			
if __name__ == '__main__':
	main()