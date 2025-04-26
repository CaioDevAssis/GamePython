import XpBase
import PosicaoBase
import AtributosBasicos

class PersonagemBase:
    
    def __init__(self, atributos):
        self.atributos = atributos
        
        
    ##### atributos ##### 
    
    def setAtributosNivel(self):
        self.atributos.setNivel(1)
    def getAtributosNivel(self):
        return self.atributos.getNivel()
        
    def getAtributosEstaminaBase(self):
        return self.atributos.getEstaminaBase()
        
    def setAtributosEstamina(self, valor):
        self.atributos.setEstamina(valor)
    def getAtributosEstamina(self):
        return self.atributos.getEstamina()
        
    
    def getAtributosManaBase(self):
        return self.atributos.getManaBase()
    
    def setAtributosMana(self, valor):
        self.atributos.setMana(valor)
    def getAtributosMana(self):
        return self.atributos.getMana()

        
    def setAtributosForca(self, valor):
        self.atributos.setForca(valor)
    def getAtributosForca(self):
        return self.atributos.getForca()
        
    def setAtributosInteligencia(self, valor):
        self.atributos.setInteligencia(valor)   
    def getAtributosInteligencia(self):
        return self.atributos.getInteligencia()
        
    def Prints(self):
        
        print("Nivel: ",self.getAtributosNivel(),
        " | EstaminaBase: ",self.getAtributosEstaminaBase(), "/",self.getAtributosEstamina()," Estamina",
        " | ManaBase: ", self.getAtributosManaBase(),"/",self.getAtributosMana()," Mana",
        " | Forca: ", self.getAtributosForca()," | Inteligencia: ",self.getAtributosInteligencia()
                )