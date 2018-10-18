class Settings():
    def __init__(self):
        self.screenWidth = 738
        self.screenHeight = 818

        # Pacman
        self.pacmanColor = (255, 255, 0)
        self.pacmanRad = 36
        self.pacmanSpeed = 2

        # points
        self.pointVal = 10
        self.score = 0

        # Ghosts
        self.blinkyColor = (255, 0, 0)
        self.pinkyColor = (255, 192, 203)
        self.inkyColor = (137, 207, 240)
        self.clydeColor = (255, 165, 0)
        self.ghostSize = 34
        self.ghostSpeed = 1

        # Portal
        self.portalSpeed = 8

    def resetScore(self):
        self.score = 0