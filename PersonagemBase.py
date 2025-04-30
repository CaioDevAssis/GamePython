import XpBase
import PosicaoBase
import AtributosBasicos

class PersonagemBase:
    
    def __init__(self, atributos, xp, posicao):
        self.atributos = atributos
        self.xp = xp
        self.posicao = posicao
        
        
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
        
    def setAtributosAgilidade(self, valor):
        self.atributos.setAgilidade(valor)
    def getAtributosAgilidade(self):
        return self.atributos.getAgilidade()
        
    ## XpBase
           

    def setXpTotal(self, valor):
        self.xp.setXpTotal(valor)
    def getXpTotal(self):
        return self.xp.getXpTotal()
        
    def getXpProximoNivel(self):
        return self.xp.getXpProximoNivel() 

    def setXpGanha(self, xpGanha):
        resultado = self.xp.setXpGanha(xpGanha)
        if resultado == 1:
            self.atributos.setNivel(1)
    
    def getXpGanha(self):
        return self.xp.getXpGanha()
        
    ## posicaoBase ##
    
    def setPosicaoPx(self, valor):
        self.posicao.setPx(valor)
    def getPosicaoPx(self):
        return self.posicao.getPx()
        
    def setPosicaoPy(self, valor):
        self.posicao.setPy(valor)
    def getPosicaoPy(self):
        return self.posicao.getPy()
    
    def setPosicaoPxBase(self, valor):
        self.posicao.setPxBase(valor)
    def getPosicaoPxBase(self):
        return self.posicao.getPxBase()
        
    def setPosicaoPyBase(self, valor):
        self.posicao.setPyBase(valor)
    def getPosicaoPyBase(self):
        return self.posicao.getPyBase()
        
    def Prints(self):
        
        print("Nivel: ",self.getAtributosNivel(),
        " | EstaminaBase: ",self.getAtributosEstaminaBase(), "/",self.getAtributosEstamina()," Estamina",
        " | ManaBase: ", self.getAtributosManaBase(),"/",self.getAtributosMana()," Mana",
        " | Forca: ", self.getAtributosForca()," | Inteligencia: ",self.getAtributosInteligencia(),
        " | Agilidade: ", self.getAtributosAgilidade()
                )
        print(
            "XpTotal: ",self.getXpTotal(), " | Proximo nivel: ",self.getXpProximoNivel(),"/",self.getXpGanha()," Xpganha",
            
        )
        print(
        "PosicaoPx: ",self.getPosicaoPx()," | PosicaoPy: ", self.getPosicaoPy(),
        " | PxBase: ",self.getPosicaoPxBase(), " | PyBase: ",self.getPosicaoPyBase()
        
        )