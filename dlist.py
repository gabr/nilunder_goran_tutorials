class Dlist(list):

    def __init__(self):
        super(Dlist, self)

    def append(self, x):
        super(Dlist, self).append(x+x)
