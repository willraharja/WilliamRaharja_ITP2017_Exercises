'''
4-10. Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
•	 Print the message, The frst three items in the list are: Then use a slice to
print the first three items from that program’s list
•	 Print the message, Three items from the middle of the list are: Use a slice
to print three items from the middle of the list
•	 Print the message, The last three items in the list are: Use a slice to print
the last three items in the list.
'''
Places = ['Belarus' , 'Antarctica' , 'Ecuador' , 'Denmark' , 'Canada']
print ("These are the items in the list:                    ", Places)
print ("The first three items in the list are:              ", Places[:3])
print ("The three items from the middle of the list are:    ", Places[1:-1])
print ("The last three items in the list are:               ", Places[-3:])
