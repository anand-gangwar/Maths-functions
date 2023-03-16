nu=0
a="_"
ab=a*60
instruction = " This is to help you find prime factors of a number . \n \n Instructions :: \n 1. Enter the number using digits only (0-9) \n 2. Entering number using spellings will cause error . \n 3.Example - To find Prime Factors of \"30\" , enter \"30\" instead of typing \" Thirty \" "

print  (instruction)
while True :
	print(f"\n{ab}")
	no= input("\n \n  	Enter the number : ")
	try :
		n = int(no)
		print ( "	Prime factors of the number are : 	1")
	except Exception as e :
		print ("Try Again. You have mistakenly entered wrong word . Try to enter the number using digits (0-9) ")
	while True:
		for i in range (2,n+1):
			if n%i==0 :
				print ("						",i)
				f = int(n/i)
				n=f
				break
			elif n==1:
				break
			else :
				pass
				
		if n==1 :
			break
		else :
			 pass
			
		