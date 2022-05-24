from asyncio.windows_events import NULL
import random
from re import T
from time import monotonic, sleep
import Funcoes
import personagens
import os
import Effects
import Skills
input("Quando você ver esse simbolo '!' : pressione enter para continuar ou espere um pouco")
sleep(1)
os.system('cls') or None
nome = input("Digite seu nome: ")
print("\n ------------CLASSES------------")

Funcoes.apresentacaoDeClasse(personagens.Sabel, 'o somelier de estagio(S)')
Funcoes.apresentacaoDeClasse(personagens.Santos, 'o bombado(SA)')
Funcoes.apresentacaoDeClasse(personagens.Reisch, 'o emo feliz(R)')

#EVENTOS
encerrarCombate = False
emboscada = False
monologo = False

#CAMINHOS
enfrentarMonstroElite = False
caminhoChefe = False
enfrentarMonstroComun = False
acessarMisterio = False

#STATUS
danoM = 0
dano = 0
ouro = 0
marcadorArea = 0
artefatos = []

#ITENS
itemPedraCoracao = False
habilidades = []
classes = ["SA", "S", "R"]
decisaoClasse = ""
efeito = personagens.efx

#ESCOLHA DE CLASSE
while decisaoClasse not in classes:
  decisaoClasse = input("Digite a letra inicial da sua classe : ")
  decisaoClasse = decisaoClasse.upper()
  if decisaoClasse in classes:
    if decisaoClasse == "SA":

        jogador = personagens.Santos
        jogador.artefatos.append("AMDA")#Artefato >Masoquista da academia<        
                                    #sempre que o jogador recebe dano, o proximo ataque do jogador causa dano extra
        jogador.habilidades.append("HRDA")

    elif decisaoClasse == "S":

        jogador = personagens.Sabel
        jogador.artefatos.append("ACC")#Critico recupera vida e ignora o dano mitigado
        jogador.habilidades.append("HOAM")

    elif decisaoClasse == "R":

        jogador = personagens.Reisch
        jogador.artefatos.append("ACD") #Artefato >Conhecimento da dor<
                                        #sempre que o jogador recebe dano metade desse dano é convertido em mana
        jogador.habilidades.append("HMR")

os.system('cls') or None
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
        monologo = False

    print("~~~~~~Caminhos~~~~~~\n")
    caminhoMisterio = False
    caminhoMonstroComun = False
    caminhoMonstroElite = False
    caminhoLoja = False
    jogador.passar = False

    while not jogador.passar:
        jogador.caminhado += 1
        caminhos = random.randint(4,5)
        print(f"Seu saldo: {jogador.ouro}\n\nVocê pode: ")
        cont = 0
        if jogador.caminhado < 10:
            while cont < caminhos:
                escolha = random.randint(1, 100)
                if escolha > 0 and escolha <= 50:
                    print(f"Lutar com um monstro comun(C)\n")
                    caminhoMonstroComun = True
                # elif escolha > 50 and escolha <= 75:
                #     print(f"Investigar um misterio(M)\n")
                #     caminhoMisterio = True
                elif escolha > 50 and escolha <= 80:
                    print(f"Lutar com um monstro de Elite(E)\n")
                    caminhoMonstroElite = True
                elif escolha > 80 and escolha <= 100:
                    print(f"Entrar na loja(L)\n")
                    caminhoLoja = True
                cont+= 1
        else:
            input(f"Você sente uma presença ameaçadora !:")
            caminhoChefe = True
            jogador.caminhado = 0
            jogador.passar = True
            break

        while True:

            decisaoExplorar = input("\nQual sua escolha: ")
            decisaoExplorar = decisaoExplorar.upper()

            if caminhoChefe:
                
                jogador.passar = True
            elif decisaoExplorar == "C" and caminhoMonstroComun:
                enfrentarMonstroComun = True
                jogador.passar = True
                break

            elif decisaoExplorar == "E" and caminhoMonstroElite:
                enfrentarMonstroElite = True
                jogador.passar = True
                break

            elif decisaoExplorar == "L" and caminhoLoja:
                Funcoes.comprarNaLoja(jogador)
                break
                
            elif decisaoExplorar == "M" and caminhoMisterio:
                acessarMisterio = True
                jogador.passar = True
                break

            else:
                print("Decisao Invalida")

        os.system('cls') or None

    #A PARTIR DE UMA INT ALEATORIA É ESCOLHIDO UM MONSTRO PARA BATALHAR
    decisaoMonstro = random.randint(0,1)
    if marcadorArea == 0:
        if decisaoMonstro == 0 and enfrentarMonstroComun:

            print("UM SLIME APARECE!!!\n")
            monstro = personagens.npc(vida = 20, vidaMax= 20, ataque= 4, defesa= 50,
                nome="SLIME", critico= 5, ouro= 23, danoMitigado=3, podeAgir = True)
            enfrentarMonstroComun = False

        elif decisaoMonstro == 1 and enfrentarMonstroComun:
            print("UM GOBLIN APARECE!!!\n")
            monstro = personagens.npc(vida = 17, vidaMax= 17, ataque= 6, defesa= 30,
                nome="GOBLIN", critico= 7, ouro=23, danoMitigado=2, podeAgir = True)
            enfrentarMonstroComun = False

        elif enfrentarMonstroElite:
            print("UM GOLEM BEBE APARECE!!!\n")
            monstro = personagens.npc(vida = 35, vidaMax= 35, ataque= 8, defesa= 80,
                nome="GOLEM BEBE", critico= 0, ouro= 40, danoMitigado= 3, podeAgir = True)
            efeito.monstroAgir = 1
            enfrentarMonstroElite = False

        elif caminhoChefe:
            print("O REI SLIME SE IRRITOU COM SEUS ATOS!!!\n")
            monstro = personagens.npc(vida = 75, vidaMax= 75, ataque= 13, defesa= 70,
                nome="REI SLIME", critico= 0, ouro= 100, danoMitigado= 3, podeAgir = True)
            caminhoChefe = False
            marcadorArea = 1

    #O COMBATE VAI OCORRER ENQUANTO A CONDIÇÃO "encerrarCombate" FOR FALSA
    encerrarCombate = False
    monstro.danoMitigado = monstro.defesa

    while not encerrarCombate:
        jogador.passar = False
        
        #AREA QUE CONTROLA BUFFS QUE DURAM MAIS DE UM TURNO
        if efeito.defesa == 0:
            jogador.danoMitigado = jogador.defesa
        else:
            efeito.defesa -= 1
        #MELHORAR O SISTEMA DE STUN
        Effects.atordoar(jogador, efeito)
        #BUFFAR DANO
        if efeito.danoAumentado == 0:
            jogador.danoAumentado = 0
        else:
            efeito.danoAumentado = efeito.danoAumentado - 1

        #ATIVA A EMBOSCADA
        if emboscada:
            print("VOCÊ FOI EMBOSCADO!!!\n")
            danoM = (monstro.ataque + (random.randint(0, monstro.ataque))) - jogador.danoMitigado
            if danoM < 0:
                danoM = 0
            print(f"Você sofreu {danoM}(-{jogador.danoMitigado}) pontos de dano\n")
            jogador.vida -= danoM

        #MOSTRA OS STATUS ATUAIS DO JOGADOR E DO MONSTRO
        Funcoes.status(monstro)
        Funcoes.status(jogador)
        Funcoes.continuar()
        #MOSTRA AS DECISOES DE COMBATE PARA O JOGADOR
        if jogador.podeAgir:
            jogador.passar = False
            while not jogador.passar:

                print("AÇÕES :\n(A)ATACAR\n(D)DEFENDER\n(H)HABILIDADES\n(F)FUGIR\n(I)ITENS\n")
                decisaoCombate = input("ESCOLHA UMA AÇÃO: ")
                decisaoCombate = decisaoCombate.upper()
                os.system('cls') or None

                if decisaoCombate == "A":
                    Funcoes.atacar(jogador, monstro)

                elif decisaoCombate == "D":
                    danoMitigado = jogador.defesa*2
                    efeito.Defesa = 2
                    jogador.passar = True
                    print("SUA DEFESA FOI DOBRADA(2t)\n")

                #habilidadeS
                elif decisaoCombate == "H":

                    while True:
                        Funcoes.adicionarHabilidade(jogador)
                        for habilidade in jogador.habilidadesDesc:
                            print(habilidade)

                        print("Voltar(V)")
                        decisaoHabilidade = (input("ESCOLHA UMA HABILIDADE: ")).upper()

                        if decisaoHabilidade == "HMR" and "HMR" in jogador.habilidades and jogador.mana >= 3:
                            sleep(1)
                            Skills.multilacaoRegenerativa(jogador, monstro)
                            break

                        elif decisaoHabilidade == "HOAM" and "HOAM" in jogador.habilidades:
                            Skills.organizarAMente(jogador)
                            break

                        elif decisaoHabilidade == "HRDA" and "HRDA" in jogador.habilidades:
                            Skills.rapDeAcademia(jogador, efeito)
                            break

                        elif "V":
                            break

                        else:
                            print("")

                elif decisaoCombate == "F":
                    encerrarCombate = True
                    jogador.passar = True
                elif decisaoCombate == "I":
                    Funcoes.todosOsStatus(jogador)
                else:
                    print("")

        #CALCULA, APLICA E MOSTRA O DANO DO MONSTRO ALEM DE VERIFICAR SE UMA EMBOSCADA JA FOI REALIZADA
        if emboscada:
            emboscada = False
        elif monstro.vida > 0 and efeito.monstroAgir == 0:
            danoM = (monstro.ataque + (random.randint(0, monstro.ataque))) - danoMitigado
            if "ACD" in jogador.artefatos:
                jogador.mana += int(danoM/2)
                print(f"você recupera {int(danoM/2)} pontos de mana")
            if "AMDA" in jogador.artefatos:
                jogador.danoAumentado = int(danoM/2)
                print("A dor te motiva, seu proximo ataque causa dano extra")
            if danoM < 0:
                danoM = 0
            print(f"Você sofreu {danoM}(-{danoMitigado}) pontos de dano\n")
            if jogador.vida == NULL:
                jogador.vida = 0
            jogador.vida -= danoM

        elif efeito.monstroAgir > 0:
            efeito.monstroAgir -= 1

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
            efeito.podeAgir = 0