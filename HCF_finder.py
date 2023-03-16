"""HCF finder """

n1 =  int(input("Enter number 1 : "  ))
n2 = int(input("Enter number 2  : "  ))

if n1 > n2 :
	sml = n2
	grt = n1
else :
	sml = n1
	grt = n2
	
for i in  range (grt+1 , 0 , -1 ):
	if grt%i==0 and sml%i==0 :
		print (f"The HCF of the numbers is : {i}")
		break
	
