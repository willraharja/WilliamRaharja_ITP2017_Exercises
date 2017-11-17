'''
5-10. Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username
•	 Make a list of fve or more usernames called current_users
•	 Make another list of fve usernames called new_users Make sure one or
two of the new usernames are also in the current_users list
•	 Loop through the new_users list to see if each new username has already
been used If it has, print a message that the person will need to enter a
new username If a username has not been used, print a message saying
that the username is available
•	 Make sure your comparison is case insensitive If 'John' has been used,
'JOHN' should not be accepted.
'''

usernames = ['arminzz' , 'gahara013' , 'theextremistz1' , 'hunterzxx' , 'supermnz']
new_usernames = ['ARMinzz' , 'sAHAara3' , 'theeXTremistz1' , 'preYz99' , 'lxlthorIZ1']
mke_low1 = [low1.lower() for low1 in usernames] #user variable to make the listing lowercases
for new_usernames in new_usernames:
    if new_usernames.lower() in mke_low1:
        print("The username of ' ", new_usernames, "' has been taken. Please enter a new username!")
        print('---------------------------------------')
    else:
        print("The username of ' ", new_usernames, "' is still avaiable! You can use it for your username!")
        print('---------------------------------------')
