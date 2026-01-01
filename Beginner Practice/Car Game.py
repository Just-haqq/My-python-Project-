command = ""
while True:
    command = input('> ').lower()
    if command == 'Start':
        print("Car has started")
    elif command == 'Stop':
        print("Car has stopped")
    elif command == 'help':
        print(""""
    Start - to start the car
    Stop - to stop the car
    quit - to exit   
    """)
    elif command == 'quit':
        print('Goodbye!')
        break
    else:
        print("System doesn't understand command")