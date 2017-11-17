'''
Exercise 6
Rewrite the calculator function from Exercise 5
so that it takes any number of number parameters as well as the same optional keyword parameters.
The function should apply the operation to the first two numbers,
and then apply it again to the result and the next number, and so on.
For example, if the numbers are 6, 4,  9 and 1 
and the operation is subtraction the function should return 6 - 4 - 9 - 1.
If only one number is entered, it should be returned unmodified.
If no numbers are entered, raise an exception.


def calculator(op = "+",form = "float",*numbers):
    if len(numbers) < 2:
        raise ValueError
        if op == "+":
            for x in numbers[1:]:
                hasil += x
        elif op == "-":
            for x in numbers[1:]:
                hasil -= x
        elif op == ":":
            for x in numbers[1:]:
                hasil /= x
        elif op == "x":
            for x in numbers[1:]:
                hasil *= x
        else:
            for x in numbers[1:]:
                hasil += x

        if form == "integer":
            print(int(round(hasil)))
        if form == "float":
            print(float(hasil))

def check(numbz):
    list = []
    if numbz == "":
        return list
    elif len(numbz) == 1:
        list.append(int(numbz))
        return list
    elif numbz == " ":
        numbz = numbz.split(" ")
        for x in numbz:
            if "." not in x:
                list.append(int(x))
            elif "." in x:
                list.append(float(x))
        return list
    elif numbz == ",":
        numbz = numbz.split(",")
        for x in numbz:
            if "." not in x:
                list.append(int(x))
            elif "." in x:
                list.append(float(x))
        return list
    elif "." in numbz:
        list.append(float(numbz))
        return list
print(calculator('', '', 5, 5, 5))

'''
i = 0
def calculator(operator = "+" , o_format = float , *numbers):
    result = numbers[0] #to assign the index[0] variable[numbers] into [result] variable
    print("Your first number: ", result)
    if len(numbers) < 2:
        raise ValueError
    for x in numbers[1:]: #to slice the first parameter
        global i
        global n
        if operator == "+":
            result += x
            print("+", result) #to check every single digit of the addition calculation
        elif operator == "-":
            result -= x
            print("-", result) #to check every single digit of the subtraction calculation
        elif operator == ":":
            result /= x
            print(":", result) #to check every single digit of the modulus calculation
        elif operator == "x":
            result *= x
            print("x", result) #to check every single digit of the timing calculation
        else:
            raise ValueError
        if o_format == float:
            print("Your desired outcome: ", float(result))
        elif o_format == int:
            print("Your desired outcome: ", int(result))
        else:
            raise ValueError
    print("final integer:", round(result)) #to check the all calculation outcome in rounded integer
    print("final float: ", float(result)) #to check the all calculation outcome in float
    return result #printing the outcome of all calculation by calling [result] variable

#test
#print(calculator("+", int, 5, 15, 30))
#print(calculator("+", float, 5, 5, 5))
#print(calculator("-", int, 5,10,100))
#print(calculator("-", float, 5,10,100))
#print(calculator(":", int, 5,10,100))
#print(calculator(":", float, 5,10,100))
#print(calculator("x", int, 5,10,15))
#print(calculator("x", float, 5,10,15))

#Referenced with Sherlyn & Vincent Exercise_6 work
