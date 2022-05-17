from asyncio.format_helpers import _format_callback_source

class CriarPersonagem():
    def __init__(self, vida, vidaMax, ataque, defesa, classe, nome, critico,
    inteligencia, mana, manaMax, regenMana, habilidades, ouro, caminhado, danoMitigado, artefatos, danoAumentado):
        self.vida = vida
        self.vidaMax = vidaMax
        self.ataque = ataque
        self.defesa = defesa
        self.classe = classe
        self.critico = critico
        self.inteligencia = inteligencia
        self.mana = mana
        self.manaMax = manaMax
        self.regenMana = regenMana
        self.habilidades = habilidades
        self.nome = nome
        self.ouro = ouro
        self.caminhado = caminhado
        self.danoMitigado = danoMitigado
        self.artefatos = artefatos
        self.danoAumentado = danoAumentado
class npc():
    def __init__(self, vida, vidaMax, ataque, defesa, nome, critico, ouro, danoMitigado):
        self.vida = vida
        self.vidaMax = vidaMax
        self.ataque = ataque
        self.defesa = defesa
        self.nome = nome
        self.critico = critico
        self.ouro = ouro
        self.danoMitigado= danoMitigado

#-------------------------------------------- Personagens ---------------------------------------------------------
habilidades = []
artefatos = []
Sabel = CriarPersonagem(vida=8,
                        vidaMax=8,
                        ataque=3,
                        defesa=1,
                        classe="SABEL",
                        critico=8,
                        nome='Greg',
                        inteligencia=2,
                        mana=6,
                        manaMax=6,
                        regenMana=1,
                        habilidades=habilidades,
                        artefatos=artefatos,
                        ouro= 100,
                        caminhado=0,
                        danoMitigado=0,
                        danoAumentado=0)

Santos = CriarPersonagem(vida=10,
                        vidaMax=10,
                        ataque=2,
                        defesa=2,
                        classe="SANTOS",
                        critico=6,
                        nome='Maicon',
                        inteligencia=2,
                        mana=4,
                        manaMax=4,
                        regenMana=1,
                        habilidades=habilidades,
                        artefatos=artefatos,
                        ouro=30,
                        caminhado=0,
                        danoMitigado=0,
                        danoAumentado=0)

Reisch = CriarPersonagem(vida=7,
                        vidaMax=7,
                        ataque=3,
                        defesa=1,
                        classe="REISCH",
                        critico=3,
                        nome='Vinicius',
                        inteligencia=3,
                        mana=9,
                        manaMax=9,
                        regenMana=1,
                        habilidades=habilidades,
                        artefatos=artefatos,
                        ouro= 30,
                        caminhado=0,
                        danoMitigado=0,
                        danoAumentado=0)
