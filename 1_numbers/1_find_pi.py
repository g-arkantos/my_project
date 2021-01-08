#1 find the pi value to the  nth digit
import math

class pI:
	def __init__(self, number):
		self.number=number

	def get_value(self):
		pii=math.pi 
		pii=str(pii)
		result=""
		for i in range(self.number+2):
			x=str(pii[i])
			result=result+x
		result=float(result)	
		return result	

if __name__ == "__main__":
	print("This is a program that will print the pi value till the nth digit after the decimal")
	condition=False	
	while condition==False:
		try:
			number=int(input("Enter a number between 1 to 15: "))
			if number>15:
				raise Exception
			else:
				x=True
				break
		except :
			print("The number should be a Natural number not exceeding 15.")		
	object=pI(number)
	print(object.get_value())

