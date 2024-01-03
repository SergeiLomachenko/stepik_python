numbers = [8, 9, 10, 11]
numbers.insert(1, 17)
numbers.insert(25, 4)
numbers.insert(26, 5)
numbers.insert(27, 6)
numbers.pop(0)
numbers2 = numbers.copy()
numbers = numbers + numbers2
numbers.insert(3, 25)
print(numbers)