""" Problem 1
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl',
your program should print:

Number of vowels: 5
"""

s = 'azcbobobegghakl'
count = 0

for char in s:

    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        count += 1

print (count)

""" Problem 2

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print:

Number of times bob occurs is: 2
"""

s = 'azcbobobegghakl'
i = 0
count = 0

while i < len(s):

    if s[i:i+3] == "bob":
        count += 1
    i += 1
print (count)

""" Problem 3

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur
in alphabetical order. For example, if s = 'azcbobobegghakl', then your program
should print:

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd',
then your program should print:

Longest substring in alphabetical order is: abc
"""
