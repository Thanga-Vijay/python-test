a = int(input("Enter the first value :"))
b = int(input("Enter the second value :"))
c = int(input("Enter the third value :"))
d = [a, b, c]
total = sum(d)

if a == b == c:
    print(total * 3)
else:
    print(total)
