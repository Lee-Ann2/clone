value1 = input('Enter your first number:\n')
value2 = input('Enter your second number:\n')

v1 = int(value1)
v2 = int(value2)

choice = input('Enter option 1 for addition\nEnter option 2 for subration\nEnter option 3 for multiplication\nEnter 4 for division\n')
choice = int(choice)

if choice == 1:
    print(v1 + v2)
elif choice == 2:
    print(v2 - v1)
elif choice == 3:
    print(v1 * v2)
elif choice == 4:
    (v2 / v1)
else:
    print('Stop being full of shiet bro!')