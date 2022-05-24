from asyncio.format_helpers import _format_callback_source

class CriarPersonagem():
    def __init__(self, vida, vidaMax, ataque, defesa, classe, nome, critico,
    inteligencia, mana, manaMax, regenMana, habilidades, habilidadesDesc, artefatosDesc, 
    ouro, caminhado, danoMitigado, artefatos, danoAumentado, passar, podeAgir, criticoGarantido, foiCritico):
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
        self.habilidadesDesc = habilidadesDesc
        self.nome = nome
        self.ouro = ouro
        self.caminhado = caminhado
        self.danoMitigado = danoMitigado
        self.artefatos = artefatos
        self.artefatosDesc = artefatosDesc
        self.danoAumentado = danoAumentado
        self.passar = passar
        self.podeAgir = podeAgir
        self.criticoGarantido = criticoGarantido
        self.foiCritico = foiCritico
class timers():
    def __init__(self, defesa, podeAgir, danoAumentado, monstroAgir):
        self.defesa = defesa
        self.podeAgir = podeAgir
        self.danoAumentado = danoAumentado
        self.monstroAgir = monstroAgir

class npc():
    def __init__(self, vida, vidaMax, ataque, defesa, nome, critico, ouro, danoMitigado, podeAgir):
        self.vida = vida
        self.vidaMax = vidaMax
        self.ataque = ataque
        self.defesa = defesa
        self.nome = nome
        self.critico = critico
        self.ouro = ouro
        self.danoMitigado= danoMitigado
        self.podeAgir = podeAgir

#-------------------------------------------- Personagens ---------------------------------------------------------
habilidades = []
habilidadesDesc = []
artefatos = []
artefatosDesc = []
efx = timers(defesa = 0,
            podeAgir= 0,
            danoAumentado = 0,
            monstroAgir = 0)

Sabel = CriarPersonagem(vida=26,
                        vidaMax=26,
                        ataque=8,
                        defesa=34,
                        classe="SABEL",
                        critico=8,
                        nome='Greg',
                        inteligencia=2,
                        mana=6,
                        manaMax=6,
                        regenMana=1,
                        habilidades=habilidades,
                        artefatos=artefatos,
                        habilidadesDesc=habilidadesDesc,
                        artefatosDesc= artefatosDesc,
                        ouro= 100,
                        caminhado=0,
                        danoMitigado=0,
                        danoAumentado=0,
                        passar = False,
                        podeAgir= True,
                        criticoGarantido = False,
                        foiCritico= False)

Santos = CriarPersonagem(vida=30,
                        vidaMax=30,
                        ataque=5,
                        defesa=55,
                        classe="SANTOS",
                        critico=6,
                        nome='Maicon',
                        inteligencia=2,
                        mana=4,
                        manaMax=4,
                        regenMana=1,
                        habilidades=habilidades,
                        habilidadesDesc=habilidadesDesc,
                        artefatosDesc= artefatosDesc,
                        artefatos=artefatos,
                        ouro=30,
                        caminhado=0,
                        danoMitigado=0,
                        danoAumentado=0,
                        passar = False,
                        podeAgir= True,
                        criticoGarantido = False,
                        foiCritico= False)

Reisch = CriarPersonagem(vida=21,
                        vidaMax=21,
                        ataque=8,
                        defesa=34,
                        classe="REISCH",
                        critico=3,
                        nome='Vinicius',
                        inteligencia=3,
                        mana=9,
                        manaMax=9,
                        regenMana=1,
                        habilidades=habilidades,
                        habilidadesDesc=habilidadesDesc,
                        artefatosDesc= artefatosDesc,
                        artefatos=artefatos,
                        ouro= 30,
                        caminhado=0,
                        danoMitigado=0,
                        danoAumentado=0,
                        passar = False,
                        podeAgir= True,
                        criticoGarantido = False,
                        foiCritico= False)


