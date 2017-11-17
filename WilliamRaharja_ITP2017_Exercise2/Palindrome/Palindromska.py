#This is a program to check whether your word is a palindrome or not
print ("Welcome to the Palindrome checker code ver0.01")
pal = input("Please input your word: ").lower()
print(pal)
print(pal[0])
print(pal[-1])
print(reversed(pal)) #will reversed Pal and then call it assigned memory address
print('_'.join(reversed(pal)))
'''will reversed pal and then join Pal with
    other string data or assigned text(e.g. '_')
    to make one single-united variable'''
if str(pal) == ''.join(reversed(pal)):
    print("It is a Palindrome!")
else:
    print("It is NOT a Palindrome!")

input("Please ENTER to Exit!")
#Reference:  Excelino.Fernando
