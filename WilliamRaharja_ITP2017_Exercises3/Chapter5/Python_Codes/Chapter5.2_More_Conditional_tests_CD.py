'''
5-2. More Conditional Tests: You don’t have to limit the number of tests you
create to 10 If you want to try more comparisons, write more tests and add
them to conditional_tests.py Have at least one True and one False result for
each of the following:
•	 Tests for equality and inequality with strings
•	 Tests using the lower() function
•	 Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
•	 Tests using the and keyword and the or keyword
•	 Test whether an item is in a list
•	 Test whether an item is not in a list
'''
food = ['Pizza' , 'French Fries' , 'Fried Chicken']
in_food = 'Pizza'
not_food = 'Cap Chai'

if in_food in food:
    print ("There is", in_food, "inside", food)
if not_food in food:
    print ("There is no", not_food,"inside", food)
print("\n")
print('---------------------------------------')
check="Junkfoods!"
print(check == "Capchai!")
print(check != "Capchai!")
print(check == "Junkfoods!")
print(check != "Junkfoods!")
print('---------------------------------------')
print(check.lower() == "junkfoods!")
print(check.lower() != "junkfoods!")
print(check.lower() == "capchai!")
print(check.lower() != "capchai!")
print('---------------------------------------')
no = 12
print(no == 12)
print(no != 12)
print(no > 12)
print(no < 12)
print(no >= 12)
print(no <= 12)
print('---------------------------------------')
print(no == 22)
print(no != 22)
print(no > 22)
print(no < 22)
print(no >= 22)
print(no <= 22)
print('---------------------------------------')
no1 = 1
no2 = 2
print (no1 == 1 and no2 == 2)
print (no1 == 1 and no2 != 2)
print (no1 > 1 and no2 == 2)
print (no1 > 1 and no2 != 2)
print (no1 < 1 and no2 == 2)
print (no1 < 1 and no2 != 2)
print('---------------------------------------')
print (no1 == 1 or no2 == 2)
print (no1 == 1 or no2 != 2)
print (no1 > 1 or no2 == 2)
print (no1 > 1 or no2 != 2)
print (no1 < 1 or no2 == 2)
print (no1 < 1 or no2 != 2)
print('---------------------------------------')
shinigami_list = ['Adolf Hitler' , 'Joseph Stalin' , 'Kim Jong Il']
not_ded_yet = 'Donald Trump'

'Adolf Hitler' in shinigami_list
'Adolf Hitler' not in shinigami_list
'Donald Trump' in shinigami_list
'Donald Trump' not in shinigami_list
print('---------------------------------------')
if shinigami_list[0] in shinigami_list:
    print("Finally! ' " +shinigami_list[0],"'is perished yet.")
if not_ded_yet not in shinigami_list:
    print("Unfortunately ' " +not_ded_yet,"'is not perished yet.")
else:
    print("The world is still burning until now..")
