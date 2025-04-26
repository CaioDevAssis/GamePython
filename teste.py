import os

import XpBase

os.system('cls')
print("iniciando teste ... ")


teste = XpBase.XpBase(0, 0, 0)

teste.Prints()

print("\nAlterando valor ...\n")

teste.setXpGanha(350)

teste.Prints()


print("\nAlterando valor ...\n")

teste.setXpGanha(350)

teste.Prints()

for x in range(10):
    teste.setXpGanha(157)
    teste.Prints()
    
