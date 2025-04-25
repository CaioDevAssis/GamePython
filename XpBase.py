

class XpBase:
    def __init__(self, xpTotal):
        self.xpTotal = xpTotal
        
    
    def setXpTotal(self, valor):
        self.xpTotal = valor
        
    def getXpTotal(self):
        return self.xpTotal
        
    
    
    def Prints(self):
        print("xpTotal: ", self.getXpTotal())