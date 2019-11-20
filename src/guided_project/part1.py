print("Hello, world!")
# declaring a variable
name = "Austen"

CONST_NAME = ''

print(name)

# string concatenation
print("Hello " + name)

# f-strings // format strings
# f-strings replaces formats %
print(f'Hello, {name}')

# create a list with some numbers // same as array in js
q = [10, 15, 20, 5]

list_of_zeros = [0] * 10
print(list_of_zeros)


# add an element to q
q.append(3)
print(q)


# print all values in each list
for elem in q:
    print(elem)



# using list comprehensions...
numbers = [1, 2, 3, 4, 5]
# create a new list containing the squares of all values in 'numbers'
# loop over each number in numbers
    # take each number, and just n * n
    # add to new list

squares = [num*num for num in numbers]
print(numbers)
print(squares)


# create a new list containing only the even values of 'numbers'
evens = [num for num in numbers if num % 2 == 0]
print(evens)


# create a new list containing only the names that starts with 's' 
# so that they are properly capitalized
# regardless of how the name originally appears
names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy", "shawn"]
s_names = [name.capitalize() for name in names if name[0].lower() == 's' ]
print(s_names)



# create an empty dictionary

d = {}



# create a dictionary with at least two keys : value pairs

d = {
    "apple" : 'is a fruit',
    'cucumber' : 'is a vegetable'
}

fruit = 'apple'
print(d[fruit])

print(d.keys())
print(d.values())

alphabet = [{'a': 'anchor'}, {'b': 'bat'}, {'c': 'cat'}]
print(alphabet[0])

d['apple'] = 'is the best fruit'
print(d)

# iterate through dictionary

print(d.items())

for key, value in d.items():
    print(f'{key} : {value}')

for pair in d.items():
    print(pair[0] + pair[1])



# sets 
# sets are unordered and does not include duplicate item
# uses { }

fruits = {'apple', 'banana', 'cherry'}
print(fruits)
fruits.add('tomato')
fruits.add('apple')
print(fruits)
print('banana' in fruits)

# tuple 
# keeps order but immutable
# uses ()

animals = ('dog', 'cat', 'monkey', 'rabbit')
print(animals)
print(animals[0])
print('dog' in animals)

for animal in animals:
    print(animal)


single_tuple_str = ('one')
single_tuple = ('one', )
print(type(single_tuple))
print(single_tuple)

