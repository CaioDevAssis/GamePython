import math

class AtributosBasicos:
    
    def __init__(self, nivel, forca, inteligencia, estamina, mana):
        
        self.nivel = nivel
        self.forca =forca
        self.inteligencia = inteligencia
        self.base_player = 50
        
        self.estaminaBase = self.base_player + int( math.sqrt(self.nivel) * self.nivel + math.sqrt(self.forca) * self.forca ) 
        if (estamina < self.estaminaBase):
            self.estamina = estamina
        else:
            self.estamina = self.base_player
        
        self.manaBase = self.base_player + int( math.sqrt(self.nivel) * self.nivel + math.sqrt(self.inteligencia) * self.inteligencia )
        if (mana < self.manaBase):
            self.mana = mana
        else:
            self.mana = self.base_player

