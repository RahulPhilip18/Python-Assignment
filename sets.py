# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 12:40:36 2022

@author: rahul
"""

thisset = {'apple', 'banana', 'cherry'}
thisset.add('orange')
print(thisset)

fruits = {'apple', 'banana', 'cherry'}
fruits.clear()
print(fruits)

fruits = {'apple', 'banana', 'cherry'}
x = fruits.copy()
print(x)

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.difference(y)
print(z)

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
x.difference_update(y)
print(x)

fruits = {'apple', 'banana', 'cherry'}
fruits.discard('banana')
print(fruits)

x = {'apple', 'banana', 'cherry'}
y = {'google, microsoft', 'apple'}
z = x.intersection(y)
print(z)

x = {'apple', 'banana', 'cherry'}
y = {'google, microsoft', 'apple'}
z = x.intersection_update(y)
print(x)

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'facebook'}
z = x.isdisjoint(y)
print(z)

x = {'a', 'b', 'c'}
y = {'f', 'e', 'd', 'c', 'b', 'a'}
z = x.issubset(y)
print(z)

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

fruits = {'apple', 'banana', 'cherry'}
fruits.pop()
print(fruits)

fruits = {'apple', 'banana', 'cherry'}
fruits.remove('banana')
print(fruits)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)