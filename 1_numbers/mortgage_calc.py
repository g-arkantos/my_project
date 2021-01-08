'''Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. 
Also figure out how long it will take the user to pay back the loan.
 For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).
 M = the total monthly mortgage payment
P = the principal loan amount
r = your monthly interest rate. 
n = number of payments over the loan’s lifetime
M = P[r(1+r)^n/((1+r)^n)-1)]
'''

def take_data():
	print("****************************Please give the following details****************************")
	principal=float(input("Enter the principal Load amount: "))
	rate=float(input("Enter the monthly rate of interest in %: "))
	n=int(input("Enter the number of payment over the loan’s lifetime: "))
	return principal*(rate*(1+rate)**n / (((1+rate)**n)-1))
def main():
	t=(take_data())
	print(int(t))

	

if __name__ == '__main__':
	main()