def negara_api(x,y):
    return x + y

def decorator(main_func, logfilename = "log.txt"):
    def new_function(x,y):
        result = main_func(x,y)
        with open(logfilename, "w") as logfile:
            logfile.write("Long time ago, %s was once called as the MAIN evil headache function.\n"
                          "and then %s disappeared.\nNow, after thousand years and slightly backpain.\n"
                          "we found the True of%s.\n"
                          "There will be a lot of challenge.\n"
                          "Nevertheless, I believe that %s will come over it.." % (main_func.__name__,x,y,result))
        return result
    return new_function
new_function = decorator(negara_api)
print(new_function("Edgar"," the Makassar"))
#If you're doing the wrong indent, your result will not be printed or will be assumed as NoneType
