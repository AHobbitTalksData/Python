# SORTING HAT: Hogwarts School of Witchcraft and Wizardry. 

print('=============================================')
print('             The Sorting Hat')
print('=============================================')

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

# ~~~~~~~~~~~~~~~ Question 1 ~~~~~~~~~~~~~~~

print('Q1) Do you like Dawn or Dusk?')
print('    1) Dawn')
print('    2) Dusk')

while True:  # loop infinitely until correct answer
    question = input('    Insert answer here: ')
    print(' ')

    if question == '1' or question == '2':  # check if the input is valid
        break  # exit the loop if the input is valid
    else:
        print('Invalid input. Please enter "1" or "2".')  # prompt the user to re-enter the input

# Assigning points to the houses according to the first answer. 
if question == 1:
    Gryffindor=1
    Ravenclaw = 1
else:
    Hufflepuff = 1
    Slytherin = 1

# ~~~~~~~~~~~~~~~ Question 2 ~~~~~~~~~~~~~~~

print('Q2) When I’m dead, I want people to remember me as:')
print('    1) The Good')
print('    2) The Great')
print('    3) The Wise')
print('    4) The Bold')

# loop infinitely until correct answer
while True:  
    question = input('    Insert answer here: ')
    print(' ')

    if question == '1' or question == '2' or question == '3' or question == '4':  # check if the input is valid
        break  # exit the loop if the input is valid
    else:
        print('Invalid input.')  # prompt the user to re-enter the input

# Assigning points to the houses according to the first answer. 
if question == 1:
    Hufflepuff = 2 + Hufflepuff
elif question == 2:
    Slytherin = 1 + Slytherin
elif question == 3:
    Ravenclaw = 1 + Ravenclaw
else:
    Gryffindor = 1 + Gryffindor    
    
# ~~~~~~~~~~~~~~~ Question 3 ~~~~~~~~~~~~~~~

print('Q3) Which kind of instrument most pleases your ear?')
print('    1) The violin')
print('    2) The trumpet')
print('    3) The piano')
print('    4) The drum')

# loop infinitely until correct answer
while True:  
    question = input('    Insert answer here: ')
    print(' ')

    if question == '1' or question == '2' or question == '3' or question == '4':  # check if the input is valid
        break  # exit the loop if the input is valid
    else:
        print('Invalid input.')  # prompt the user to re-enter the input

# Assigning points to the houses according to the first answer. 
if question == 1:
    Slytherin  = 4 + Slytherin
elif question == 2:
    Hufflepuff = 4 + Hufflepuff
elif question == 3:
    Ravenclaw = 4 + Ravenclaw
else:
    Gryffindor = 4 + Gryffindor         

# ~~~~~~~~~~~~~~~ Answer ~~~~~~~~~~~~~~~
    
houses = ['Slytherin', 'Hufflepuff', 'Ravenclaw', 'Gryffindor']
scores=[Slytherin, Hufflepuff, Ravenclaw, Gryffindor]
max_index = scores.index(max(scores))
max_house = houses[max_index]

print('The house you will be assigned to is:', max_house)
