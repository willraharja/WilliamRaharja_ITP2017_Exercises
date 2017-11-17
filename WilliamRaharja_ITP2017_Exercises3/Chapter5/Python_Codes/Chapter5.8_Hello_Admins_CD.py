'''
5-8. Hello Admin: Make a list of fve or more usernames, including the name
'admin' Imagine you are writing code that will print a greeting to each user
after they log in to a website Loop through the list, and print a greeting to
each user:
•	 If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?
•	 Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.
'''
usernames = ['admin' , 'gahara013' , 'theextremistz1' , 'hunterzxx' , 'supermnz']
for usernames in usernames:
    if 'admin' in usernames:
        print('Welcome, ADMIN! Would you like to see a status report?')
        print('---------------------------------------')
    else:
        print('Hello! '+usernames.upper() , 'Thank you for logging in again!')
        print('---------------------------------------')
