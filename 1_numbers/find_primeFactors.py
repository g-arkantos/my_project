#Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.

class find_primeFactors:
	def __init__(self):
		result=[]
	def get_primeFactors(self, number):
		self.number=number
		num=self.number
		result=[]
		i=2
		while i <=num:
			if num%i==0:
				num=num/i
				result.append(i)
			else:
				i=i+1
		return result			
						

if __name__ == '__main__':
	p=find_primeFactors()
	n=int(input("Enter an integer number: "))
	print(p.get_primeFactors(n))
	
