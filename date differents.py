from datetime import date

# a = y1, m1 , d1
# y = input("Enter the date :",y1, d1, m1)
# #m = input("Enter the month :")


d1 = date(2022, 1, 15)
d2 = date(2022, 2, 10)

d3 = d2-d1

print(d3.days)
