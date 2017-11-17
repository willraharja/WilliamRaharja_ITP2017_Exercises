'''
4-1. Pizzas: Think of at least three kinds of your favorite pizza Store these
pizza names in a list, and then use a for loop to print the name of each pizza
•	 Modify your for loop to print a sentence using the name of the pizza
instead of printing just the name of the pizza For each pizza you should
have one line of output containing a simple statement like I like pepperoni
pizza
•	 Add a line at the end of your program, outside the for loop, that states
how much you like pizza The output should consist of three or more lines
about the kinds of pizza you like and then an additional sentence, such as
I really love pizza!
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
