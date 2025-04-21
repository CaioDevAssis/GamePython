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
        
    def setEstamina(self, estamina):        
        if ( (self.estamina + estamina) < self.estaminaBase):
            
            if ( (self.estamina + estamina)> 0 ):            
                self.estamina += estamina
            else:
                self.estamina = 0
        else:
            self.estamina = self.estaminaBase
        
        
    def setManaBase(self):
        self.manaBase = self.setAtributos(self.inteligencia)
        
    def setMana(self, mana):        
        if ( (self.mana + mana) < self.manaBase):
            
            if ( (self.mana + mana)> 0 ):            
                self.mana += mana
            else:
                self.mana = 0
        else:
            self.mana = self.mana
        
        
    def Prints(self):
        print("\nNivel: ",self.nivel," Forca: ", self.forca, " Inteligencia: ", self.inteligencia)
        print("Estamina: ",self.estamina,"/",self.estaminaBase," -- Mana: ", self.mana,"/",self.manaBase)
        


teste = AtributosBasicos(1,1,1,50,50)

teste.Prints()

teste.setEstamina(23)
teste.setMana(-15)

teste.Prints()