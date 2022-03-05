d = 0
s = int(input("Enter the speed :"))
print("Your speed is :",s)

if (s >= 75) and (s % 5 ==0):
	d += ((s-75)/5)+1
	print("Demerit Points :",d)
else:
    print("nothing")

if (d >= 12):
	print("Your license is suspended")













