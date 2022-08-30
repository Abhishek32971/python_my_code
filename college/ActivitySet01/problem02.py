x=int(input("enter the number of calls"))
if x>200:
	y=200+(x-200)*0.4 + 50*0.6 + 50*0.5    #or you could write y= 155+(x-200)*0.4
elif x>150:
	y=200+(x-100)*0.5
elif x>100:
	y=200+(x-100)*0.6
else:
	y=20
print("the total cost of the telecalls is ",y)