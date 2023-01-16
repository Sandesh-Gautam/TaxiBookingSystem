class Trips():
    def __init__(self, pick_up=None, drop_off=None,date=None,time=None):
        self.pick_up = pick_up
        self.drop_off = drop_off
        self.date = date
        self.time = time
    def getPick_up(self):
        return self.pick_up

    def getDrop_off(self):
        return self.drop_off

    def getDate(self):
        return self.date

    def getTime(self):
        return self.time
    def setPick_up(self, pick_up):
        self.pick_up = pick_up
    def setDrop_off(self, drop_off):
        self.drop_off = drop_off
    def setDate(self, date):
        self.date = date
    def setTime(self, time):
        self.time = time



class String4():
    def __str__(self):
        return str(self.pick_up + ", " + self.drop_off + "," + self.date + "," + self.time)