  #variable, x[0] = 2000, x[1] = 3200, x[2] = 7, x[3] = 5, x[-1] = 0
x = 2000, 3200, 7, 5, 0
text = ('The numbers that start from 2000 to 3200 which are divisible '
        'by 7 but are not a multiple of 5, are these:')
storage = [] #null list for storing the True listings

for final in range(x[0] , x[1]): #process in 'final' listing which range
                                    # ONLY from 2000 to 3200
    #If  "X" number mods 7, the score is 0
        # and If "X" number mods 5, the score is more than 0 then the condition is fulfilled/Yes
    if ((final % x[2]) == x[-1]) and ((final % x[3]) > x[-1]):
         #changing the final listing data
            # from integer to stringer and then inserting it to null
                # storage listing
        storage.append(str(final))
print(text)
print(', '.join(storage))#to join all of the key-listings into a single string

print("\n-------------------------------")
print("Thank you for using this program! Have a nice day! :)")
