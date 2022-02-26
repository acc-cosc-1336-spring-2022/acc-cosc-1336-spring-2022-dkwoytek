import repetition

menu_selex = 'y'
while menu_selex == 'y':   #This is so that HW Menu is generated
    print('\nHomework 3 Menu\n1-Factorial\n2-Sum odd numbers\n3-Exit')
    selex = int(input('Please select menu item 1, 2 or 3: ')) 
    
    if selex == 1:   #This is the factorial part of the assignment
        keep_factoring = 'y'
        while keep_factoring == 'y':
            num = int(input('To calculate the factorial, please enter a whole number greater than 0 but less than 10: '))
            if num <= 0 or num >= 10:
                print('Number entered is outside of specified range. Please enter another number in the correct range.')
                num = int(input('To calculate the factorial, please enter a whole number greater than 0 but less than 10: '))

            else:
                factorial = repetition.get_factorial(num)
                print('The factorial for', num,'is', format(factorial, ','))
            keep_factoring = input('Do you want to calculate another factorial (Enter y for yes, n for no): ')

    elif selex == 2:   #This is the sum of odd numbers part of the assignment
        keep_summing = 'y'
        while keep_summing =='y':
            num2 = int(input('To get sum of odd numbers, please enter a whole number greater than zero but less than 100: '))
            if num2 <= 0 or num2 >= 100:
                print('Numbner entered is outside of specified range. Please enter another number in the correct range.')
                num2 = int(input('To get sum of odd numbers, please enter a whole number greater than zero but less than 100: '))
            
            else:
                total_odds = repetition.sum_odd_numbers(num2)
                print('The sum of all odd numbers up to', num2, 'is', format(total_odds, ','))
            keep_summing = input('Do you want to calculate the sum of odd numbers again (Enter y for yes, n for no): ')

    elif selex == 3:   #This is the exit from the menu part of the assignment
        print('You have chosen to exit.')
    
    else:
        print("Invalid entry")

    menu_selex = input('Do you want to continue with another menu selection (Enter y for yes, n to exit from Homework 3 Menu): ')
