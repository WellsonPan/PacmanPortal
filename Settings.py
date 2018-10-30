class Settings():
    def __init__(self):
        self.screenWidth = 738
        self.screenHeight = 868
        self.backgroundColor = (0, 0, 0)
        self.gameActive = False
        self.highScores = False

        # Pacman
        self.pacmanColor = (255, 255, 0)
        self.pacmanRad = 36
        self.pacmanSpeed = 2.1

        # points
        self.pointVal = 10
        self.score = 0
        self.high_score = 0
        self.livesLeft = 3

        # Ghosts
        self.blinkyColor = (255, 0, 0)
        self.pinkyColor = (255, 192, 203)
        self.inkyColor = (137, 207, 240)
        self.clydeColor = (255, 165, 0)
        self.ghostSize = 34
        self.ghostSpeed = 2

        # Portal
        self.portalSpeed = 10

    def reset(self):
        self.score = 0
        self.gameActive = False
        self.livesLeft = 3