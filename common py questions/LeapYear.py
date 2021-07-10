year=int(input("enter the year:"))
if(x%4==0):
	if(x%100==0):
		if(x%400==0):
			print("the year is  leap y")
		else:
			print("the year is not leap y")	
	
	else:
		print("the year is leap y")		

else:
	print("the year is not leap y")