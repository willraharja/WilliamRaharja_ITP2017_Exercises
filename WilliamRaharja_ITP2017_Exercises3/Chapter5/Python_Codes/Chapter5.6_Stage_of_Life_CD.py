'''
5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
stage of life Set a value for the variable age, and then:
•	 If the person is less than 2 years old, print a message that the person is
a baby
•	 If the person is at least 2 years old but less than 4, print a message that
the person is a toddler
•	 If the person is at least 4 years old but less than 13, print a message that
the person is a kid
•	 If the person is at least 13 years old but less than 20, print a message that
the person is a teenager
•	 If the person is at least 20 years old but less than 65, print a message that
the person is an adult
•	 If the person is age 65 or older, print a message that the person is an
elder.
'''
person = 20
if person < 2:
    print("You're a baby.")
elif person >= 2 and person < 4:
    print("You're a toddler.")
elif person >= 4 and person < 13:
    print("You're a kid.")
elif person >= 13 and person < 20:
    print("You're a teenager.")
elif person >= 20 and person < 65:
    print("You're an adult.")
else:
    print("You're an elder.")
