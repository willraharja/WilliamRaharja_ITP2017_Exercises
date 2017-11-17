'''
5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif else chain
•	 If the alien is green, print a message that the player earned 5 points
•	 If the alien is yellow, print a message that the player earned 10 points
•	 If the alien is red, print a message that the player earned 15 points
•	 Write three versions of this program, making sure each message is printed
for the appropriate color alien.
'''
alien_color = 'green'
if 'green' in alien_color:
    print("You just earned 5 points.")
elif 'green' in alien_color:
    print("You just earned 10 points.")
else:
    print("You just earned 15 points.")
print('---------------------------------------')
alien_color = 'yellow'
if 'yellow' in alien_color:
    print("You just earned 10 points.")
elif 'yellow' in alien_color:
    print("You just earned 5 points.")
else:
    print("You just earned 15 points.")
print('---------------------------------------')
alien_color = 'red'
if 'red' in alien_color:
    print("You just earned 15 points.")
elif 'red' in alien_color:
    print("You just earned 10 points.")
else:
    print("You just earned 5 points.")
print('---------------------------------------')
