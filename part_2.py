rover_status = {'Battery': 100, 'Heater': 'Off'}
print(rover_status['Battery'])
rover_status['Battery'] = 85
rover_status['Heater'] = 'On'
rover_status['Speed'] = 5
print(rover_status)
