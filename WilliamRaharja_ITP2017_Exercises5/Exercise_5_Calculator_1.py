'''
Write a function called calculator.
It should take the following parameters: two numbers, an arithmetic operation
(which can be addition, subtraction, multiplication or division and is addition by default),
and an output format (which can be integer or floating point, and is floating point by default).
Division should be floating-point division.
The function should perform the requested operation on the two input numbers,
and return a result in the requested format
(if the format is integer, the result should be rounded and not just truncated).
Raise exceptions as appropriate if any of the parameters passed to the function are invalid.
Call the function with the following sets of parameters, and check that the answer is what you expect:
2, 3.0
2, 3.0, output format is integer
2, 3.0, operation is division
2, 3.0, operation is division, output format is integer
'''

def calculator(n1 , n2 , op = "+" , form = "float"):
    try:
        if op == "+":
            hasil = int(n1)+int(n2)
        elif op == "-":
            hasil = int(n1)-int(n2)
        elif op == ":":
            hasil = int(n1)/int(n2)
        elif op == "x":
            hasil = int(n1)/int(n2)
        else:
            hasil = int(n1)+int(n2)

        if form == "integer":
            print(int(round(hasil)))
        if form == "float":
            print(float(hasil))
        elif form != "integer" and form != "float":
            print("Please, input the format!")

        return hasil
    except (ValueError,TypeError):
        print("Please, input the data correctly!")


#test
#calculator(2 , 3.0) #2, 3.0
#calculator(2 , 3.0 , "" , "integer") #2, 3.0, output format is integer
#calculator(2 , 3.0 , ":") #2, 3.0, operation is division
#calculator(2 , 3.0 , ":" , "integer") #2, 3.0, operation is division, output format is integer
