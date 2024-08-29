class luz (object):
    def __init__(self, intensidad,x,y,alcanze):
        self.intensidad = intensidad
        self.x = x
        self.y = y
        self.alcanze = alcanze

    def getAlcanze(self):
        return self.alcanze
    
    def setAlcanze(self,alcanze):
        self.alcanze = alcanze

    def getPosicion(self):
        return self.x,self.y
    
    def setPosicion(self,x,y):
        self.x = x
        self.y = y

    def getIntensidad(self):
        return self.intensidad

    def setIntensidad(self, intensidad):
        self.intensidad = intensidad
