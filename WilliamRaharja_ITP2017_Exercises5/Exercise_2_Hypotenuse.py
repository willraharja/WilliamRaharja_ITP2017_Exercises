'''
Exercise 2
1. Create a function called hypotenuse, which takes two numbers as parameters
and prints the square root of the sum of their squares.
2. Call this function with two floats.
3. Call this function with two integers.
4. Call this function with one integer and one float.
'''
def hypotenuse(x , y):
    import math
    print(math.sqrt(x+y))
    print((x+y)**0.5)
hypotenuse(2.0,23.0)
hypotenuse(2,7)
hypotenuse(1,15.0)
