'''
3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations You’ll have to think of
someone else to invite
•	 Start with your program from Exercise 3-4 Add a print statement at the
end of your program stating the name of the guest who can’t make it
•	 Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting
•	 Print a second set of invitation messages, one for each person who is still
in your list.
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
