import os


import PosicaoBase
import XpBase
import AtributosBasicos

import PersonagemBase

posicao = PosicaoBase.PosicaoBase(0, 0, 0, 0) #  -- pxBase, pyBase, px, py
pontos = XpBase.XpBase(0, 0, 0) # -- xpTotal, nivel, xpGanha
atributos = AtributosBasicos.AtributosBasicos(0, 0, 0, 45, 34) # --  nivel, forca, inteligencia, estamina, mana


os.system('cls')
print("iniciando teste ... ")

personagem = PersonagemBase.PersonagemBase(atributos)
personagem.setAtributosForca(5)
personagem.setAtributosInteligencia(5)


personagem.Prints()

for x in range(15):
    personagem.setAtributosForca(x)
    personagem.setAtributosInteligencia(x)
    personagem.setAtributosNivel();
    personagem.Prints()
