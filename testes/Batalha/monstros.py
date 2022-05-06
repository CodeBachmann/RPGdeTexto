
class monstro:
  def __init__(self, nome, vida, dano, aparencia):
    self.nome = nome
    self.vida = vida
    self.dano = dano
    self.aparencia = aparencia


aparencia = ['          ',
         '//(o,,o)\\\\',
         '          ']
aranha = monstro(nome='aranha',vida=20,dano=3, aparencia=aparencia)

aparencia = [' o ',
         '/|\\', 
         '/ \\']
esqueleto = monstro(nome='esqueleto',vida=20,dano=3, aparencia=aparencia)

aparencia = [' o ',
         '/O\\', 
         '/ \\']
barrigudo = monstro(nome='barrigudo',vida=20,dano=3, aparencia=aparencia)





    