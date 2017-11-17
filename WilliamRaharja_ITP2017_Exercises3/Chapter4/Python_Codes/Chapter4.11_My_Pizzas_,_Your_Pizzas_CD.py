'''
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
(page 60) Make a copy of the list of pizzas, and call it friend_pizzas
Then, do the following:
•	 Add a new pizza to the original list
•	 Add a different pizza to the list friend_pizzas
•	 Prove that you have two separate lists Print the message, My favorite
pizzas are:, and then use a for loop to print the frst list Print the message,
My friend’s favorite pizzas are:,
and then use a for loop to print the second list Make sure each new pizza is stored in the appropriate list.
'''
#Chapter4.1_Pizzas
Pizzas = ['pizza hut' , 'domino', 'old town pizza' ]
print ('-------------------------------')
for Pizza in Pizzas:
    print(Pizza.upper())
print ('-------------------------------')
for Pizza in Pizzas:
    print(Pizza.title() + ", I'd like to order a Durian Pizza.")
print ('\nI like Durian Pizza because it is unique.\nI really like Pizza!\nEspecially when I can afford to buy it!!')
print ('-------------------------------')
#Chapter_4.11_My_Pizzas_Your_Pizzas
F_Pizzas = Pizzas[:]
Pizzas.append('krusty krab pizza')
F_Pizzas.append('chumbucket')
print ("My favourite pizzas are: ")
for Pizza in Pizzas:
    print(Pizza.title())
print ('-------------------------------')
print ("My friend favourite pizzas are: ")
for Pizza in F_Pizzas:
    print(Pizza.title())
print ('-------------------------------')
