import cv2 as cv
#gets postition of fish as a tupple (x, y), returns empty if no fish found
class FishFinder:
    fishColors = None
    tankColors = None
    threshold = None
    def setFishColors(self, colors):
        self.fishColors = colors
    def setTankColors(self, colors):
        self.tankColors = colors
    def setThreshold(self, threshold):
        self.threshold = threshold
    #gets postition of fish as a tupple (x, y)
    def getFishPostion(self, img, hight, width, tankHight, tankWidth, tankCornerx, tankCornery):
        if tankCornerx >= width/2:
            tankCornerx = tankCornerx-tankWidth
        if tankCornery >= hight/2:
            tankCornery = tankCornery-tankHight
        xpos = float(0)
        ypos = float(0)
        count = float(0)
        for x in range(tankCornerx, tankCornerx+tankWidth):
            for y in range(tankCornery, tankCornery+tankHight):
                pix = img[y, x]
                minDistSQ = 195076
                for c in self.fishColors:
                    distSQ = (int(pix[0]) - int(c[0]))**2 + (int(pix[1]) - int(c[1]))**2 + (int(pix[2]) - int(c[2]))**2
                    if distSQ < minDistSQ:
                        minDistSQ = distSQ
                if minDistSQ > self.threshold:
                    continue
                isfish = True
                for c in self.tankColors:
                    if minDistSQ>((int(pix[0]) - int(c[0]))**2 + (int(pix[1]) - int(c[1]))**2 + (int(pix[2]) - int(c[2]))**2):
                        isfish = False
                        break
                if isfish:
                    xpos += x
                    ypos += y
                    count += 1
                else:
                    continue
        if count != 0:
            return (int(round(xpos/count)), int(round(ypos/count)))
        else:
            return ()
def test():
    fishFinder = FishFinder()
    imgPath = "C:\\dev\\applications\\FishTankSquared\\Test\\TestFakeFishImage.png"
    fishFinder.setFishColors([[39, 127, 255]])
    fishFinder.setTankColors([[255, 255, 255]])
    fishFinder.setThreshold(1500)   
    img = cv.imread(imgPath)
    assert img is not None
    print(fishFinder.getFishPostion(img, img.shape[0], img.shape[1], 525, 1100, 20, 50))
test()