
class poder:
  def __init__(self, nome, dano, aparencia):
    self.nome = nome
    self.dano = dano
    self.aparencia = aparencia


aparencia = ['          ',
             '//(o,,o)\\\\',
             '          ']
ataque = poder(nome='ataque',dano=3, aparencia=aparencia)
