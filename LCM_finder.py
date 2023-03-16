"""LCM finder """

num = int(input("Enter a number 1 : "  ))
um = int(input("Enter a number 2  : "  ))

if num > um:
	sml = um
	grt = num
else :
	sml = num
	grt = um

for i in range(1,grt+1):
	lcm = sml*i
	if lcm%grt==0:
		print ( f"The LCM of the number is {lcm}")
		break
	 
	
		
