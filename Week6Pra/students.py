class student():
    def __init__(self, name, id):
        self.id = id
        self.name = name

    def changeID(self, id):
        self.id = id

    def print(self):
        print("{} - {}".format(self.name, self.id))

jane = student("Jane", 10)
jane.print()
jane.changeID(11)
jane.print()