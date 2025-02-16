import math
class PosToSpeedInterface:
    #returns a tuple with size of 2 with 2 floats (R, L)
    def getCurrentSpeed(self, x:int, y:int) -> tuple:
        pass
    #width is width of image and hight is hight of image
    def setSettings(self, maxSpeed:float, maxTurnRate:float, width:int, height:int, *args:int):
        pass
# I'll come up with a better name later
class RectangleBoxCircleDeadZonePosToSpeed(PosToSpeedInterface):
    maxSpeed = 0
    maxTurnRate = 0
    size = [0,0]
    tankCorner = [0,0]
    tankSize = [0,0]
    deadZoneRaidius = 0
    deadZoneCenter = [0, 0]
    def getCurrentSpeed(self, x:int, y:int) -> tuple:
        if ((x-self.deadZoneCenter[0])**2 + (y-self.deadZoneCenter[1])**2 < self.deadZoneRaidius**2):
            return (0, 0)

        shiftx = self.deadZoneCenter[0] - x
        shifty = self.deadZoneCenter[1] - y
        theta = math.atan2(shifty, shiftx)
        deadZoneEdge =  [self.deadZoneCenter[0] + math.cos(theta)*self.deadZoneRaidius, self.deadZoneCenter[0] + math.sin(theta)*self.deadZoneRaidius]
        tankEdge = [0, 0]
        px = shiftx/(self.tankSize[0]/2)
        py = shifty/(self.tankSize[1]/2)
        if(math.fabs(px)>math.fabs(py)):
          if (px < 0):
              tankEdge[0] = self.tankCorner[0] if self.tankCorner[0] >= self.tankSize[0] else self.tankCorner[0] + self.tankSize[0]
              tankEdge[1] = self.deadZoneCenter[1] - (shifty/shiftx)*(self.deadZoneCenter[0] - tankEdge[0])
          else:
              tankEdge[0] = self.tankCorner[0] if self.tankCorner[0] <= self.tankSize[0] else self.tankCorner[0] + self.tankSize[0]
              tankEdge[1] = self.deadZoneCenter[1] - (shifty/shiftx)*(self.deadZoneCenter[0] - tankEdge[0])
        else:
            if (py < 0):
                tankEdge[1] = self.tankCorner[1] if self.tankCorner[1] >= self.tankSize[1] else self.tankCorner[1] + self.tankSize[1]
                tankEdge[0] = self.deadZoneCenter[0] - (shiftx/shifty)*(self.deadZoneCenter[1] - tankEdge[1])
            else:
                tankEdge[1] = self.tankCorner[1] if self.tankCorner[1] <= self.tankSize[1] else self.tankCorner[1] + self.tankSize[1]
                tankEdge[0] = self.deadZoneCenter[0] - (shiftx/shifty)*(self.deadZoneCenter[1] - tankEdge[1])
        # get max vector magatude
        mag = math.fabs(math.sin(theta)-math.cos(theta) if math.fabs((math.sin(theta)-math.cos(theta))) > math.fabs((math.sin(theta)+math.cos(theta))) else (math.sin(theta)+math.cos(theta)))
        # get percent of maximum power
        per = (math.sqrt((x-deadZoneEdge[0])**2 + (y-deadZoneEdge[1])**2))/(math.sqrt((tankEdge[0]-deadZoneEdge[0])**2 + (tankEdge[1]-deadZoneEdge[1])**2))
        return ((math.sin(theta)*self.maxSpeed-math.cos(theta)*self.maxTurnRate)*per/mag,(math.sin(theta)*self.maxSpeed+math.cos(theta)*self.maxTurnRate)*per/mag)
    #args[0] = tankCornerX
    #args[1] = tankCornerY
    #args[2] = tankWidth
    #args[3] = tankHeight
    #args[4] = deadZoneRaidius
    def setSettings(self, maxSpeed:float, maxTurnRate:float, width:int, height:int, *args:int):
        self.maxSpeed = maxSpeed
        self.maxTurnRate = maxTurnRate
        self.size[0] = width
        self.size[1] = height
        self.tankCorner[0] = args[0]
        self.tankCorner[1] = args[1]
        self.tankSize[0] = args[2]
        self.tankSize[1] = args[3]
        self.deadZoneRaidius = args[4]
        self.deadZoneCenter[0] = self.tankCorner[0] - (self.tankSize[0]/2) if self.tankCorner[0]>(self.size[0]/2) else self.tankCorner[0] + (self.tankSize[0]/2)
        self.deadZoneCenter[1] = self.tankCorner[1] - (self.tankSize[1]/2) if self.tankCorner[1]>(self.size[1]/2) else self.tankCorner[1] + (self.tankSize[1]/2)
        pass
def test():
    controler = RectangleBoxCircleDeadZonePosToSpeed()
    controler.setSettings(1, 1, 500, 500, 50, 50, 400, 400, 100)
    print(controler.getCurrentSpeed(250, 250))
    print(controler.getCurrentSpeed(60, 250))
    print(controler.getCurrentSpeed(440, 250))
    print(controler.getCurrentSpeed(250, 60))
    print(controler.getCurrentSpeed(250, 440))
    print(controler.getCurrentSpeed(440, 440))
