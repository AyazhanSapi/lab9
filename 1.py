# Функция принимает на вход кортеж с именем и ростом, возвращает только рост
def get_height(human_tuple):
    height = human_tuple[1]
    return height

people = [('John', 155), ('Pete', 160), ('Clara', 188), ('Alex', 180)]
print(sorted(people, key=get_height))
# [(‘John’, 155), (‘Pete’, 160), (‘Alex’, 180), (‘Clara’, 188)]

people = [('John', 155), ('Pete', 160), ('Clara', 188), ('Alex', 180)]
print(sorted(people, key=lambda x: x[1]))

def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result

list_of_integers = [1, 2, 3]
print(my_sum(list_of_integers))

#*args
def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))


#**kwargs
def mysal(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Sapi", b="Ayazhan", c="Polatkyzy"))



matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
# С использованием цикла for
result = []
for row in matrix:
    for item in row:
        item *= 0.3
print(result)

# С использованием map
result = map(lambda x: x * 0.3, matrix)
print(result)


# С использованием цикла for
result = []
summ = 0
for row in matrix:
    summ = sum(row)
    if summ < 10:
        result.append(row)
print(result)

# С использованием filter
result = filter(lambda x: sum(x) < 10, matrix)
print(result)


# С использованием цикла for
result = []
for row in matrix:
    for item in row:
        result.append(item)
print(result)

# С использованием reduce
result = reduce(lambda x, y: x + y, matrix)
print(result)