'''
4-13. Buffet: A buffet-style restaurant offers only fve basic foods Think of fve
simple foods, and store them in a tuple
•	 Use a for loop to print each food the restaurant offers
•	 Try to modify one of the items, and make sure that Python rejects the
change
•	 The restaurant changes its menu, replacing two of the items with different
foods Add a block of code that rewrites the tuple, and then use a for
loop to print each of the items on the revised menu.
'''
Cheap_S = ('Water' , 'Mineral Water' , 'Well Water' , 'White Water' , 'Alkaline Water')
print ("the cheapskate restaurant".title())
print ('-------------------------------')
print ("These are The Cheapskate Restaurant's restaurant menu: ")
for menu in Cheap_S:
    print(' *', menu)
print ('-------------------------------')
Cheap_S = ('Water' , 'Mineral Water' , 'Well Water' , 'Ordinary Water' , 'Slightly Mineral Water')
print("We've updated our menu!\nThese are The Cheapskate Restaurant's NEW restaurant menu: ")
for menu in Cheap_S:
    print(' *', menu)
