sum = 0
for i in range (5):
    while True:
        try:
            user_input = int(input(f'Enter int #{i+1}: '))
            sum += user_input
            break
        except ValueError:
            print('Invalid input. Please enter an int.')

print(f'Your sum is {sum}')