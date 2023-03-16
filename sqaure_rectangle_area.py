print ( " Enter '1' if you want to find the area of a rectangle or '2' if you want to find the area of a square. ")
a=int(input("Enter the number : "))
if a==1 :
	l=int(input("Enter the lenght of the rectangle : "))
	b=int(input("Enter the breadth of the rectangle : "))
	ar= l*b
	print ( " The area of the rectangle is : " , ar )
	
else :
	s=int(input("Enter the side of the square : "))
	area=s**2
	print ( " The area of the square is : " , area)