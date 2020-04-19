class Item():

    def __init__(self,item_name):
        self.name = item_name
        self.description = None
        self.location = None

    def get_name(self):
        return self.name

    def set_name(self, item_name):
        self.name = item_name

    def set_description(self,item_description):
        self.description = item_description

    def set_location(self,item_room):
         self.location = item_room

    def get_description(self):
        return self.description

    def describe(self):
         print(self.name + " - " + self.description)
         #print("Found in the " + self.location)
     
        
