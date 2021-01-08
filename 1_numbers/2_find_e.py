#Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.

import math

class find_E:
	def __init__(self, number):
		self.number=number

	def get_value(self):
		E=math.e 
		E=str(E)
		result=""
		for i in range(self.number+2):
			x=str(E[i])
			result=result+x
		result=float(result)	
		return result	

if __name__ == "__main__":
	print("This is a program that will print the e value till the nth digit after the decimal")
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
	object=find_E(number)
	print(object.get_value())
