# num = 10    
# print(num)

# name2_my = "Anurag"
# print(name2_my)

# str1 = "My name is Anurag. \nI am 22 years old"
# lst1 = list(str1)
# print(lst1)
# print(str1)

# str2 = "Anurag"
# lst2 = [str2[i] for i in range(0, len(str2))]
# lst2.sort()
# print(lst2)

# import counter class from collections module
from collections import Counter

# Creation of a Counter Class object using
# string as an iterable data container
x = Counter("geeksforgeeks")

# printing the elements of counter object
# for i in x.elements():
# 	print ( i, end = " ")

# print(x)

# y = x.values()
# print(x.values())
# z = []
# for a in y:
#    z[i] = a
# print(z) 

# lst_a = []
# lst_a[2] = 3
# print(lst_a)

# lst = [x for x in range(50) if x % 2 == 0]

# l1 = [1, 2, 3]
# l2 = l1
# l1.append(4)
# print(l2)

# l1 = ['a', 'b', 'c']
# print(l2)

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print('Name' in dict) #True
print('Zara' in dict) #False
# ie by default the KEYS are searched
