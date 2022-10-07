#!/bin/python3

# Variables and Methods
quote = "All is fair in love and war."

print()
print("Quote to manipulate: ", quote)
print()

# Print can be in upper case via ".upper()"
print(".upper():", end = ' ')
print(quote.upper())

# as well as lower via ".lower()"
print(".lower():", quote.lower())

# and Title Case ".title()"
print(".title(): ", quote.title())

# I can also print the length!
print("len():", end = ' ')
print(len(quote))

print()
print()
print("Example of printing using preset variables: ")
print()

name = "Mindy" # string
age = 20 # not really... int(20)
gpa = 5.0 # ha.. float(5.0)

print("My name is " + name + " and I am " + str(age) + " years old.")
print()
print()

# Important reminder:
print("Don't forget to turn integers into strings with str(your_int) before concatenating!")