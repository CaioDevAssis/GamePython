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
            
            
    def setAtributos(self, valor): #esse metodo é usado apenas em setEstaminaBase e setManaBase... valor é o estado da classe, nem se preoculpe
        return self.base_player + int( math.sqrt(self.nivel) * self.nivel + math.sqrt(valor) * valor )
        
    def setEstaminaBase(self):
        self.estaminaBase = self.setAtributos(self.forca)
        
    def setEstamina(self, estamina): 
        if (estamina >= 0):
            if ( (self.estamina + estamina) < self.estaminaBase):
                self.estamina += estamina
            else:
                self.estamina = self.estaminaBase
        else:
            if ( (self.estamina + estamina) >= 0):
                 self.estamina += estamina
            else:
                self.estamina = 0
        
        
    def setManaBase(self):
        self.manaBase = self.setAtributos(self.inteligencia)
        
    def setMana(self, mana): 
        if (mana >= 0):
            if ( (self.mana + mana) < self.manaBase):
                self.mana += mana
            else:
                self.mana = self.manaBase
        else:
            if ( (self.mana + mana) >= 0):
                 self.mana += mana
            else:
                self.mana = 0
                
    def setNivel(self, nivel):
        self.nivel = nivel
        self.setEstaminaBase()
        self.setManaBase()
        self.estamina = self.estaminaBase
        self.mana = self.manaBase
    
    def getNivel(self):
        return self.nivel
        
    def setForca(self, valor):
        self.forca += valor
    
    def getForca(self):
        return self.forca
        
    def setInteligencia(self, valor):
        self.inteligencia += valor
        
    def getInteligencia(self):
        return self.inteligencia
        
        
    def Prints(self):
        print("\nNivel: ",self.nivel," Forca: ", self.forca, " Inteligencia: ", self.inteligencia)
        print("Estamina: ",self.estamina,"/",self.estaminaBase," -- Mana: ", self.mana,"/",self.manaBase)
        
