 #python variables
  #1
x = 5
y = "John"
print(x)
print(y)
  #2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
  #3
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
  #4
x = 5
y = "John"
print(type(x))
print(type(y))
  #5
x = "John"
# is the same as
x = 'John'
  #6
a = 4
A = "Sally"
#A will not overwrite a
 #variable names
#legal
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
#illegal
"""
2myvar = "John"
my-var = "John"
my var = "John"
"""
#camel 
myVariableName = "John"
#Pascal
MyVariableName = "John"
#snake
my_variable_name = "John"
 #assign multiple values
#multiple
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#one value
x = y = z = "Orange"
print(x)
print(y)
print(z)
#unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

      #Exercise
  #1
carname = "Volvo"
  #2
x = 50
  #3
x = 5
y = 10
print(x + y)
  #4
x = 5 
y = 10
z = x + y 
print(z)
  #5
#was been: 2my-first_name = "John"
myfirst_name = "John"
  #6
x = y = z = "Orange"
  #7
x = "awesome"

def myfunc():
  global x
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
