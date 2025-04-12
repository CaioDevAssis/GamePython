import math

class AtributosBasicos:
    
    def __init__(self, nivel, forca, inteligencia):
        self.nivel = nivel
        self.forca =forca
        self.inteligencia = inteligencia
        self.base_player = 50
        
        self.estaminaBase = self.base_player + int( math.sqrt(self.nivel) * self.nivel + math.sqrt(self.forca) * self.forca )      
        self.manaBase = self.base_player + int( math.sqrt(self.nivel) * self.nivel + math.sqrt(self.inteligencia) * self.inteligencia )
        
        
teste = AtributosBasicos(5,12,9)

print(teste.estaminaBase)
print(teste.manaBase)