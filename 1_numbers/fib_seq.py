#Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

class fibonacci:
	def __init__(self, number):
		self.number=number

	def display_fibseq(self):
		li=[1,1]
		for i in range(0,self.number-2):
			j=i+1
			result=li[i]+li[j]
			li.append(result)
		return li
		

if __name__ == '__main__':
	print("This is a program that will print the pi value till the nth digit after the decimal")
	number=int(input("Enter a number between 1 to 15: "))			
	object=fibonacci(number)
	print(object.display_fibseq())	
	i=5
	j=28//i
	print(type(j))
	print(i)
