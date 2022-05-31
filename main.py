from asyncio.windows_events import NULL
from distutils.command.clean import clean
from operator import truediv
import random
from re import T
from time import monotonic, sleep
from typing import Any
import Funcoes
import personagens
import os
import Artefacts
import Effects
import Skills
import Loja
import keyboard
# --------------------------------- VARIÁVEIS --------------------------------- #

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
dano = 0
ouro = 0
marcadorArea = 0
artefatos = []

habilidades = []
classes = ["SA", "S", "R"]
decisaoClasse = ""
decisaoHabilidade = ""
efeito = personagens.efx

# --------------------------------- INÍCIO --------------------------------- #
os.system('cls') or None
nome = input("Digite seu nome: ")
os.system('cls') or None
print("\n ------------CLASSES------------")

Funcoes.apresentacaoDeClasse(personagens.Santos, 'o bombado(1)')
Funcoes.apresentacaoDeClasse(personagens.Sabel, 'o somelier de estagio(2)')
Funcoes.apresentacaoDeClasse(personagens.Reisch, 'o emo feliz(3)')
quebra = False

#ESCOLHA DE CLASSE

while True:
        if keyboard.read_key() == "1":

            personagens.Santos.artefatos.append("AMDA")
            personagens.Santos.habilidades.append("HRDA")
            jogador = personagens.Santos
            break

        elif keyboard.read_key() == "2":

            personagens.Sabel.artefatos.append("ACC")
            personagens.Sabel.habilidades.append("HOAM")
            jogador = personagens.Sabel
            break

        elif keyboard.read_key() == "3":

            personagens.Reisch.artefatos.append("ACD") 
            personagens.Reisch.habilidades.append("HMR")
            jogador = personagens.Reisch
            break

# input("1")
print(f"CLASSE {jogador.classe} ESCOLHIDA")
sleep(2)
os.system('cls') or None
jogador.nome = nome
os.system('cls') or None
sleep(2)

#ENQUANTO A VIDA DO JOGADOR FOR MAIOR QUE 0 O JOGO VAI CONTINUAR RODANDO
while jogador.vida > 0:
    if marcadorArea == 0 and not monologo:
        print("Você adentra a floresta de Cornwood, o sol se torna apenas um borrão entre as árvores...")
        sleep(1)
        os.system('cls') or None
        monologo = True
    elif marcadorArea == 1 and monologo:
        input("JOGO EM CONSTRUÇÃO!!!")
        exit()
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
        if jogador.caminhado < 10 and jogador.caminhado != 1:
            while cont < caminhos:
                escolha = random.randint(1, 100)
                if escolha > 0 and escolha <= 50:
                    print(f"Lutar com um monstro comun(1)\n")
                    caminhoMonstroComun = True
                elif escolha > 50 and escolha <= 80:
                    print(f"Lutar com um monstro de Elite(2)\n")
                    caminhoMonstroElite = True
                elif escolha > 80 and escolha <= 100:
                    print(f"Entrar na loja(3)\n")
                    caminhoLoja = True
                cont+= 1
        elif jogador.caminhado == 1:
            print(f"Lutar com um monstro comun(1)\n")
            caminhoMonstroComun = True
        else:
            input(f"Você sente uma presença ameaçadora !:")
            caminhoChefe = True
            jogador.caminhado = 0
            jogador.passar = True
            break

        while True:
            if caminhoChefe:
                jogador.passar = True
                break

            elif keyboard.read_key() == "1" and caminhoMonstroComun:
                enfrentarMonstroComun = True
                jogador.passar = True
                break

            elif keyboard.read_key() == "2" and caminhoMonstroElite:
                enfrentarMonstroElite = True
                jogador.passar = True
                break

            elif keyboard.read_key() == "3" and caminhoLoja:
                Loja.comprarNaLoja(jogador)
                break
                
            else:
                print("Decisao Invalida")

        os.system('cls') or None
        

    #A PARTIR DE UMA INT ALEATORIA É ESCOLHIDO UM MONSTRO PARA BATALHAR
    decisaoMonstro = random.randint(0,1)
    if marcadorArea == 0:
        if decisaoMonstro == 0 and enfrentarMonstroComun:

            print("UM SLIME APARECE!!!\n")
            monstro = personagens.npc(vida = 20, vidaMax= 20, ataque= 4, defesa= 24,
                nome="SLIME", critico= 5, ouro= 23, podeAgir = True, dano = 0, danoReal = 0)
            enfrentarMonstroComun = False

        elif decisaoMonstro == 1 and enfrentarMonstroComun:
            print("UM GOBLIN APARECE!!!\n")
            monstro = personagens.npc(vida = 17, vidaMax= 17, ataque= 6, defesa= 15,
                nome="GOBLIN", critico= 7, ouro=23, podeAgir = True, dano = 0, danoReal = 0)
            enfrentarMonstroComun = False

        elif enfrentarMonstroElite:
            print("UM GOLEM BEBE APARECE!!!\n")
            monstro = personagens.npc(vida = 35, vidaMax= 35, ataque= 8, defesa= 41,
                nome="GOLEM BEBE", critico= 0, ouro= 40, podeAgir = True, dano = 0, danoReal = 0)
            efeito.monstroAgir = 1
            enfrentarMonstroElite = False

        elif caminhoChefe:
            print("O REI SLIME SE IRRITOU COM SEUS ATOS!!!\n")
            monstro = personagens.npc(vida = 50, vidaMax= 50, ataque= 10, defesa= 36,
                nome="REI SLIME", critico= 0, ouro= 100, podeAgir = True, dano = 0, danoReal = 0)
            caminhoChefe = False
            marcadorArea = 1

    #O COMBATE VAI OCORRER ENQUANTO A CONDIÇÃO "encerrarCombate" FOR FALSA
    encerrarCombate = False
    efeito.tempoCombate = 0
    
    #monstro.danoMitigado = monstro.defesa

    while not encerrarCombate:
        jogador.acaoBonus = True
        jogador.passar = False
        efeito.tempoCombate += 1
        Funcoes.manaLimite(jogador)
        Effects.atordoar(jogador, efeito)

        #MOSTRA OS STATUS ATUAIS DO JOGADOR E DO MONSTRO
        Funcoes.statusMonstro(monstro)
        Funcoes.status(jogador)
        sleep(1)
        #MOSTRA AS DECISOES DE COMBATE PARA O JOGADOR
        if jogador.podeAgir:
            jogador.passar = False
            while not jogador.passar:
                print("AÇÕES :\n(1)ATACAR\n(2)HABILIDADES\n(3)FUGIR\n(4)ITENS\n")
                
                if keyboard.read_key() == "1":
                    Funcoes.atacar(jogador, monstro, efeito)

                elif keyboard.read_key() == "2":
                    while True:
                        Funcoes.adicionarHabilidade(jogador, efeito)
                        for habilidade in jogador.habilidadesDesc:
                            print(habilidade)
                        print(f"{efeito.quantidadeHabilidades} - Voltar")
                        volta = str(efeito.quantidadeHabilidades)

                        while True:
                            
                            if 1 <= efeito.quantidadeHabilidades and keyboard.read_key() == "0":
                                decisaoHabilidade = jogador.habilidades[0]
                                break

                            if 2 <= efeito.quantidadeHabilidades and keyboard.read_key() == "1":  
                                decisaoHabilidade = jogador.habilidades[1]
                                break

                            if 3 <= efeito.quantidadeHabilidades and keyboard.read_key() == "2":
                                decisaoHabilidade = jogador.habilidades[2]
                                break
                            
                            if 4 <= efeito.quantidadeHabilidades and keyboard.read_key() == "3":
                                decisaoHabilidade = jogador.habilidades[3]
                                break

                            if keyboard.read_key() == volta:
                                decisaoHabilidade = "V"
                                break

                        efeito.quantidadeHabilidades = 0
                        jogador.habilidadesDesc = []
                        
                        if decisaoHabilidade == "HMR" and "HMR" in jogador.habilidades and jogador.mana >= 4:
                            sleep(1)
                            Skills.multilacaoRegenerativa(jogador, monstro)
                            break

                        elif decisaoHabilidade == "HOAM" and "HOAM" in jogador.habilidades and jogador.mana >= 2:
                            Skills.organizarAMente(jogador)
                            break

                        elif decisaoHabilidade == "HRDA" and "HRDA" in jogador.habilidades and jogador.mana >= 2:
                            Skills.rapDeAcademia(jogador, efeito)
                            break

                        elif decisaoHabilidade == "HCL" and "HCL" in jogador.habilidades and jogador.mana >= 3:
                            Skills.curaLeve(jogador)
                            break

                        elif decisaoHabilidade == "HPA" and "HPA" in jogador.habilidades and jogador.mana >= 3:
                            Skills.pancadaAtordoante(jogador, monstro, efeito)

                        elif "V":
                            break

                        else:
                            print("Decisao invalida!!")

                elif keyboard.read_key() == "3":
                    encerrarCombate = True
                    jogador.passar = True
                elif keyboard.read_key() == "4":
                    Funcoes.todosOsStatus(jogador)
                    print("\n")
                else:
                    print("")
        jogador.mana += jogador.regenMana
        #CALCULA, APLICA E MOSTRA O DANO DO MONSTRO ALEM DE VERIFICAR SE UMA EMBOSCADA JA FOI REALIZADA
        if monstro.vida > 0 and efeito.monstroAgir == 0:
           Funcoes.monstroAtacar(jogador, monstro)

        elif efeito.monstroAgir > 0:
            print("O monstro não age nesse turno!")
            efeito.monstroAgir -= 1

        if jogador.vida <= 0:
            encerrarCombate = True
            print("Você morreu... ")
            sleep(2)
            exit(0)

        elif monstro.vida <=0:
            print("O MONSTRO MORREU!")
            Artefacts.idoloXaoc(jogador, monstro)
            encerrarCombate = True
            sleep(1)
            ouro = random.randint(int(monstro.ouro),int(monstro.ouro*1.5))
            print(f"+{ouro}G")
            jogador.ouro += ouro
            efeito.podeAgir = 0