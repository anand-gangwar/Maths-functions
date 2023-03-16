print ("This app is used to verify that the lenght which are entered verifies Phythagoras theroem or not ")

a = int ( input ("\n" " Enter the Hypontenuse lenght :"))
b = int ( input (" Enter the base Lenght :"))
c = int ( input (" Enter the Prependicular Lenth "))

d = b*b
e = c*c
f = d + e

l = a*a

print ("\n" ,a  , "*", a, "=", b, "*", b, "+", e, "*", e, )
print ( l, "=", d, "+" , e , )
print ( l , "=" ,  f , )

if l==f :
    print ("\n"" It is a Right-Angled Trianle ")
else:
    print ("\n"" It is not a Right-Angled Triangle ")

