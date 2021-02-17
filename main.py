# Tuple items are enclosed in round brackets 
# Tuple is ordered 
# Tuple is immutable (different from lists that are mutable)
# Tuple elements do no need to be unique 
# Elements can be of different data Type 

''' Creating Tuple '''

# tuple = ()
# tuple = ('cat', [4,4,2,1,6], (1,2,3))
# tuple = 1234, 5678
# tuple = 'hello' #Not a tuple just a string
# tuple = 'hello',
# tuple = ('hello') # Also not a tuple just a string 
# tuple = ('hello',)
# print(tuple)

''' Access Tuple Elements '''

# tuple = (12345, 4321, 'hello', [7,8,9], (0,9,8,7))
# print(tuple[0])
# print(tuple[-2])

''' Slicing Tuples in Python '''

# tuple = (('orange', 'banana'), 12345, [5,6,7], ('carrot', 'kale'))
# # print(tuple[:])
# # print(tuple[2:])
# # print(tuple[2:5])
# print(tuple[::2])


''' Changing a Tuple '''

# fruits = ('apple', 'banana', 'orange', 'lemon', 'grapes')
# fruits [0] = 'pear' # TypeError: 'tuple' object does not support item assignment

''' Deleting a Tuple '''

# fruits = ('apple', 'banana', 'orange', 'lemon', 'grapes')
# del fruits[0] # TypeError: 'tuple' object doesn't support item deletion
# print(fruits)

# del fruits
# print(fruits) # NameError: name 'fruits' is not defined (deleted successfuly)

''' Tuple Methods '''
# print(dir(tuple)) # only two methods (count and index)

# fruits = ('apple', 'banana', 'orange', 'lemon', 'grapes')
# print(fruits.count('orange'))
# print(fruits.index('lemon'))
