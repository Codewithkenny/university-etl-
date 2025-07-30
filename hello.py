# greeting = 'Hello World!'
# print(greeting)

meaning = 42
# print('')

# if meaning > 10:
#     print('The answer is greater than 42')
# else:
#     print('The answer is less than or equal to 42')

print('The answer is greater than 42') if meaning > 10 else print('The answer is less than or equal to 42')  # This is a ternary    

# concatenation
firstname = 'Dave'
lastname = 'Gray'

fullname = firstname + " " + lastname
print(fullname)

fullname += " Jr."
print(fullname)

# Cating a number to a string
decade = str(1980)
print(type(decade))
print(decade)
print(decade + "s")  # This will print the 1980s

statement = "I was born in the year " + decade + "s."
print(statement)

# Multiple lines
multiline = ''''
Hey, how are you?


I was just checking in.

                                 All good?

'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods
first = 'Hello Data!'
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline) 

print(len(multiline))
multiline += "                                                "
multiline = "                           " + multiline
print(len(multiline))

print(len(multiline.strip())) 
print(len(multiline.lstrip())) 
print(len(multiline.rstrip())) 

print("")

# build a menu
title = "menu".upper()
print(title.center(20, "="))
print("coffee".ljust(16, ".") + " $2.00")
print("muffin".ljust(16, ".") + " $1.45")
print("sourbet".ljust(16, ".") + " $3.00")

print("")

# String index value
print(first[0])
print(first[-1])
print(first[1:])

# Some methods return boolean data
print(first.startswith("Hello"))
print(first.endswith("!"))

# Boolean data types
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data types
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))