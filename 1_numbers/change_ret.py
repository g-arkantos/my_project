'''Change Return Program - The user enters a cost and then the amount of money given. 
The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.'''
import math
def main():
	penny=0.01
	nickel=penny*5
	dime=penny*10
	quarter=penny*25
	dollar=int(penny*100)
	print("dollar: ", dollar,'\n ', "nickel: ", nickel)
	cost=11.14
	get_change(cost)

main()

def get_change():
	while True:
		if cost>0:
			dollar=math.floor(cost)
			rem=cost-dollar
			






