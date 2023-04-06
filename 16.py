list1 = [3, 5, 4, 8, 6, 33, 22, 18, 76, 1]
result = list(filter(lambda x: (x%2 != 0), list1))
print(result)