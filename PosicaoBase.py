

class PosicaoBase:
    
    def __init__(self pxBase, pyBase, px, py):
        
        self.pxBase = pxBase
        self.pyBase = pyBase
        self.px     = px
        self.py     = py
    
    def setPxBase(self, pxBase ):
        self.pxBase = pxBase
        
    def getPxBase(self):
        return self.pxBase
        
    def setPx(self, px):
        self.px = px
        
    def getPx(self):
        return self.px
        
    def setPyBase(self, pyBase):
        self.pyBase = pyBase
    
    def getPyBase(self):
        return self.pyBase
        
    def selPy(self, py):
        self.py = py
        
    def getPy(self):
        return self.py