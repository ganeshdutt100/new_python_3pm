# # String 
# # '', "" , ''' '''

# a = "Hello World"
# print(a)
# print(type(a))

# b = 'Hello World'
# print(b)
# print(type(b))

# c = '''Hello 
#    Python
#  World'''
# print(c)
# print(type(c))

# text = "Hello"
# print(text[0])
# print(text[-1])

# String slicing 
# text = "pythonProgramming"

# print(text[3:6])
# print(text[:6])
# print(text[5:])
# print(text[::2])
# print(text[::-3])


# String Operations
# first  = "Hello"
# second = "world"

# result  = first  + " :  "+  second 
# print(result)

# String  Repetition

# print("python " * 10  )

# Membership Operators

# text  = "Hello Python "

# print("Hello" in text)



# print(len(text))

# String formatting 
# text  = "Hello python"
# name = "Ganesh Dutt"


# message  = f"My name is {name}"
# print(message)


# String Methods 
# text  ="hello world "
# print(text.strip())
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())

# text =  "apple, banana , orange "
# fruits = text.split(",")
# print(fruits)

# text  = "i love python "
# print(text.replace("python", "java"))
# print(text.find("python"))
# print(text.count("o"))

text  =  "234sdfgh"
print(text.isdigit())
print(text.isalpha())

print("12345".isdigit())
print("hgfdsdfghj".isalpha())
print("hello".islower())
print("PYTHONLOVEJAVA".isupper())
print("Hello".istitle())
