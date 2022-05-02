# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 11:57:28 2022

@author: rahul
"""

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)

fruits = ["apple", "banana", "cherry"]
x = fruits.count("cherry")
print(x)

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

fruits = [ 'apple', 'banana', 'cherry']
x = fruits.index('cherry')
print(x)

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, 'orange')
print(fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.remove('banana')
print(fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)



