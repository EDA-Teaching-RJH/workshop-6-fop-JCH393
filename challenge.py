rover_state = {
    'x':0,
    'y':0,
    'samples':0
}
cmds = input('Are there more commands in command_batch? ').strip().capitalize()

if cmds == 'Yes':
    next_command = input('Move or Dig? ').upper()
    if next_command == 'MOVE':
        try:
            x = input('Distance? ')
            y = int(x)
            rover_state['y'] += y
        except ValueError:
            print('Bad distance')
    elif next_command == 'DIG':
        rover_state['samples'] += 1
    else:
        print('Unkown command')
else:
    print(rover_state)


