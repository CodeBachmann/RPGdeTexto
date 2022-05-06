from asyncio.windows_events import NULL
import random
from time import sleep

from pyparsing import And
import Funcoes
import personagens
import os
#diogo
input("Quando você ver esse simbolo '!' : pressione enter para continuar ou espere um pouco")
sleep(3)
os.system('cls') or None
nome = input("Digite seu nome: ")
print("\n ------------CLASSES------------")

print("""SABEL, o somelier de estagio(S) 
  ATAQUE: 3
  DEFESA: 1
  VIDA: 8
  INTELIGENCIA: 2
""")

print("""SANTOS, o bombado(SA) 
  ATAQUE: 2 
  DEFESA: 2
  VIDA: 10 
  INTELIGENCIA: 2
""")

print("""REISCH, o emo feliz(R) 
  ATAQUE: 3
  DEFESA: 1
  VIDA: 7
  INTELIGENCIA: 3
""")


#EVENTOS
passar = False
encerrarCombate = False
emboscada = False
podeAtacar = True
criticoGarantido = False
foiCritico = True
monologo = False

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

#ARTEFATOS COMUNS
artefatoGolpeGanancioso = False

#ITENS
itemPedraCoracao = False


habilidades = []
#ESCOLHA DE CLASSE
while not passar:
    decisaoClasse = input("Digite a letra inicial da sua classe : ")
    decisaoClasse = decisaoClasse.upper()
    if decisaoClasse == "SA":
        print("CLASSE SANTOS ESCOLHIDA")
        habilidades.append("RAP DE ANIME(RA)")
        habilidades.append("MASOQUISTA DA ACADEMIA (PASSIVA)")
        jogador = personagens.Personagem\
            (vida=10,
             vidaMax=10,
             ataque=2,
             defesa=2,
             classe="SANTOS",
             critico=6,
             nome=nome,
             inteligencia=2,
             mana=4,         
             habilidades=habilidades,
             ouro=0,
             caminhado=0)
        passar = True
        passivaMasoquistaDaAcademia = True
        magiaRapDeAcademia = True

    elif decisaoClasse == "S":
        print("CLASSE SABEL ESCOLHIDA")
        habilidades.append("ORGANIZAR A MENTE(OM)")
        habilidades.append("CABELO COLORIDO(PASSIVO)")
        jogador = personagens.Personagem\
            (vida=8,
             vidaMax=8,
             ataque=3,
             defesa=1,
             classe="SABEL",
             critico=8,
             nome=nome,
             inteligencia=2,
             mana=6,
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
             habilidades=habilidades,
             ouro= 0,
             caminhado=0)
        passar = True
        passivaCrescimentoAcelerado = True
        magiaMultilacaoRegenerativa = True
    sleep(1)
    os.system('cls') or None
        
#ENQUANTO A VIDA DO JOGADOR FOR MAIOR QUE 0 O JOGO VAI CONTINUAR RODANDO
while jogador.vida > 0:
    danoMitigado = jogador.defesa
    if marcadorArea == 0 and not monologo:
        input("Você adentra a floresta de Cornwood, o sol se torna apenas um borrão entre as árvores... !:")
        os.system('cls') or None
        monologo = True
    elif marcadorArea == 1 and monologo:
        input

    print("Caminhos")
    caminhoMisterio = False
    caminhoMonstroComun = False
    caminhoMonstroElite = False
    caminhoLoja = False

    while not passar:
        passarCaminho = False
        jogador.caminhado += 1
        caminhos = random.randint(1,3)
        input("Você pode:")
        cont = 0
        while cont < caminhos:
            escolha = random.randint(1, 100)
            if escolha > 0 and escolha <= 50:
                print(f"Lutar com um monstro comun(MC)\n")
            elif escolha > 50 and escolha <= 75:
                print(f"Investigar um misterio(M)\n")
            elif escolha > 75 and escolha <= 90:
                print(f"Lutar com um monstro de Elite(E)\n")
            elif escolha > 90 and escolha <= 100:
                print(f"Entrar na loja(L)\n")

        while not passarCaminho:

            decisaoExplorar = input("Qual sua escolha: ")
            decisaoExplorar = decisaoExplorar.upper()

            if decisaoExplorar == "MC" and caminhoMonstroComun:
                enfrentarMonstroComun = True
            elif decisaoExplorar == "E" and caminhoMonstroElite:
                enfrentarMonstroElite = True
            elif decisaoExplorar == "L" and caminhoLoja:
                input("Você adentra a loja.. !:")
                itemLoja = random.randint(0,100)
                
                
            #elif decisaoExplorar == "M" and caminhoMisterio:
            #   acessarMisterio = True
            #else:
            #   decisaoInvalida

        os.system('cls') or None

    #A PARTIR DE UMA INT ALEATORIA É ESCOLHIDO UM MONSTRO PARA BATALHAR
    decisaoMonstro = random.randint(0,1)
    if marcadorArea == 0:
        if decisaoMonstro == 0:
            print("UM SLIME APARECE!!!\n")
            monstro = personagens.npc(vida = 6, vidaMax= 6, ataque= 2, defesa= 3,
                nome="SLIME", critico= 5, ouro= 9)

        elif decisaoMonstro == 1:
            print("UM GOBLIN APARECE!!!\n")
            monstro = personagens.npc(vida = 5, vidaMax= 5, ataque= 3, defesa= 2,
                nome="GOBLIN", critico= 7, ouro= 9)

        elif decisaoMonstro == 2:
            print("UM GOLEM BEBE APARECE!!!\n")
            monstro = personagens.npc(vida = 7, vidaMax= 6, ataque= 3, defesa= 3,
                nome="GOLEM BEBE", critico= 0, ouro= 15)

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
        #MELHORAR O SISTEMA DE STUN 
        if efeitoPodeAgir != 0 and efeitoPodeAgir != 5:
            podeAgir = False
            efeitoPodeAgir -= 1
        elif efeitoPodeAgir == 0:
            podeAgir = True
        elif efeitoPodeAgir ==5:
            podeAgir = True
            efeitoPodeAgir = 1

        if efeitoDanoAumentado == 0:
            danoAumentado = 0
        else:
            efeitoDanoAumentado -= 1

        #ATIVA A EMBOSCADA
        if emboscada:
            print("VOCÊ FOI EMBOSCADO!!!\n")
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

                print("AÇÕES :\n(A)ATACAR\n(D)DEFENDER\n(H)HABILIDADES\n(F)FUGIR\n(I)ITENS\n")
                decisaoCombate = input("ESCOLHA UMA AÇÃO: ")
                decisaoCombate = decisaoCombate.upper()
                os.system('cls') or None

                if decisaoCombate == "A":
                    monstro.vida =(Funcoes.calculaDano(monstro.vida, jogador.ataque, criticoGarantido,
                                 jogador.critico, foiCritico,passivaCabeloColorido, monstro.defesa, danoAumentado ))
                    foiCritico = False
                    passar = True

                elif decisaoCombate == "D":
                    danoMitigado = jogador.defesa*2
                    efeitoDefesa = 2
                    passar = True
                    print("SUA DEFESA FOI DOBRADA(2t)\n")

                #MAGIAS
                elif decisaoCombate == "H":
                    while not passar:

                        for habilidade in habilidades:
                            print(habilidade)

                        decisaoHabilidade = input("ESCOLHA UMA HABILIDADE")
                        decisaoHabilidade = decisaoHabilidade.upper()
                        if decisaoHabilidade == "MR" and magiaMultilacaoRegenerativa:
                            print("Voce se multila com as unhas e oferece seu sangue a xaoc")
                            sleep(1)
                            jogador.vida = Funcoes.magiaMultilacaoRegenerativa(jogador.vida, jogador.vidaMax, jogador.inteligencia)
                            passar = True

                        elif decisaoHabilidade == "OM" and magiaOrganizarAMente:
                            estresse -= jogador.inteligencia
                            danoMitigado += jogador.inteligencia/2
                            input("Você organiza sua mente, sua resiliencia aumenta e seu proximo golpe será critico ")
                            sleep(1)
                            criticoGarantido = True
                            passar = True

                        elif decisaoHabilidade == "RA" and magiaRapDeAcademia:
                            danoAumentado = jogador.ataque+jogador.defesa
                            efeitoDanoAumentado = 1
                            print("Apos ouvir o RAP DO SAITAMA você sente que tem que dar tudo de si em um golpe final!!!")
                            sleep(1)
                            efeitoMonstroPodeAtacar = 1
                            efeitoPodeAgir = 5
                            passar = True

                elif decisaoCombate == "F":
                    encerrarCombate = True
                    passar = True
                elif decisaoCombate == "I":
                    print()
                else:
                    print("DECISÃO INVALIDA")

        #CALCULA, APLICA E MOSTRA O DANO DO MONSTRO ALEM DE VERIFICAR SE UMA EMBOSCADA JA FOI REALIZADA

        if emboscada:
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
            ouro = random.randint(int(monstro.ouro/2),int(monstro.ouro*1.5))
            print(f"+{ouro}G")
            jogador.ouro += ouro