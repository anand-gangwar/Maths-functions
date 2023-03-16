def fact(n):
	""" It finds the factorial of a given number . """
	if n/1==1:
		if n == 0 or n==1 :
			return 1
		else :
			return n * fact(n-1)
	else :
		if n == 0 or n==-1 :
			return -1
		else :
			return n * fact(n+1)
		
#maximum number : 995 and -995
#print(fact(-5))


## fibonacii func

def fibo(x):
	f1=0
	f2=1
	print(f"	 			0 \n		 		1")
	for i in range (0,x-1):
		f3= f1+f2
		f1=f2
		f2=f3
		print("				",f3)
	
#fibo(5)

def fib(x):
	""" This function finds the fibonaci number found at the xth place . It gives only the number not the  series . """
	if x==1:
		return 0
	elif x==2:
		return 1
	elif x==3:
		return 1
	else :
		return (fib(x-1)+fib(x-2))

print(fib(7))		

print(fib.__doc__)