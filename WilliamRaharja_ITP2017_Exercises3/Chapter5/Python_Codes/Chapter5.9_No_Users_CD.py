'''
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty
•	 If the list is empty, print the message We need to fnd some users!
•	 Remove all of the usernames from your list, and make sure the correct
message is printed.
'''
usernames = []

if usernames == []:
    print("we need to find some users!".upper())
