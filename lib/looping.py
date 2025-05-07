#!/usr/bin/env python3

def happy_new_year(n=10):
    while n > 0:
        print(n)
        n -= 1
    print("Happy New Year!")

def square_integers(int_list):
    squared = []
    for num in int_list:
        squared.append(num ** 2)
    return squared

def fizzbuzz():
    for x in range(1, 101):
        if x % 15 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)
