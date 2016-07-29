class Classy(object):

    def __init__(self):
        self.items = [];

    def getClassiness(self):
        points = 0
        for item in self.items:
            if item == "tophat":
                points += 2
            elif item == "bowtie":
                points += 4
            elif item == "monocle":
                points += 5

        return points

    def addItems(self, item):
        self.items.append(item)

me = Classy()

me.addItems("tophat")
me.addItems("bowtie")
me.addItems("monocle")

print me.getClassiness()