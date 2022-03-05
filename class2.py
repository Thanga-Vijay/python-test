a = int(input("Enter the value :"))

if (a % 3 == 0) and (a % 5 == 0):
	print("This value is FizzBuzz ")
elif (a % 5 == 0):
	print("This value is Buzz ")
elif (a % 3 == 0):
	print("This value is Fizz")
else:
	print(a)