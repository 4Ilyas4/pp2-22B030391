
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
#The price is 49 dollars

txt = "The price is {:.2f} dollars"
#The price is 49.00 dollars

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
#I want 3 pieces of item number 567 for 49.00 dollars.

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
# want 3 pieces of item number 567 for 49.00 dollars.

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
#His name is John. John is 36 years old.

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
#I have a Ford, it is a Mustang.


