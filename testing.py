# for a in range (5,11,2):
# 	print(a)

# x = [1,3,2,4,5,6,7,88,5345,35,4]

# for y in x:
# 	if y == 88:
# 		break;
# 	print(y)
# print("Function break")
# else:
# 	print("Function fully executed")

# a = 58
# b = 56
# c = 59
# #print("a is equal to b") if a == b else print("a is bigger than b") if a > b else print("b is bigger than a")
# # 	print('a is equal to b')
# # # elif a > b:
# # # 	print('a is greater than b')
# # else:
# # 	print("b is bigger than a")
# if a > c or a > b:
# 	print('a is the biggest value')
# else:
# 	print('program not running')

# def my_fun(*kids):
# 	print(kids[0] +" The litte child is")

# my_fun("vijay","vijay11","vijay22")


# text = 'This is my sample file \n'

# saveFile = open('E:/demo.txt','w')
# saveFile.write(text)
# saveFile.close()


# appendME = '\n Append Example'

# appendFile = open('E:/demo.txt','a')
# appendFile.write(appendME)
# appendFile.close()


# readme = open('E:/demo.txt','r').readlines()

# print(readme)

# x = 1,6,9,2,45
# y = [45,676,34,7,34]

# print(x[2])

import urllib.request
address = urllib.request.urlopen('https://www.snapay.in/')
print(address.read())