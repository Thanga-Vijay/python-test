a = int(input("Enter the value : "))
sum = 0

for i in range(0,a):
    if (i % 3 == 0 or i % 5 == 0):
        sum = i
        print(sum)

# for i in range(5,15,3):
#     print(i)