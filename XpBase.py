

class XpBase:
    def __init__(self, xpTotal, nivel, xpGanha):
        self.xpTotal = xpTotal
        self.nivel = nivel
        self.xpBase = 350
        self.setXpProximoNivel() #aqui configura self.xpProximoNivel
        self.xpGanha = xpGanha
        
    
    def setXpTotal(self, valor):
        self.xpTotal += valor
        
    def getXpTotal(self):
        return self.xpTotal
        
    def getNivel(self):
        return self.nivel
        
    def setXpProximoNivel(self):
        self.xpProximoNivel = int(self.nivel * 0.1 * self.xpBase + self.xpBase)
    
    def getXpProximoNivel(self):
        return self.xpProximoNivel
        
    def setXpGanha(self, xp):
        self.xpTotal += xp
        if( (self.xpGanha+xp) < self.xpProximoNivel ):
            self.xpGanha += xp
            return 0
        else:
            self.nivel += 1
            self.xpGanha = (self.xpGanha+xp) - self.xpProximoNivel
            self.setXpProximoNivel()
            return 1
    
    def getXpGanha(self):
        return self.xpGanha
        
    
    
    def Prints(self):
        print("\nAlterando valor ...\n")
        print("xpTotal: ", self.getXpTotal(), " | Nivel: ", self.getNivel(), " | xpProximoNivel", self.getXpProximoNivel(),"/",self.getXpGanha() )
