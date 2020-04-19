class Room():

    enemies_defeated = 0

    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def set_name(self,room_name):
        self.name = room_name

    def set_description(self,room_description):
        self.description = room_description

    def set_character(self,character_name):
        self.character = character_name

    def set_item(self,item_description):
        self.item = item_description

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_character(self):
        return self.character

    def get_item(self):
        return self.item 

    def describe(self):
        print(self.description)

    def show_name(self):
        print(self.name)

    def link_room(self,room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        # print(self.name + ' linked rooms: ' + repr(self.linked_rooms))
        
    def get_details(self):
        print('The ' + self.name)
        print("------------------")
        print(self.description)
        if self.item is not None:
            roomitem = self.get_item()
            print("There is a " + roomitem.get_name() + " (" + roomitem.get_description() + ") in the room")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print('The ' + room.get_name() + ' is ' + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You cant go that way")
            return self
        

    # Getters and setters for the enemies_defeated variable
    def get_defeated(self):
        return Room.enemies_defeated
  
    def set_defeated(self, number_defeated):
        Room.enemies_defeated = number_defeated
    
    
    
