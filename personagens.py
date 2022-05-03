from asyncio.format_helpers import _format_callback_source


class Personagem():
    def __init__(self, vida, vidaMax, ataque, defesa, classe, nome, critico,/
                 inteligencia, mana, xp, nivel, habilidades, ouro, caminhado):
        self.vida = vida
        self.vidaMax = vidaMax
        self.ataque = ataque
        self.defesa = defesa
        self.classe = classe
        self.critico = critico
        self.inteligencia = inteligencia
        self.mana = mana
        self.xp = xp
        self.nivel = nivel
        self.habilidades = habilidades
        self.nome = nome
        self.ouro = ouro
        self.caminhado = caminhado

class npc():
    def __init__(self, vida, vidaMax, ataque, defesa, classe, critico, nivel, ouro):
        self.vida = vida
        self.vidaMax = vidaMax
        self.ataque = ataque
        self.defesa = defesa
        self.classe = classe
        self.critico = critico
        self.nivel = nivel
        self.ouro = ouro