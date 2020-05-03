""" Creates and sim lite particles. """



class SimpleParticle:
    def __init__(self):
        self.id = []
        self.lifeTime = []
        self.state = []
        self.color = []
        self.bg = []

    def add(self, lifeTime=100, color=(255,255,255)):
        if lifeTime <= 0:
            lifeTime = 1
            break

        self.id.append(len(self.id))
        self.lifeTime.append(lifeTime)
        self.state.append(0)
        self.color.append(color)
        self.bg.append()

    def delete(self, id):
        if type(id) == type(0):
            del self.id[id]
            del self.lifeTime[id]
        if type(id) == type([]):
            for i in id:
                del self.id[i]
                del self.lifeTime[i]

    def live(self, pygameWindow):
        """ function that calculates all particle's info """
        for i in range(len(self.id)):








    pass
