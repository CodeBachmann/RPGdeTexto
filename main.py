from asyncio.windows_events import NULL
import random
import Funcoes
import personagens

input("Quando você ver esse simbolo !: pressione enter para continuar")
nome = input("Digite seu nome: ")
print("CLASSES!!!!!!")
print("GREG(G) \nATAQUE: 3\nDEFESA: 1\nVIDA: 8\nINTELIGENCIA: 2")
print("MAICON(M) \nATAQUE: 2\n DEFESA: 2\n VIDA: 10\nINTELIGENCIA: 2")
print("REISCH(R) \nATAQUE: 3\n DEFESA: 1\n VIDA: 7\nINTELIGENCIA: 3")

#EVENTOS
passar = False
encerrarCombate = False
emboscada = False
podeAtacar = True
criticoGarantido = False
foiCritico = True

#EFEITOS
efeitoDefesa = False
efeitoDanoAumentado = False
efeitoPodeAgir = False
efeitoMonstroPodeAtacar = False

#STATUS
vidaM = 0
vida = 0
vidaMax = 0
vidaMaxM = 0
danoM = 0
dano = 0
defesa = 0
danoAumentado = 0
experiencia = 0
marcadorArea = 0
estresse = 0
ouro = 0
caminhado = 0

#DECLARO AS PASSIVAS
passivaCabeloColorido = False
passivaCrescimentoAcelerado = False
passivaMasoquistaDaAcademia = False

#MAGIAS
magiaRapDeAcademia = False
magiaOrganizarAMente = False
magiaMultilacaoRegenerativa = False

#ARTEFATOS
#artefatoGolpeGanancioso = 0

habilidades = []
#ESCOLHA DE CLASSE
while not passar:
    decisaoClasse = input("Digite a letra inicial da sua classe : ")
    decisaoClasse = decisaoClasse.upper()
    if decisaoClasse == "M":
        print("CLASSE MAICON ESCOLHIDA")
        habilidades.append("RAP DE ANIME(RA)")
        habilidades.append("MASOQUISTA DA ACADEMIA (PASSIVA)")
        jogador = personagens.Personagem\
            (vida=10,
             vidaMax=10,
             ataque=2,
             defesa=2,
             classe="MAICON",
             critico=6,
             nome=nome,
             inteligencia=2,
             mana=4,
             xp=0,
             nivel=1,
             habilidades=habilidades,
             ouro=0,
             caminhado=0)
        passar = True
        passivaMasoquistaDaAcademia = True
        magiaRapDeAcademia = True

    elif decisaoClasse == "G":
        print("CLASSE GREG ESCOLHIDA")
        habilidades.append("ORGANIZAR A MENTE(OM)")
        habilidades.append("CABELO COLORIDO(PASSIVO)")
        jogador = personagens.Personagem\
            (vida=8,
             vidaMax=8,
             ataque=3,
             defesa=1,
             classe="GREG",
             critico=8,
             nome=nome,
             inteligencia=2,
             mana=6,
             xp=0,
             nivel=1,
             habilidades=habilidades,
             ouro= 0,
             caminhado=0)
        passar = True
        passivaCabeloColorido = True
        magiaOrganizarAMente = True
        

    elif decisaoClasse == "R":
        print("CLASSE REISCH ESCOLHIDA")
        habilidades.append("CRESCIMENTO ACELERADO(PASSIVA)")
        habilidades.append("MULTILAÇÃO REGENERATIVA (MR)")
        jogador = personagens.Personagem\
            (vida=7,
             vidaMax=7,
             ataque=3,
             defesa=1,
             classe="REISCH",
             critico=3,
             nome=nome,
             inteligencia=3,
             mana=9,
             xp=0,
             nivel=1,
             habilidades=habilidades,
             ouro= 0,
             caminhado=0)
        passar = True
        passivaCrescimentoAcelerado = True
        magiaMultilacaoRegenerativa = True
        
#ENQUANTO A VIDA DO JOGADOR FOR MAIOR QUE 0 O JOGO VAI CONTINUAR RODANDO
while jogador.vida > 0:
    danoMitigado = jogador.defesa
    if marcadorArea == 0:
        input("Você adentra a floresta de Cornwood, o sol se torna apenas um borrão entre as árvores... !:")

    print("O que você deseja: \n(D)DESCANSAR\n(C)CAMINHAR")
    decisaoExplorar = input("Qual sua escolha: ")
    decisaoExplorar = decisaoExplorar.upper()
    if decisaoExplorar == "D":
        descanso = int(input("QUANTOS TURNOS VOCÊ DESEJA DESCANSAR: "))
        tempo = 0
        while tempo < descanso and emboscada == False:
            if random.randint(1,10) == 10:
                emboscada = True
            else:
                descansoVida = round(jogador.vidaMax/5, 0)
                print(f"você recuperou {descansoVida}pontos de vida")
                jogador.vida += descansoVida
                jogador.vida = Funcoes.vidaLimite(jogador.vida, jogador.vidaMax)

    #A PARTIR DE UMA INT ALEATORIA É ESCOLHIDO UM MONSTRO PARA BATALHAR
    decisaoMonstro = random.randint(0,2)
    if marcadorArea == 0:
        if decisaoMonstro == 0:
            print("UM SLIME APARECE!!!")
            monstro = personagens.npc(vida = 6, vidaMax= 6, ataque= 2, defesa= 3,
                nome="SLIME", critico= 5, xp= 1, ouro= 10)

        elif decisaoMonstro == 1:
            print("UM GOBLIN APARECE!!!")
            monstro = personagens.npc(vida = 5, vidaMax= 5, ataque= 3, defesa= 2,
                nome="GOBLIN", critico= 7, xp= 1, ouro= 10)

        elif decisaoMonstro == 2:
            print("UM GOLEM BEBE APARECE!!!")
            monstro = personagens.npc(vida = 7, vidaMax= 6, ataque= 3, defesa= 3,
                nome="GOLEM BEBE", critico= 0, xp= 10, ouro= 15)

            efeitoMonstroPodeAtacar = 1

    #O COMBATE VAI OCORRER ENQUANTO A CONDIÇÃO "encerrarCombate" FOR FALSA
    encerrarCombate = False
    danoMitigado = monstro.defesa

    while not encerrarCombate:
        passar = False
        #AREA QUE CONTROLA BUFFS QUE DURAM MAIS DE UM TURNO
        if efeitoDefesa == 0:
            danoMitigado = jogador.defesa
        else:
            efeitoDefesa -= 1
        if efeitoPodeAgir != 0 and efeitoPodeAgir != 5:
            podeAgir = False
            efeitoPodeAgir -= 1
        elif efeitoPodeAgir == 0:
            podeAgir = True
        elif efeitoPodeAgir ==5:
            podeAgir == True
            efeitoPodeAgir = 1

        if efeitoDanoAumentado == 0:
            danoAumentado = 0
        else:
            efeitoDanoAumentado -= 1
        #ATIVA A EMBOSCADA
        if emboscada == True:
            print("VOCÊ FOI EMBOSCADO!!!")
            danoM = (monstro.ataque + (random.randint(0, monstro.ataque))) - danoMitigado
            if danoM < 0:
                danoM = 0
            print(f"Você sofreu {danoM}(-{danoMitigado}) pontos de dano\n")
            jogador.vida -= danoM
        #MOSTRA OS STATUS ATUAIS DO JOGADOR E DO MONSTRO
        Funcoes.status(monstro.vida,monstro.ataque,monstro.defesa,monstro.nome)
        Funcoes.status(jogador.vida,jogador.ataque,jogador.defesa,jogador.nome)
        Funcoes.continuar()
        #MOSTRA AS DECISOES DE COMBATE PARA O JOGADOR
        if podeAgir:
            while not passar:

                print("AÇÕES :\n(A)ATACAR\n(D)DEFENDER\n(H)HABILIDADES\n(F)FUGIR ")
                decisaoCombate = input("ESCOLHA UMA AÇÃO: ")
                decisao0Combate = decisaoCombate.upper()
                if decisaoCombate == "A":
                    monstro.vida =(Funcoes.calculaDano(monstro.vida, jogador.ataque, criticoGarantido,
                                 jogador.critico, foiCritico,passivaCabeloColorido, monstro.defesa, danoAumentado ))
                    foiCritico = False
                    passar = True
                elif decisaoCombate == "D":
                    danoMitigado = jogador.defesa*2
                    efeitoDefesa = 2
                    passar = True
                    print("SUA DEFESA FOI DOBRADA(2t)")
                #HABILIDADES
                elif decisaoCombate == "H":
                    while not passar:
                        for habilidade in habilidades:
                            print(habilidade)
                        decisaoHabilidade = input("ESCOLHA UMA HABILIDADE")
                        decisaoHabilidade = decisaoHabilidade.upper()
                        if decisaoHabilidade == "MR" and magiaMultilacaoRegenerativa:
                            jogador.vida = Funcoes.magiaMultilacaoRegenerativa(jogador.vida, jogador.vidaMax, jogador.inteligencia)
                            passar = True
                        elif decisaoHabilidade == "OM":
                            estresse -= jogador.inteligencia
                            danoMitigado += jogador.inteligencia/2
                            print("Você organiza sua mente, sua resiliencia aumenta e seu proximo golpe será critico")
                            criticoGarantido = True
                            passar = True

                        elif decisaoHabilidade == "RA":
                            danoAumentado = jogador.ataque+jogador.defesa
                            efeitoDanoAumentado = 1
                            print("Apos ouvir o RAP DO SAITAMA você sente que tem que dar tudo de si em um golpe final!!!")
                            efeitoMonstroPodeAtacar = 1
                            efeitoPodeAgir = 5
                            passar = True

                elif decisaoCombate == "F":
                    encerrarCombate = True
                    passar = True
                else:
                    print("DECISÃO INVALIDA")

        #CALCULA, APLICA E MOSTRA O DANO DO MONSTRO ALEM DE VERIFICAR SE UMA EMBOSCADA JA FOI REALIZADA

        if emboscada == True:
            emboscada = False
        elif monstro.vida > 0 and efeitoMonstroPodeAtacar == 0:
                danoM = (monstro.ataque + (random.randint(0, monstro.ataque))) - danoMitigado
                if danoM < 0:
                    danoM = 0
                print(f"Você sofreu {danoM}(-{danoMitigado}) pontos de dano\n")
                if jogador.vida == NULL:
                    jogador.vida = 0
                jogador.vida -= danoM
        elif efeitoMonstroPodeAtacar > 0:
            efeitoMonstroPodeAtacar -= 1
        if jogador.vida <= 0:
            encerrarCombate = True
            print("Você morreu... ")
        elif monstro.vida <=0:
            print("O MONSTRO MORREU!")
            encerrarCombate = True
            Funcoes.continuar()
            print(f"+{monstro.ouro}G\n+{monstro.xp}XP")
            jogador.ouro += monstro.ouro
            jogador.xp += monstro.xp
