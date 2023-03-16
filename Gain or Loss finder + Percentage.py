print ( " Hello , This is an application to find Profit or loss and thier percentage .","\n","To do so follow the steps ","\n","1-  It will first ask CP ( Cost price ) and SP ( Sellong Price ) then we have to enter the amount and then it will display the results . " )


a = int ( input ("\n"" Enter the Cost Price :"))
b = int ( input (" Enter the Selling Price :"))

if a < b :
    p = b - a
    p_ = ( p / a ) * 100
    print ( "\n" , "You will have profit of " , p ,"and profit percentage is " , p_ , "%",  )
else:
     l = a - b
     l_ = ( l / a ) * 100
     print ( "\n", "You will have loss of " , l , "and lost percentage is " , l_ ,"%" ,)
