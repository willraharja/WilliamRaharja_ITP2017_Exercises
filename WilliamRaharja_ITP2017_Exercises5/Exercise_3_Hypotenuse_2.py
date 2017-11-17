'''
Exercise 3
1. Rewrite the hypotenuse function from exercise 2 so that it returns a value instead of printing it.
2. Add exception handling so that the function returns None if it is called with parameters of the wrong type.
3. Call the function with two numbers, and print the result.
4. Call the function with two strings, and print the result.
5. Call the function with a number and a string, and print the result.
'''
#using return function to return back the value to None
def hypotenuse(x , y):
    import math
    try:
        a = math.sqrt(x+y)
        b = ((x+y)**0.5)
        return a , b
    except TypeError:
        return None
result = hypotenuse(2 , 23)
print("The result by using math function:", result[0],"\nThe result by using mathematical calculation:", result[1])
result = hypotenuse('2' , '23')
print(result)
result = hypotenuse('2' , '23')
print(result)
