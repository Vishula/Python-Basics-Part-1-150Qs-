# text adventure game

# play = input("Do you want to play (Yes) or (No)").lower().strip()
# if play == 'yes':
#     print("Entering Game Now...")
#     rooms = []
#     play = input("You are in Astro Road, Where do you want to go (Left) or (Right)")
#
#
# else:
#     print("END GAME")

"""
object_adventure.py

A text adventure with objects you can pick up and put down.
"""

# data setup
rooms = {'empty': {'name': 'an empty room', 'east': 'bedroom', 'north': 'temple', 'contents': [],
                   'text': 'The stone floors and walls are cold and damp.'},
         'temple': {'name': 'a small temple', 'east': 'torture', 'south': 'empty',
                    'text': 'This seems to be a place of worship and deep contemplation.',
                    'contents': ['bench', 'bench', 'bench', 'statue']},
         'torture': {'name': 'a torture chamber', 'west': 'temple', 'south': 'bedroom',
                     'contents': ['chains', 'thumbscrews'],
                     'text': 'There is a rack and an iron maiden against the wall\naand some dark stains on the floor.'},
         'bedroom': {'name': 'a bedroom', 'north': 'torture', 'west': 'empty', 'contents': ['sheets', 'bed'],
                     'text': 'This is clearly a bedroom, but no one has slept\nhere in a long time.'}}
directions = ['north', 'south', 'east', 'west']
current_room = rooms['empty']
carrying = []

# game loop
while True:
    # display current location
    print("Directions - 'north', 'south', 'east', 'west'")
    print('You are in {}.'.format(current_room['name']))
    print(current_room['text'])
    # display movable objects
    if current_room['contents']:
        print('In the room are: {}'.format(', '.join(current_room['contents'])))
    # get user input
    command = input('\nWhat do you do? ').strip()
    # movement
    if command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
        else:
            # bad movement
            print("You can't go that way.")
    # quit game
    elif command.lower() in ('q', 'quit'):
        break
    # gather objects
    elif command.lower().split()[0] == 'get':
        item = command.lower().split()[1]
        if item in current_room['contents']:
            current_room['contents'].remove(item)
            carrying.append(item)
        else:
            print("I don't see that here.")
    # get rid of objects
    elif command.lower().split()[0] == 'drop':
        item = command.lower().split()[1]
        if item in carrying:
            current_room['contents'].append(item)
            carrying.remove(item)
        else:
            print("You aren't carrying that.")
    # bad command
    else:
        print("I don't understand that command.")

