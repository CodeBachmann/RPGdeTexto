import random
from time import sleep
import Funcoes
import keyboard
from time import sleep
def comprarNaLoja (jogador):
    fecharLoja = False
    itemLojaPocao = random.randint(0,100)
    itemLojaArtefato = random.randint(0,100)
    itemLojaHabilidade = random.randint(0,100)
    pocaoComprado = False
    artefatoComprado = False
    habilidadeComprado = False

    while not fecharLoja:
        compraRealizada = False
        print("Você adentra a loja... ")
        sleep(1)
        print("Sair da loja(5)")
        if itemLojaPocao <= 25:
            print("Pocao de Ataque - 60g(1)")
            podeComprarPocao = "PA"
            precoPocao = 60
        elif itemLojaPocao <= 50:
            print("Pocao de Defesa - 45g(1)")
            podeComprarPocao = "PD"
            precoPocao = 45
        elif itemLojaPocao <= 75:
            podeComprarPocao = "PI"
            precoPocao = 50
            print("Pocao de Inteligencia - 40g(1)")
        elif itemLojaPocao <= 100:
            podeComprarPocao = "PV" 
            precoPocao = 55
            print("Pocao de Vida - 55g(1)")
        if itemLojaArtefato <= 50:
            podeComprarArtefato = "ALB"
            precoArtefato = 95
            print(f"Lagrima do Berserker 95g(2)")
        elif itemLojaArtefato <= 100:
            podeComprarArtefato = "AGG"
            precoArtefato = 40
            print(f"Golpe Ganancioso 40g(2)")
        if itemLojaHabilidade <= 100:
            podeComprarHabilidade = "HCL"
            precoHabilidade = 70
            print(f"Pergaminho de Habilidade Cura Leve (3) 70g")

        print("Recuperar 1/3 HP MAX - 25g(4)")
        while not compraRealizada:
            print(f"Saldo atual: {jogador.ouro}")
            
            
            if keyboard.read_key() == "4":
                if jogador.ouro >= 25:
                    jogador.ouro -= 25
                    jogador.vida += int(jogador.vida/3)
                    Funcoes.vidaLimite(jogador)
                    print(f"+{int(jogador.vida/3)}HP")
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
                        print("Item comprado com sucesso")
                else:
                    print("Você não tem ouro o suficiente")

            if not habilidadeComprado:
                if keyboard.read_key() == "3":
                    if precoHabilidade <= jogador.ouro:
                        jogador.habilidades.append(podeComprarHabilidade)
                        jogador.ouro -= precoHabilidade
                        habilidadeComprado = True
                        print("Item comprado com sucesso")

            if keyboard.read_key() == "5":
                compraRealizada = True
                fecharLoja = True
                print("Você sai da loja")
            else:
                print("Decisao Invalida!!!")