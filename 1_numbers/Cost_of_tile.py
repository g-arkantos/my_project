#Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take to cover a floor plan 
#of width and height, using a cost entered by the user.

def get_data():
	width=float(input("Enter the width in m: "))
	height=float(input("Enter the height in m: "))
	cost=float(input("Enter the cost of 1mx1m: "))
	return cost*(width*height)

print("The total cost will be: ",get_data())	