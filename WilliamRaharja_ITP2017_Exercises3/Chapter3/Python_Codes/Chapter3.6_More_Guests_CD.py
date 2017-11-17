'''
3-6. More Guests: You just found a bigger dinner table, so now more space is
available Think of three more guests to invite to dinner
•	 Start with your program from Exercise 3-4 or Exercise 3-5 Add a print
statement to the end of your program informing people that you found a
bigger dinner table
•	 Use insert() to add one new guest to the beginning of your list
•	 Use insert() to add one new guest to the middle of your list
•	 Use append() to add one new guest to the end of your list
•	 Print a new set of invitation messages, one for each person in your list.
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

    #Chapter3.5_Changing_Guest_List.py/ExcelinoFernando
del ppl[2]
ppl.append("Tim Cook")
print("These are the revised letters:"
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
print("-------------------------------\n"
      "Issue: NoNe!\n"
      "Information: Founded! One(1)\n"
      "We found a bigger ship and table to accomodate more people"
      "\n-------------------------------\n\n"
      )

#Chapter3.6_More_Guests
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
