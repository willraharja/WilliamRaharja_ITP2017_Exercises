'''
3-11. Intentional Error: If you haven’t received an index error in one of your
programs yet, try to make one happen Change an index in one of your programs to
produce an index error Make sure you correct the error before closing the program.
'''

brand = ['Asus', 'Apple', 'Dell', 'HP']
print("-------------------------------")
print ("The name of brands that currently in the list: " +str(brand))
print("The number of brands that currently in the list: ")
len(brand) #len is not showing the number of listing
print("-------------------------------")
brand.insert(0 , "LG")
brand.insert(2 , "Microsoft")
brand.append("Macbook")
'''
brand.append("Mcbook")
Error in here/Because of typo
'''
print ("The name of brands that currently in the list: " +str(brand))
print("The number of brands that currently in the list: ")
len(brand) #len is not showing the number of listing
print("-------------------------------")
print ("Here's the original list    #1: " +str(brand))
print ("Here's the sorted list      #2: " +str(sorted(brand)))
print ("Here's the original list    #3: " +str(brand))
print ("Here's the reversed list    #4: " +str(sorted(brand , reverse = True)))
print ("Here's the original list    #5: " +str(brand))
brand.reverse()
print ("Here's the reversed list    #6: " +str(brand))
brand.sort()
print ("Here's the sorted list      #8: " +str(brand))
print("-------------------------------")
print("The name of brands that supposed not to be inside the list: " +str(brand[-1] +", " +str(brand[4] +" & "
        +str(brand[5]))))
print("-------------------------------")
brand.remove('Macbook')
print ("The name of brands that currently in the list: " +str(brand))
print("The number of brands that currently in the list: ")
len(brand) #len is not showing the number of listing
print("-------------------------------")
del brand[-1]
print ("The name of brands that currently in the list: " +str(brand))
print("The number of brands that currently in the list: ")
len(brand) #len is not showing the number of listing
print("-------------------------------")
brand.pop(4)
print ("The name of brands that currently in the list: " +str(brand))
print("The number of brands that currently in the list: ")
len(brand) #len is not showing the number of listing
print("-------------------------------\n")
