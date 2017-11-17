'''
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
through 3-7 (page 46), use len() to print a message indicating the number
of people you are inviting to dinner.
'''
#Chapter3.4_Guest_List.py/ExcelinoFernando
ppl = ['Elon Musk' , 'Bill Gates' , 'Steve Jobs']

print("Dear, "+ppl[0], ".\nThe honour of your presence\nis requested at a \nDinner & Tech Discussion"
                       "\naboard the The Little Yacht\nSunday, November 12th, 2017\nfrom 7 p.m. until 10 p.m."
                       "\nEmbarking from Dock 'F'\nSlip No. 66\nTanjung Priok Harbour, Jakarta\n\nCasual attire"
                       "\n\nThe ExcelInTech Group\n"
                       "-------------------------------\n")
print("Dear, "+ppl[1], ".\nThe honour of your presence\nis requested at a \nDinner & Tech Discussion"
                       "\naboard The Little Yacht\nSunday, November 12th, 2017\nfrom 7 p.m. until 10 p.m."
                       "\nEmbarking from Dock 'F'\nSlip No. 66\nTanjung Priok Harbour, Jakarta\n\nCasual attire"
                       "\n\nThe ExcelInTech Group\n"
                       "-------------------------------\n")
print("Dear, "+ppl[2], ".\nThe honour of your presence\nis requested at a \nDinner & Tech Discussion"
                       "\naboard The Little Yacht\nSunday, November 12th, 2017\nfrom 7 p.m. until 10 p.m."
                       "\nEmbarking from Dock 'F'\nSlip No. 66\nTanjung Priok Harbour, Jakarta\n\nCasual attire"
                       "\n\nThe ExcelInTech Group\n"
                       "-------------------------------\n")

print("-------------------------------\n"
      "Issue: Founded! One(1)\n".upper() +ppl[2].upper(),
      "could't come to the party due to some circumstances."
      "\nPlease, contact 'Tim Cook' for further information.".upper(),
      "\n-------------------------------\n\n"
      )

print("-------------------------------")
print("The number of people invited to the party: ")
len(ppl) #len is not showing the number of listing
print("-------------------------------\n")

#Chapter3.5_Changing_Guest_List.py/ExcelinoFernando
del ppl[2]
ppl.append("Tim Cook")
print("These are revised letters:"
      "\n-------------------------------\n")
print("Dear, "+ppl[0], ".\nThe honour of your presence\nis requested at a \nDinner & Tech Discussion"
                       "\naboard the The Little Yacht\nSunday, November 12th, 2017\nfrom 7 p.m. until 10 p.m."
                       "\nEmbarking from Dock 'F'\nSlip No. 66\nTanjung Priok Harbour, Jakarta\n\nCasual attire"
                       "\n\nThe ExcelInTech Group\n"
                       "-------------------------------\n")
print("Dear, "+ppl[1], ".\nThe honour of your presence\nis requested at a \nDinner & Tech Discussion"
                       "\naboard The Little Yacht\nSunday, November 12th, 2017\nfrom 7 p.m. until 10 p.m."
                       "\nEmbarking from Dock 'F'\nSlip No. 66\nTanjung Priok Harbour, Jakarta\n\nCasual attire"
                       "\n\nThe ExcelInTech Group\n"
                       "-------------------------------\n")
print("Dear, "+ppl[2], ".\nThe honour of your presence\nis requested at a \nDinner & Tech Discussion"
                       "\naboard The Little Yacht\nSunday, November 12th, 2017\nfrom 7 p.m. until 10 p.m."
                       "\nEmbarking from Dock 'F'\nSlip No. 66\nTanjung Priok Harbour, Jakarta\n\nCasual attire"
                       "\n\nThe ExcelInTech Group\n"
                       "-------------------------------\n")

print("-------------------------------")
print("The number of people invited to the party: ")
len(ppl) #len is not showing the number of listing
print("-------------------------------\n")

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

print("-------------------------------")
print("The number of people invited to the party: ")
len(ppl) #len is not showing the number of listing
print("-------------------------------\n")

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

print("-------------------------------")
print("The number of people invited to the party: ")
len(ppl) #len is not showing the number of listing
print("-------------------------------\n")
print("-------------------------------")
print("#1 The name in the list: ")
print(ppl)
print("-------------------------------")
del ppl[0]
print("#2 The name in the list: ")
print(ppl)
print("-------------------------------")
del ppl[0]
print("#3 The name in the list: ")
print(ppl)
print("-------------------------------\n")
print("-------------------------------")
print("The number of people invited to the party: ")
len(ppl) #len is not showing the number of listing
print("-------------------------------\n")
