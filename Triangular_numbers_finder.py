
print ( "Welcome this is  a triangular number finder .  ")
ll = int(input("Enter a lower limit : "))
ul = int(input("Enter a upper  limit : "))

x = 0
a = [ ]
for i in range ( ll , ul , 1 ):
	a.append(i)
	
for i in range ( 2 , ul ):
	print()
	try :
		print ( a[x] )
	except Exception as e :
		pass
	x = x + i 
	
print ( " List finished .")

	