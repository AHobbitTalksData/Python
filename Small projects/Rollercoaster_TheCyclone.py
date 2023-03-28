print('=============================================')
print('             Rollercoaster The Cyclone')
print('=============================================')


height = int(input("-Enter height in centimeters: "))  # prompt the user to enter a value
print(' ')

credits = int(input("-Enter the number of credits you have available: "))  # prompt the user to enter a value
print(' ')

print('-Are you with a taller person?')
print('Please answer with yes or no.')
acomp=input('Insert answer here:')

while acomp.lower() != 'yes' and acomp.lower() != 'no':  # loop while the answer is neither "yes" nor "no" (case-insensitive)
    acomp = input('Invalid input. Please enter "yes" or "no": ')

print(' ')

if height>=137 and credits>=10:
    print('--Enjoy the ride!--')
elif height>=137 and credits<10:
    print('--Not enough credits.--')    
elif height<137 and credits>=10 and height<137 or height<100 and acomp=='yes':
    print('--Enjoy the ride!--')
elif height<137 and credits>=10 and height<137 or height<100 and acomp=='no':
    print('--You are not tall enough for this ride yet.--')
