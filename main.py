from asyncio.windows_events import NULL
import random
from re import T
from time import sleep
import Funcoes
import personagens
import os
input("Quando você ver esse simbolo '!' : pressione enter para continuar ou espere um pouco")
sleep(2)
os.system('cls') or None
nome = input("Digite seu nome: ")
print("\n ------------CLASSES------------")



print(f"""{personagens.Sabel.classe}, o somelier de estagio(S) 
  ATAQUE:       {personagens.Sabel.ataque}
  DEFESA:       {personagens.Sabel.defesa}
  VIDA:         {personagens.Sabel.vida}
  INTELIGENCIA: {personagens.Sabel.inteligencia}
""")

print(f"""{personagens.Santos.classe}, o bombado(SA) 
  ATAQUE:       {personagens.Santos.ataque}
  DEFESA:       {personagens.Santos.defesa}
  VIDA:         {personagens.Santos.vida}
  INTELIGENCIA: {personagens.Santos.inteligencia}
""")

print(f"""{personagens.Reisch.classe}, o emo feliz(R) 
  ATAQUE:       {personagens.Reisch.ataque}
  DEFESA:       {personagens.Reisch.defesa}
  VIDA:         {personagens.Reisch.vida}
  INTELIGENCIA: {personagens.Reisch.inteligencia}
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

#CAMINHOS
enfrentarMonstroElite = False
caminhoChefe = False

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
artefatoLagrimaDoBerserker = False
artefatos = []

#ITENS
itemPedraCoracao = False


habilidades = []
#ESCOLHA DE CLASSE
while not passar:
  decisaoClasse = input("Digite a letra inicial da sua classe : ")
  decisaoClasse = decisaoClasse.upper()
  if decisaoClasse == "SA":

      jogador = personagens.Santos        
      
      passar = True
      passivaMasoquistaDaAcademia = True
      magiaRapDeAcademia = True

  elif decisaoClasse == "S":

      jogador = personagens.Sabel

      passar = True
      passivaCabeloColorido = True
      magiaOrganizarAMente = True
      

  elif decisaoClasse == "R":

      jogador = personagens.Reisch

      passar = True
      passivaCrescimentoAcelerado = True
      magiaMultilacaoRegenerativa = True

        
print(f"CLASSE {jogador.classe} ESCOLHIDA")
sleep(2)
os.system('cls') or None
#ENQUANTO A VIDA DO JOGADOR FOR MAIOR QUE 0 O JOGO VAI CONTINUAR RODANDO
while jogador.vida > 0:
    danoMitigado = jogador.defesa
    if marcadorArea == 0 and not monologo:
        input("Você adentra a floresta de Cornwood, o sol se torna apenas um borrão entre as árvores... !:")
        os.system('cls') or None
        monologo = True
    elif marcadorArea == 1 and monologo:
        input("!:")

    print("Caminhos")
    caminhoMisterio = False
    caminhoMonstroComun = False
    caminhoMonstroElite = False
    caminhoLoja = False
    passar = False

    while not passar:
        passarCaminho = False
        jogador.caminhado += 1
        caminhos = random.randint(7,8)
        input("Você pode:")
        cont = 0
        if jogador.caminhado < 10:
            while cont < caminhos:
                escolha = random.randint(1, 100)
                if escolha > 0 and escolha <= 50:
                    print(f"Lutar com um monstro comun(C)\n")
                    caminhoMonstroComun = True
                elif escolha > 50 and escolha <= 75:
                    print(f"Investigar um misterio(M)\n")
                    caminhoMisterio = True
                elif escolha > 75 and escolha <= 90:
                    print(f"Lutar com um monstro de Elite(E)\n")
                    caminhoMonstroElite = True
                elif escolha > 90 and escolha <= 100:
                    print(f"Entrar na loja(L)\n")
                    caminhoLoja = True
                cont+= 1
        else:
            input(f"Você sente uma presença ameaçadora !:")
            caminhoChefe = True

        while not passarCaminho:

            decisaoExplorar = input("Qual sua escolha: ")
            decisaoExplorar = decisaoExplorar.upper()

            if caminhoChefe:
                passarCaminho = True
                passar = True
            elif decisaoExplorar == "C" and caminhoMonstroComun:
                enfrentarMonstroComun = True
                passarCaminho = True
                passar = True
            elif decisaoExplorar == "E" and caminhoMonstroElite:
                enfrentarMonstroElite = True
                passarCaminho = True
                passar = True
            elif decisaoExplorar == "L" and caminhoLoja:
                Funcoes.comprarNaLoja(jogador)
                passarCaminho = True
            elif decisaoExplorar == "M" and caminhoMisterio:
              acessarMisterio = True
              passarCaminho = True
              passar = True
            else:
                print("Decisao Invalida")

        os.system('cls') or None

    #A PARTIR DE UMA INT ALEATORIA É ESCOLHIDO UM MONSTRO PARA BATALHAR
    decisaoMonstro = random.randint(0,1)
    if marcadorArea == 0:
        if decisaoMonstro == 0:
            print("UM SLIME APARECE!!!\n")
            monstro = personagens.npc(vida = 6, vidaMax= 6, ataque= 2, defesa= 3,
                nome="SLIME", critico= 5, ouro= 23)

        elif decisaoMonstro == 1:
            print("UM GOBLIN APARECE!!!\n")
            monstro = personagens.npc(vida = 5, vidaMax= 5, ataque= 3, defesa= 2,
                nome="GOBLIN", critico= 7, ouro=23)

    if enfrentarMonstroElite:
        print("UM GOLEM BEBE APARECE!!!\n")
        monstro = personagens.npc(vida = 7, vidaMax= 6, ataque= 3, defesa= 3,
            nome="GOLEM BEBE", critico= 0, ouro= 40)

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

                        decisaoHabilidade = input("ESCOLHA UMA HABILIDADE: ")
                        decisaoHabilidade = decisaoHabilidade.upper()
                        if decisaoHabilidade == "HMR" and "HMR" in jogador.habilidades:
                            print("Voce se multila com as unhas e oferece seu sangue a xaoc")
                            sleep(1)
                            jogador.vida = Funcoes.magiaMultilacaoRegenerativa(jogador.vida, jogador.vidaMax, jogador.inteligencia)
                            passar = True

                        elif decisaoHabilidade == "HOAM" and "HOAM" in jogador.habilidades:
                            estresse -= jogador.inteligencia
                            danoMitigado += jogador.inteligencia/2
                            input("Você organiza sua mente, sua resiliencia aumenta e seu proximo golpe será critico ")
                            sleep(1)
                            criticoGarantido = True
                            passar = True

                        elif decisaoHabilidade == "HRDA" and "HRDA" in jogador.habilidades:
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
            sleep(1)
            exit(0)

        elif monstro.vida <=0:
            print("O MONSTRO MORREU!")
            encerrarCombate = True
            Funcoes.continuar()
            ouro = random.randint(int(monstro.ouro/2),int(monstro.ouro*1.5))
            print(f"+{ouro}G")
            jogador.ouro += ouro