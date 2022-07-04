
# 1. Write a Python program to print Hello Python?
class print_hello:
    def say_hello(self):
        return 'Hello Python'

say_hello = print_hello()

print(say_hello.say_hello())


# 2. Write a Python program to do arithmetical operations addition and division.?
class arthematic1:
    def __init__(self, num1):
        self.num1 = num1

add = (arthematic1(100).num1 + arthematic1(1000).num1)

subtract = arthematic1(100).num1 - arthematic1(1000).num1

multiply = arthematic1(100).num1 * arthematic1(1000).num1
print(add,subtract,multiply)

try :
    div = arthematic1(10).num1 / arthematic1(12).num1
    print(div)
except Exception as e:
    print(Exception)


# 3. Write a Python program to find the area of a triangle?
class are_of_triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def find_area(self):
        area_of_triangle = 1/2 * self.base * self.height
        return area_of_triangle

dimension = are_of_triangle(10,10)
print(dimension.find_area())

# 4. Write a Python program to swap two variables?
a = 10
b = a
print(b)

# 5. Write a Python program to generate a random number?
import random


class random_number_generator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def return_random(self):
        return random.randint(self.a,self.b)

random_numbers = random_number_generator(1,10)

print(random_numbers.return_random())