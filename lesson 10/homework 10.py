

numbers = [1, '3', 2, '2', 'dwadww']
n = []
number = map(lambda q: str(q) if type(q) == int else n.append(q) , numbers)
print(list(number), n)


