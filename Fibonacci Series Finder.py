a = 0
b = 1
c = int ( input ("		Enter the level upto which the series needs to be printed :"))

print ( a )
print ( b )

for i in range ( 1,c+1):
    d = a + b
    print ("		",d)
    a = b
    b = d
