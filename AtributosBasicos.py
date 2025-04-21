import math

class AtributosBasicos:
    
    def __init__(self, nivel, forca, inteligencia, estamina, mana):
        
        self.nivel = nivel
        self.forca =forca
        self.inteligencia = inteligencia
        self.base_player = 50
        
        self.setEstaminaBase()
        if (estamina < self.estaminaBase):
            self.estamina = estamina
        else:
            self.estamina = self.base_player
        
        self.setManaBase()
        if (mana < self.manaBase):
            self.mana = mana
        else:
            self.mana = self.base_player
            
            
    def setAtributos(self, valor):
        return self.base_player + int( math.sqrt(self.nivel) * self.nivel + math.sqrt(valor) * valor )
        
    def setEstaminaBase(self):
        self.estaminaBase = self.setAtributos(self.forca)
        
    def setManaBase(self):
        self.manaBase = self.setAtributos(self.inteligencia)
        


teste = AtributosBasicos(1,12,10,30,30)

print(teste.estaminaBase)
print(teste.manaBase)