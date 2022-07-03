from ntpath import join
import random
from time import  sleep
import Funcoes
import escolherMonstro
import personagens
import os
import sys
import Artefacts
import Effects
import Skills
import Loja
import keyboard
from Save import *
# --------------------------------- VARIÁVEIS --------------------------------- #

salvado = personagens.salvo
dicSkillsMana = {'HCL' : 5,
        'HRDA' : 3,
        'HMR' : 4,
        'HOAM' : 3,
        'HPA' : 3,
        'HEO' : 2,
        'HFD' : 1,
        'HEP' : 4,
        'HEF' : 4}

#EVENTOS
encerrarCombate = False
emboscada = False
monologo = False

#CAMINHOS
enfrentarMonstroElite = False
caminhoChefe = False
enfrentarMonstroComum = False
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
dddecisao = int(input('1 - Novo Jogo\n2 - Carregar jogo\n'))
# --------------------------------- INÍCIO --------------------------------- #
if dddecisao == 1:
    os.system('cls') or None
    nome = input("Digite seu nome: ")
    os.system('cls') or None
    print("\n ------------CLASSES------------")

    Funcoes.apresentacaoDeClasse(personagens.Santos, 'o bombado(1)')
    Funcoes.apresentacaoDeClasse(personagens.Sabel, 'o somelier de estagio(2)')
    Funcoes.apresentacaoDeClasse(personagens.Reisch, 'o emo feliz(3)')
    quebra = False

    # ----------------------------ESCOLHA DE CLASSE ------------------------------------

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
    # ------------------------------
    print(f"CLASSE {jogador.classe} ESCOLHIDA")
    sleep(2)
    os.system('cls') or None
    jogador.nome = nome
    os.system('cls') or None

if dddecisao == 2:
    jogador = personagens.Reisch
    Salvar.escolherSave(Salvar(),jogador= jogador)
    Salvar.carregar(Salvar(),jogador = jogador, salvado = salvado)



#ENQUANTO A VIDA DO JOGADOR FOR MAIOR QUE 0 O JOGO VAI CONTINUAR RODANDO
while jogador.vida > 0:
    if marcadorArea == 0 and not monologo:
        print("1 - Pular monologo\n2 - Ver monologo\n\n")
        while True:
            if keyboard.read_key() == '2':
                texto = "Você adentra a floresta de Cornwood, o sol se torna apenas um borrão entre as árvores..."
                for c in texto:
                    print(c, end="")
                    sys.stdout.flush()
                    sleep(0.05)
                sleep(1)
                break
            if keyboard.read_key() == '1':
                break
        sleep(1)
        os.system('cls') or None
        monologo = True
    elif marcadorArea == 1 and monologo:
        input("JOGO EM CONSTRUÇÃO!!!")
        exit()
        monologo = False

    print("~~~~~~Caminhos~~~~~~\n")
    caminhoMisterio = False
    caminhoMonstroComum = False
    caminhoMonstroElite = False
    caminhoLoja = False
    jogador.passar = False
    
    while not jogador.passar:
        Salvar.salvar(Salvar(), jogador, salvado)
        jogador.caminhado += 1
        caminhos = random.randint(4,5)
        print(f"Seu saldo: {jogador.ouro}\n\nVocê pode: ")
        cont = 0
        if jogador.caminhado < 12 and jogador.caminhado != 1:
            while cont < caminhos:
                escolha = random.randint(1, 100)
                if escolha > 0 and escolha <= 50:
                    print(f"Lutar com um monstro Comum(1)\n")
                    caminhoMonstroComum = True
                elif escolha > 50 and escolha <= 80:
                    print(f"Lutar com um monstro de Elite(2)\n")
                    caminhoMonstroElite = True
                elif escolha > 80 and escolha <= 100:
                    print(f"Entrar na loja(3)\n")
                    caminhoLoja = True
                cont+= 1
        elif jogador.caminhado == 1:
            print(f"Lutar com um monstro Comum(1)\n")
            caminhoMonstroComum = True
        elif jogador.caminhado == 12:
            print(f"Entrar na loja(3)\n")
            caminhoLoja = True
        else:
            print(f"Você sente uma presença ameaçadora!!!")
            sleep(2)
            os.system('cls') or None
            caminhoChefe = True
            jogador.caminhado = 0
            jogador.passar = True
            break

        while True:
            if caminhoChefe:
                jogador.passar = True
                os.system('cls') or None
                break

            elif keyboard.read_key() == "1" and caminhoMonstroComum:
                enfrentarMonstroComum = True
                jogador.passar = True
                os.system('cls') or None
                break

            elif keyboard.read_key() == "2" and caminhoMonstroElite:
                enfrentarMonstroElite = True
                jogador.passar = True
                os.system('cls') or None
                break

            elif keyboard.read_key() == "3" and caminhoLoja:
                Loja.comprarNaLoja(jogador)
                os.system('cls') or None
                break
                
            else:
                print("Decisao Invalida")
        
        os.system('cls') or None
        

    #A PARTIR DE UMA INT ALEATORIA É ESCOLHIDO UM MONSTRO PARA BATALHAR

    monstro = escolherMonstro.monstroEscolhido(efeito, marcadorArea, enfrentarMonstroComum, enfrentarMonstroElite, caminhoChefe)
    enfrentarMonstroComum = False
    enfrentarMonstroElite = False
    if caminhoChefe:
        caminhoChefe = False
        marcadorArea += 1
        
    #O COMBATE VAI OCORRER ENQUANTO A CONDIÇÃO "encerrarCombate" FOR FALSA
    encerrarCombate = False
    efeito.tempoCombate = 0
    

    while not encerrarCombate:
        jogador.acaoBonus = True
        jogador.passar = False
        efeito.tempoCombate += 1
        Funcoes.manaLimite(jogador)
        Effects.atordoar(jogador, efeito)

        #MOSTRA OS STATUS ATUAIS DO JOGADOR E DO MONSTRO
        
        Funcoes.statusMonstro(monstro)
        Funcoes.status(jogador)
        print("\n")
        sleep(1)
        #MOSTRA AS DECISOES DE COMBATE PARA O JOGADOR
        if jogador.podeAgir:
            jogador.passar = False
            while not jogador.passar:
                
                print("AÇÕES :\n(1)ATACAR\n(2)HABILIDADES\n(3)FUGIR\n(4)PERSONAGEM\n")
                
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

                            if 5 <= efeito.quantidadeHabilidades and keyboard.read_key() == "4":
                                decisaoHabilidade = jogador.habilidades[4]
                                break

                            if 6 <= efeito.quantidadeHabilidades and keyboard.read_key() == "5":
                                decisaoHabilidade = jogador.habilidades[5]
                                break

                            if 7 <= efeito.quantidadeHabilidades and keyboard.read_key() == "6":
                                decisaoHabilidade = jogador.habilidades[6]
                                break

                            if keyboard.read_key() == volta:
                                decisaoHabilidade = "V"
                                break

                        efeito.quantidadeHabilidades = 0
                        jogador.habilidadesDesc = []
                        dicSkills = {'HCL' : Skills.organizarAMente,
                                    'HRDA' : Skills.rapDeAcademia,
                                    'HMR' : Skills.multilacaoRegenerativa,
                                    'HOAM' : Skills.organizarAMente,
                                    'HPA' : Skills.pancadaAtordoante,
                                    'HEO' : Skills.enfraquecerOponente,
                                    'HFD' : Skills.freneticDespair,
                                    'HEP' : Skills.enchantPoison,
                                    'HEF' : Skills.enchantFire}
                                    
                        if decisaoHabilidade in jogador.habilidades and jogador.mana >= dicSkillsMana[decisaoHabilidade]:
                            f'{dicSkills[decisaoHabilidade](jogador, monstro, efeito)}'
                            break
                            
                        elif "V":
                            break

                elif keyboard.read_key() == "3":
                    encerrarCombate = True
                    jogador.passar = True

                elif keyboard.read_key() == "4":
                    Funcoes.todosOsStatus(jogador)
                    print("\n")
                else:
                    print("")
            
        jogador.mana += jogador.regenMana
        print(f"+{jogador.regenMana} MP")
        sleep(1)

        if monstro.vida > 0 and efeito.monstroAgir == 0:
            Funcoes.monstroAtacar(jogador, monstro, efeito)
            print("\n") 

        elif efeito.monstroAgir > 0:
            print("O monstro não age nesse turno!")
            efeito.monstroAgir -= 1
        
        Effects.debuffAtaque(monstro, efeito)


        if jogador.vida <= 0:
            encerrarCombate = True
            print("Você morreu... ")
            Salvar.deletarSave(Salvar(),jogador = jogador, salvado = salvado)
            sleep(2)
            exit(0)

        elif monstro.vida <=0:
            print("O monstro morreu!")
            Artefacts.idoloXaoc(jogador, monstro, efeito)
            encerrarCombate = True
            sleep(1)
            ouro = random.randint(int(monstro.ouro),int(monstro.ouro*1.5))
            print(f"+{ouro}G\n")
            jogador.ouro += ouro
            efeito.podeAgir = 0
            sleep(1)