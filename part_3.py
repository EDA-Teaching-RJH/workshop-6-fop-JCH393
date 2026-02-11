user_input = input('Enter Motor Speed: ')
try:
    motor_speed = int(user_input)
    print(f'Speed set to {motor_speed}')
except ValueError:
    print('Error: Corrupted Signal')
