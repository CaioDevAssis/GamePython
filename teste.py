import os

import PosicaoBase

os.system('cls')
print("iniciando teste ... ")


teste = PosicaoBase.PosicaoBase(0, 0, 1, 1)

teste.Prints()

print("\nAlterando valores ... \n")

teste.setPxBase(5)
teste.setPx(-8)
teste.setPyBase(-9)
teste.setPy(23)

teste.Prints()

