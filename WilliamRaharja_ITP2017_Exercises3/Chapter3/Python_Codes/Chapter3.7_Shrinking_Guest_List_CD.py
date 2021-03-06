'''
3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests
•	 Start with your program from Exercise 3-6 Add a new line that prints a
message saying that you can invite only two people for dinner
•	 Use pop() to remove guests from your list one at a time until only two
names remain in your list Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner
•	 Print a message to each of the two people still on your list, letting them
know they’re still invited
•	 Use del to remove the last two names from your list, so you have an empty
list Print your list to make sure you actually have an empty list at the end
of your program.
'''
#Chapter3.6_More_Guests
ppl = ['Elon Musk' , 'Bill Gates' , 'Tim Cook']
ppl.insert(0 , "William Tanuwijaya")
ppl.insert(2 , "Kevin Osmond")
ppl.append("Calvin Kizana")
print("These are the revised FINAL letters:"
      "\n-------------------------------\n")
print("Dear, "+ppl[0], ".\nThe honour of your presence\nis requested at a \nDinner & Tech Discussion"
                       "\naboard the The Slightly Bigger Yacht\nSunday, November 12th, 2017\nfrom 7 p.m. until 10 p.m."
                       "\nEmbarking from Dock 'F'\nSlip No. 66\nTanjung Priok Harbour, Jakarta\n\nCasual attire"
                       "\n\nThe ExcelInTech Group\n"
                       "-------------------------------\n")
print("Dear, "+ppl[1], ".\nThe honour of your presence\nis requested at a \nDinner & Tech Discussion"
                       "\naboard The Slightly Bigger Yacht\nSunday, November 12th, 2017\nfrom 7 p.m. until 10 p.m."
                       "\nEmbarking from Dock 'F'\nSlip No. 66\nTanjung Priok Harbour, Jakarta\n\nCasual attire"
                       "\n\nThe ExcelInTech Group\n"
                       "-------------------------------\n")
print("Dear, "+ppl[2], ".\nThe honour of your presence\nis requested at a \nDinner & Tech Discussion"
                       "\naboard The Slightly Bigger Yacht\nSunday, November 12th, 2017\nfrom 7 p.m. until 10 p.m."
                       "\nEmbarking from Dock 'F'\nSlip No. 66\nTanjung Priok Harbour, Jakarta\n\nCasual attire"
                       "\n\nThe ExcelInTech Group\n"
                       "-------------------------------\n")
print("Dear, "+ppl[3], ".\nThe honour of your presence\nis requested at a \nDinner & Tech Discussion"
                       "\naboard the The Slightly Bigger Yacht\nSunday, November 12th, 2017\nfrom 7 p.m. until 10 p.m."
                       "\nEmbarking from Dock 'F'\nSlip No. 66\nTanjung Priok Harbour, Jakarta\n\nCasual attire"
                       "\n\nThe ExcelInTech Group\n"
                       "-------------------------------\n")
print("Dear, "+ppl[4], ".\nThe honour of your presence\nis requested at a \nDinner & Tech Discussion"
                       "\naboard The Slightly Bigger Yacht\nSunday, November 12th, 2017\nfrom 7 p.m. until 10 p.m."
                       "\nEmbarking from Dock 'F'\nSlip No. 66\nTanjung Priok Harbour, Jakarta\n\nCasual attire"
                       "\n\nThe ExcelInTech Group\n"
                       "-------------------------------\n")
print("Dear, "+ppl[5], ".\nThe honour of your presence\nis requested at a \nDinner & Tech Discussion"
                       "\naboard The Slightly Bigger Yacht\nSunday, November 12th, 2017\nfrom 7 p.m. until 10 p.m."
                       "\nEmbarking from Dock 'F'\nSlip No. 66\nTanjung Priok Harbour, Jakarta\n\nCasual attire"
                       "\n\nThe ExcelInTech Group\n"
                       "-------------------------------\n")

#Chapter3.7_Shrinking_Guest_List
print("Dear, "+ppl[0],".\nWe're really sorry to inform you that \nthe 'Dinner & Tech Discussion'"
                      "\nwhich is going to be held on the \nNovember 12th, 2017 \nwill be cancelled"
                      " due to some technical issues.\nYour understanding is much appreciated.\n"
                      "\nThe ExcelInTechGroup\n"
                      "-------------------------------\n")
ppl.pop(0)
print("Dear, "+ppl[1],".\nWe're really sorry to inform you that \nthe 'Dinner & Tech Discussion'"
                      "\nwhich is going to be held on the \nNovember 12th, 2017 \nwill be cancelled"
                      " due to some technical issues.\nYour understanding is much appreciated.\n"
                      "\nThe ExcelInTechGroup\n"
                      "-------------------------------\n")
ppl.pop(1)
print("Dear, "+ppl[-1],".\nWe're really sorry to inform you that \nthe 'Dinner & Tech Discussion'"
                      "\nwhich is going to be held on the \nNovember 12th, 2017 \nwill be cancelled"
                      " due to some technical issues.\nYour understanding is much appreciated.\n"
                      "\nThe ExcelInTechGroup\n"
                      "-------------------------------\n")
ppl.pop(-1)
print("Dear, "+ppl[2],".\nWe're really sorry to inform you that \nthe 'Dinner & Tech Discussion'"
                      "\nwhich is going to be held on the \nNovember 12th, 2017 \nwill be cancelled"
                      " due to some technical issues.\nYour understanding is much appreciated.\n"
                      "\nThe ExcelInTechGroup\n"
                      "-------------------------------\n")
ppl.pop(2)
print("Dear, "+ppl[0], ".\nThe honour of your presence\nis STILL requested at a \nDinner & Tech Discussion"
                       "\n\nThe ExcelInTech Group\n"
                       "-------------------------------\n")
print("Dear, "+ppl[1], ".\nThe honour of your presence\nis STILL requested at a \nDinner & Tech Discussion"

                       "\n\nThe ExcelInTech Group\n"
                       "-------------------------------\n")

print("#1 The name in the list: ")
print(ppl)
del ppl[0]
print("#2 The name in the list: ")
print(ppl)
del ppl[0]
print("#3 The name in the list: ")
print(ppl)

