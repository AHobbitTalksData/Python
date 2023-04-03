print('=============================================')
print('              FizzBuzz')
print('=============================================')


def answer_user(n):
    print(' ') 
    print('-  Entering a number   -') 
    num = int(input('Please enter an integer number from 1 to 100: '))

    while 0>num or num>100:
        try:
            num = int(input('Wrong input. Please enter an integer number from 1 to 100: '))
        except ValueError:
            print("Invalid input. Please enter an integer.")

    if num % 3 == 0 and num % 5 == 0:
        print("------FizzBuzz------")
    elif num % 3 == 0:
        print("------Fizz------")
    elif num % 5 == 0:
        print("------Buzz------")
    else:
        print(num)
    
def automatic(x):      
    print(' ') 
    print('-  Automatic   -') 

    # Automatic from 1 to 100 
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
            print(' ')
        elif num % 3 == 0:
            print("Fizz")
            print(' ')
        elif num % 5 == 0:
            print("Buzz")
            print(' ')
        else:
            print(num)
        
while True:
    print(' *** How would you like to continue? *** ')
    print('1) I want to enter a number')
    print('2) I want to see the results for all the numbers from 1 to 100')
    print('3) I want to stop the program')

    try:
        answer = int(input('Please enter a number from 1 to 3: '))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

    if answer == 1:
        answer_user(answer)
    elif answer == 2:
        automatic(answer)
    elif answer == 3:
        break
    else:
        print('Invalid input. Please enter a number from 1 to 3.')
        continue
