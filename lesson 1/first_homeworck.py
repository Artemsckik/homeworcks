#  3 переменные с одинаковыми данными (и одинаковым типом) и с одинаковыми идентификаторами.

a = 3

b = 3

c = 3

print("1: ",a is b is c)

print(a == b == c)

print(type(a),type(b),type(c))
# 2 переменные с одинаковыми данными (и одинаковым типом) и с разными идентификаторами

n = [2]

e = [2]

print('2: ',n == e)

print(n is e)

print(type(n), type(e))

# Первые 3 разны индификаторы, 2 последних индификаторы =, даные равны у всех

h = [2]

b = e

c = n

a = h

n = a

e = a

print('3: ',a is b is c)
print(id(a),id(b),id(c))
print(n is e)
print(id(n), id(e))
print(a == b == c)
print(type(a),type(b),type(c))
print(n == e)
print(type(n), type(e))
# a1 = ...., a2 = ...., a1 == a2 True , a1 is a2 True

g1 = 4

g2 = 4

print('4: ', g1 == g2)

print(g1 is g2)

# a1 == a2 True, a1 is a2 False

q1 = [5]

q2 = [5]

print('5: ', q1 == q2)

print(q1 is q2)

# 6

z = int(3)

x = float(3)



print('6: ', z is x)
print(z == x)
