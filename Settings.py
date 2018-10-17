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

    def resetScore(self):
        self.score = 0