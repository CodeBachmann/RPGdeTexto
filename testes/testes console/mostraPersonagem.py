
import os

class CriarPersonagem():
    def __init__(self, vida, vidaMax, ataque, defesa, classe, nome, critico,
    inteligencia, mana, habilidades, ouro, caminhado):
        self.vida = vida
        self.vidaMax = vidaMax
        self.ataque = ataque
        self.defesa = defesa
        self.classe = classe
        self.critico = critico
        self.inteligencia = inteligencia
        self.mana = mana
        self.habilidades = habilidades
        self.nome = nome
        self.ouro = ouro
        self.caminhado = caminhado

habilidades = []

habilidades.append("RAP DE ANIME(RA)")
habilidades.append("MASOQUISTA DA ACADEMIA (PASSIVA)")
Sabel = CriarPersonagem(vida=8,
                        vidaMax=8,
                        ataque=3,
                        defesa=1,
                        classe="SABEL",
                        critico=8,
                        nome='Greg',
                        inteligencia=2,
                        mana=6,
                        habilidades=habilidades,
                        ouro= 100,
                        caminhado=0)

RED   = "\033[1;31m"
BLUE  = "\033[1;34m"        
RESET = "\033[0;0m"

class p():
  p = ['__O__',
       '  |  ',
       ' / \\ ']
  a =[RESET+'     '+RESET,
      RED  +' (ºº)'+RESET,
      BLUE +' < > '+RESET,]

os.system('cls')
print(F"""

 {p.p[0]}     Vida: {'*'*Sabel.vida          + RED +'**'+RESET }
 {p.p[1]}      Def: {'*'*Sabel.defesa        + BLUE +'***'+RESET }
 {p.p[2]}      Int: {'*'*Sabel.inteligencia  + RED +''+RESET }
inventário: {p.a[1]} {p.a[2]} {p.a[0]}


""")