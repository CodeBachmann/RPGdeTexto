import random
from time import sleep
import Funcoes
import keyboard
import personagens
from time import sleep

loja = personagens.Compraveis

listaNaoCompradosPocoes = ["PA","PD","PI","PV"]

def comprarNaLoja (jogador):
    for i in jogador.habilidades:
        if i in loja.habilidadesComprados:
            loja.habilidadesComprados.remove(i)
    for i in jogador.artefatos:
        if i in loja.artefatosComprados:
            loja.artefatosComprados.remove(i)
    fecharLoja = False
    itemLojaPocao = random.choice(listaNaoCompradosPocoes)
    itemLojaArtefato = random.choice(loja.artefatosComprados)
    itemLojaHabilidade = random.choice(loja.habilidadesComprados)
    pocaoComprado = False
    artefatoComprado = False
    habilidadeComprado = False

    while not fecharLoja:
        compraRealizada = False
        print("Você adentra a loja... ")
        sleep(1)
        print("Sair da loja - (5)")
        if itemLojaPocao == "PA":
            podeComprarPocao = "PA"
            precoPocao = 60
            print("Pocao de Ataque - 60g(1)\nIncreases your attack plus 2")

        elif itemLojaPocao == "PD":
            podeComprarPocao = "PD"
            precoPocao = 45
            print("Pocao de Defesa - 45g(1)\nIncreases your defense plus 11")

        elif itemLojaPocao == "PI":
            podeComprarPocao = "PI"
            precoPocao = 50
            print("Pocao de Inteligencia - 40g(1)\nIncreases your intelligence plus 2")
            
        elif itemLojaPocao == "PV":
            podeComprarPocao = "PV" 
            precoPocao = 55
            print("Pocao de Vida - 55g(1)\nIncreases your max health plus six")

        if itemLojaArtefato == "ALB":
            podeComprarArtefato = "ALB"
            precoArtefato = 95
            print(f"Lagrima do Berserker - {precoArtefato}g(2)\nEvery turn increases your damage")

        elif itemLojaArtefato == "AGG":
            podeComprarArtefato = "AGG"
            precoArtefato = 40
            print(f"Golpe Ganancioso - {precoArtefato}g(2)\nAll the over damage you do is converted in gold")

        elif itemLojaArtefato == "AIX":
            podeComprarArtefato = "AIX"
            precoArtefato = 65
            print(f"Xaoc Idol - {precoArtefato}g(2)\nAt the end of every combat you recover some health")
        
        elif itemLojaArtefato == "APP":
            podeComprarArtefato = "APP"
            precoArtefato = 70
            print(f"Pikeman Patience - {precoArtefato}g(2)\nEvery 3 turns increases your damage")
        
        elif itemLojaArtefato == "AHSS":
            podeComprarArtefato = "AHSS"
            precoArtefato = 75
            print(f"Hard Snake Skin - {precoArtefato}g(2)\nMitigate some flat damage")
        
        elif itemLojaArtefato == "AIE":
            podeComprarArtefato = "AIE"
            precoArtefato = 75
            print(f"Ifrith Eyes - {precoArtefato}g(2)\nIncreases your critical chance")

        if itemLojaHabilidade == "HCL":
            podeComprarHabilidade = "HCL"
            precoHabilidade = 70
            print(f"Pergaminho de Habilidade Cura Leve - {precoHabilidade}g(3)\nHeal based on your intelligence (extra action)")

        elif itemLojaHabilidade == "HPA":
            podeComprarHabilidade = "HPA"
            precoHabilidade = 75
            print(f"Pancada Atordoante - {precoHabilidade}g(3)\nTry to stun your opponent and do some damage (extra action)")

        elif itemLojaHabilidade == "HEO":
            podeComprarHabilidade = "HEO"
            precoHabilidade = 65
            print(f"Enfraquecer Oponente - {precoHabilidade}g(3)\nHalf the opponent Attack (extra action)")
        
        elif itemLojaHabilidade == "HFD":
            podeComprarHabilidade = "HFD"
            precoHabilidade = 70
            print(f'Desespero Frenetico - {precoHabilidade}g(3)\nUse all your mana to unleash a final blow')
        print("Recuperar 1/3 HP MAX - 25g(4)")
        while not compraRealizada:
            print(f"Saldo atual: {jogador.ouro}")
            
            
            if keyboard.read_key() == "4":
                if jogador.ouro >= 25:
                    jogador.ouro -= 25
                    jogador.vida += int(jogador.vidaMax/3)
                    Funcoes.vidaLimite(jogador)
                    print(f"+{int(jogador.vidaMax/3)}HP")
                else:
                    print("Ouro insuficiente!!!")

            if not pocaoComprado:
                if keyboard.read_key() == "1":
                     if precoPocao <= jogador.ouro:
                        if podeComprarPocao == "PA":
                            jogador.ataque += 2
                        elif podeComprarPocao == "PD":
                            jogador.defesa += 11
                        elif podeComprarPocao == "PI":
                            jogador.inteligencia += 2
                        elif podeComprarPocao == "PV":
                            jogador.vidaMax += 6
                            jogador.vida += 6
                        jogador.ouro -= precoPocao
                        pocaoComprado = True
                        print("Item comprado com sucesso")
                else:
                    print("Você não tem ouro o suficiente")

            if not artefatoComprado:
                if precoArtefato <= jogador.ouro:
                    if keyboard.read_key() == "2":
                        jogador.artefatos.append(podeComprarArtefato)
                        jogador.ouro -= precoArtefato
                        artefatoComprado = True
                        loja.artefatosComprados.remove(podeComprarArtefato)
                        print("Item comprado com sucesso")
                else:
                    print("Você não tem ouro o suficiente")

            if not habilidadeComprado:
                if keyboard.read_key() == "3":
                    if precoHabilidade <= jogador.ouro:
                        jogador.habilidades.append(podeComprarHabilidade)
                        jogador.ouro -= precoHabilidade
                        habilidadeComprado = True
                        loja.habilidadesComprados.remove(podeComprarHabilidade)
                        print("Item comprado com sucesso")

            if keyboard.read_key() == "5":
                compraRealizada = True
                fecharLoja = True
                print("Você sai da loja")
            else:
                print("Decisao Invalida!!!")