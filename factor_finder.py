"""Factor Finder"""
a= 1
while a == 1 :
	print ("_"*60, "\n \n")
	um = (input("	Enter a number : "  ))
	if um=="q":
		break
	else : pass
	print ( "	The factors of the number are :  \n " )
	
	num= int(um)
	for i in range ( 1 , num+1):
		if num%i==0 : print ("		",i)
	

	