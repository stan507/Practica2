class robot (object):
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    #funcion para presentarse
    def introduce_self(self):
        print("My name is " + self.name)