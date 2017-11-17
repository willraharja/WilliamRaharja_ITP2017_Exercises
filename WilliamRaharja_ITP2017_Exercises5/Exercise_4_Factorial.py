'''
Write a recursive function which calculates the factorial of a given number.
Use exception handling to raise an appropriate exception if the input parameter is not a positive integer,
but allow the user to enter floats as long as they are whole numbers.
'''
def recur(n , form):
    try:
        if n == 1:
            return 1
        if form == "integer":
            return int(int(n)*recur(int(n)-1,form))
        if form == "float":
            return float(int(n)*recur(int(n)-1,form))
        elif form != "integer" and form != "float":
            print("Please, input the correct format!")
    except RecursionError:
        return None
    except (TypeError , ValueError):
        print("Please, input the data correctly!")
        return False
inp_form = input("Please, input the format you desire <float or integer>: ")
inp_num = int(input("Please, input your number in INTEGER: "))
print(recur(inp_num , inp_form))
input("Press 'ENTER' to Exit!")
