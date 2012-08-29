class Dog:
    
    def __init__(self, name):

        self.name = name
        self.live = True

    def __str__(self):

        if self.live:
            return "A dog named "+self.name
        return "A dead dog named "+self.name

    def bark(self):

        if self.live:
            print self.name+": Woof, woof!"
        else:
            print "Dead dogs can't bark."

    def die(self):

        if self.live:
            self.live = False
            print self.name+" died."
        else:
            print self.name+" is already dead."
