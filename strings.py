# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 14:21:24 2022

@author: rahul
"""

txt = 'hello, and welcome to my world.'
x = txt.capitalize()
print (x)

txt = 'Hello, and welcome to my world.'
x = txt.casefold()
print(x)

txt = 'banana'
x = txt.center(20)
print(x)

txt = 'I love apples, apples are my favorite food.'
x = txt.count('apples')
print(x)

txt = 'My name is Ståle'
x = txt.encode()
print(x)

txt = 'Hello, and welcome to my world.'
x = txt.endswith('.')
print(x)

txt = 'H\te\tl\tl\to'
x = txt.expandtabs(2)
print(x)

txt = 'Hello, and welcome to my world.'
x = txt.find('welcome')
print(x)

txt = 'For only {price:.2f} dollars!'
print(txt.format(price = 49))

txt = 'Hello, and welcome to my world'
x = txt.index('welcome')
print(x)

txt = 'Company12'
x = txt.isalnum()
print(x)

txt = '54600'
x = txt.isdecimal()
print(x)

txt = '54699'
x = txt.isdigit()
print(x)

txt = 'Demo'
x = txt.isidentifier()
print(x)

txt = 'hello, and welcome to my world.'
x = txt.islower()
print(x)

txt = '67485'
x = txt.isnumeric()
print(x)

txt = 'Hello, are you #1!'
x = txt.isprintable()
print(x)

txt = '   '
x = txt.isspace()
print(x)

txt = 'Hello, And Welcome To My World!'
x = txt.istitle()
print(x)

txt = 'THIS IS NOW!'
x = txt.isupper()
print(x)

myTuple = ('John', 'Peter', 'Vicky')
x = '#'.join(myTuple)
print(x)

txt = 'banana'
x = txt.ljust(20)
print(x, 'is my favorite fruit.')

txt ='Hello my FRIENDS'
x = txt.lower()
print(x)

txt = '     banana     '
x = txt.lstrip()
print('of all fruits', x, 'is my favorite fruit')

txt = 'Hello Sam!'
mytable = txt.maketrans('S', 'P')
print(txt.translate(mytable))

txt = 'I could eat bananas all day'
x = txt.partition('bananas')
print(x)

txt = 'I like bananas'
x = txt.replace('bananas', 'apples')
print(x)

txt = 'Mi casa, su casa.'
x = txt.rfind('casa')
print (x)

txt = 'Mi casa, su casa.'
x = txt.rindex('casa') 
print(x)

txt = 'banana'
x = txt.rjust(20)
print(x, 'is my favorite fruit.')

txt = 'I could eat bananas all day, bananas are my favorite fruit'
x = txt.rpartition('bananas')
print(x)

txt = 'apple, banana, cherry'
x = txt.rsplit(', ')
print(x)

txt = '     banana     '
x = txt.rstrip()
print('of all fruits', x, 'is my favorite')

txt = 'welcome to the jungle'
x = txt.split()
print(x)

txt = 'Thank you the for the music\nWelcome to the jungle'
x = txt.splitlines()
print(x)

txt = 'Hello, and welcome to my world.'
x = txt.startswith('Hello')
print(x)

txt = '     banana     '
x = txt.strip()
print('of all fruits', x, 'is my favorite')

txt = 'Hello My Name Is Peter'
x = txt.swapcase()
print(x)

txt = 'Welcome to my world'
x = txt.title()
print(x)

#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83: 80}    
txt = 'Hello Sam!'
print(txt.translate(mydict))

txt = 'Hello my friends'
x = txt.upper()
print(x)

txt = '50'
x = txt.zfill(10)
print(x)

