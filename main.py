from room import Room
from item import Item
from character import Character
from character import Enemy
from character import Friend

# Create rooms
hall = Room("Hall")
hall.set_description("The main entrance with sweeping stairs and seveal doors")

escape = Room("Escape")
escape.set_description("Well done you have won, all the enemies have been defeated and are free to leave")

dining_room = Room("Dining Room")
dining_room.set_description("A large room with a chandelier over the old dining table")

kitchen = Room("Kitchen")
kitchen.set_description("A working room full of the smell of cooking")

garden_room = Room("Garden Room")
garden_room.set_description("A light relaxing room overlooking the garden")

garden = Room("Garden")
garden.set_description("A neat courtyard space")

lounge = Room("Lounge")
lounge.set_description("A family room with many comfy chairs")

library = Room("Library")
library.set_description("A place of study with many books in large bookcases")

garage = Room("Garage")
garage.set_description("A space for the cars")

cellar = Room("Cellar")
cellar.set_description("A dark room full of wine")

garage_flat = Room("Garage Flat")
garage_flat.set_description("A self contained living space")

outhouse = Room("Outhouse")
outhouse.set_description("A place to store all the tools")

landing = Room("Landing")
landing.set_description("A joining space")

master_bedroom = Room("Master Bedroom")
master_bedroom.set_description("A room for the master to sleep in")

bathroom = Room("Bathroom")
bathroom.set_description("The ensuite for the master")

guest_bedroom = Room("Guest Bedroom")
guest_bedroom.set_description("A bedroom for the guests")

spare_bedroom = Room("Spare Bedroom")
spare_bedroom.set_description("A bedroom just in case")

attic = Room("Attic")
attic.set_description("A big open space")

box_room = Room("Box Room")
box_room.set_description("A room full of trunks")

junk_room = Room("Junk Room")
junk_room.set_description("A storeroom for every thing else")

# Link rooms
hall.link_room(dining_room, 'west')
hall.link_room(lounge, 'east')
hall.link_room(garden, 'north')
hall.link_room(escape, 'south')
hall.link_room(landing, 'up')


dining_room.link_room(hall, 'east')
dining_room.link_room(kitchen, 'north')

kitchen.link_room(dining_room, 'south')
kitchen.link_room(garden_room, 'north')

garden_room.link_room(kitchen, 'south')
garden_room.link_room(garden, 'east')

garden.link_room(garden_room, 'west')
garden.link_room(hall, 'south')
garden.link_room(outhouse, 'east')

lounge.link_room(hall, 'west')
lounge.link_room(library, 'east')

library.link_room(lounge, 'west')
library.link_room(garage, 'east')

garage.link_room(library, 'west')
garage.link_room(garage_flat, 'east')
garage.link_room(outhouse, 'north')
garage.link_room(cellar, 'down')

cellar.link_room(garage, 'up')

garage_flat.link_room(garage, 'west')

outhouse.link_room(garage, 'south')
outhouse.link_room(garden, 'west')

landing.link_room(hall, 'down')
landing.link_room(attic, 'up')
landing.link_room(guest_bedroom, 'west')
landing.link_room(master_bedroom, 'east')
landing.link_room(spare_bedroom, 'south')

master_bedroom.link_room(landing, 'west')
master_bedroom.link_room(bathroom, 'north')

bathroom.link_room(master_bedroom, 'south')

guest_bedroom.link_room(landing, 'east')

spare_bedroom.link_room(landing, 'north')

attic.link_room(landing, 'down')
attic.link_room(box_room, 'west')
attic.link_room(junk_room, 'east')

box_room.link_room(attic, 'east')

junk_room.link_room(attic, 'west')

# Create items
dagger = Item("dagger")
dagger.set_description("A nasty pointed object")

gun = Item("gun")
gun.set_description("A dangerous weapon keep clear")

cheese = Item("cheese")
cheese.set_description("A block of yellow mouldy cheese")

key = Item("key")
key.set_description("Your way to freedom")

# Assign items to rooms
kitchen.set_item(cheese)
dining_room.set_item(gun)


# Create characters
dave = Enemy("Dave","A smelly zombie")
dave.set_conversation("I am here to eat your brains")
dave.set_weakness("cheese")

catrina = Friend("Catrina", "A friendly skeleton")
catrina.set_conversation("I am here to guide you")

# Assign characters to rooms
dining_room.set_character(dave)


# Function to reassign an item to a room during game
def change_item(item):
    if item == 'gun':
        current_room.set_item(gun)
    elif item == 'cheese':
        current_room.set_item(cheese)
    elif item == 'dagger':
        current_room.set_item(dagger)
    elif item == 'key':
        current_room.set_item(key)

# Initialise
backpack = ['key', 'gun', 'dagger']
max_items_in_backpack = 3
dead = False
current_room = hall
number_of_enemies = 1
number_of_lives = 3

# Run game
while not dead:

    print("\n")         
    current_room.get_details()
    inhabitant = current_room.get_character()
    item = current_room.get_item()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")    
    if command in ["north","south","east","west","up","down"]:
        if current_room.get_name() == "Hall" and command == "south":
            if not ('key' in backpack):
                print("You don't have the key in your packback")
            elif not current_room.get_defeated() == number_of_enemies:
                print("There are still some enemies to defeated")                    
            else:
                print("you can escape")
                current_room = current_room.move(command)
        else:
            current_room = current_room.move(command)
    elif command == "talk":
        inhabitant.talk()
    elif command == "backpack":
        if len(backpack) == 0:
            print("Your backpack is empty")
        else:
            print(backpack)
    elif command == "hug":
        if inhabitant == None:
            print("There is no one here to hug :(")
        else:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                inhabitant.hug()
    elif command == "take":
        item = current_room.get_item()
        if  item == None:
            print("Nothing to take from this room")
        else:
            if isinstance(inhabitant, Enemy):
                print("Sorry, the enemy is guarding it, you'll have to fight him for it")
            else:
                if len(backpack) == max_items_in_backpack:
                    print("Sorry, you can only get three items in your packback")
                else:
                    backpack.append(item.get_name())
                    print(item.get_name() + " has been added to your backpack")
                    current_room.set_item(None)
    elif command =="leave":
        #item = current_room.get_item()
        if item is not None:
            print("There is already a " + item.get_name() + " in the room. You will have to swap it")            
        else:
            print("What do you want to leave")
            print(backpack)
            leave_it  = input()
            if not (leave_it in backpack):
                print("You don't have " + leave_it + " in your packback")
            else:
                print("OK leaving " + leave_it)
                backpack.remove(leave_it)
                change_item(leave_it)
    elif command == "swap":
        #item = current_room.get_item()
        print("What do you want to swap")
        print(backpack)
        swap  = input()
        if not (swap in backpack):
            print("You don't have " + swap + " in your packback")
        else:
            print("OK swapping " + swap + " with " + item.get_name())
            backpack.remove(swap)
            backpack.append(item.get_name())
            change_item(swap)            
    elif command == "fight":
        print("What will you fight with?")
        fight_with = input()
        print("You want to fight with " + fight_with)
        if not (fight_with in backpack):
            print("You don't have " + fight_with + " in your packback")
            fight_with = None
        if inhabitant.fight(fight_with) == True:
            dead = False
            current_room.set_character(None)
            backpack.remove(fight_with)
            current_room.set_defeated(current_room.get_defeated() + 1)
        else:
            number_of_lives = number_of_lives - 1
            if number_of_lives ==0:
                dead = True
            else:
                print("A lucky escape, but you still have " + str(number_of_lives) + " lives left")
            
    else:
        print("Sorry, I don't under the word " + command)
        
if dead:
    print("Game over")
            
            

        
        

        

    
