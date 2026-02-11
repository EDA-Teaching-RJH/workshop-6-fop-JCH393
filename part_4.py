travel_log = []

while True:
    user_input = input('Sensor Reading (Slope Angle): ')

    try:
        angle = float(user_input)
        if angle > 45:
            print('CRITICAL TILT! HALTING.')
            break
        else:
            travel_log.append(angle)
            print('Path Stable')

    except ValueError:
        print('Sensor Glitch')

print('Mission Terminated')