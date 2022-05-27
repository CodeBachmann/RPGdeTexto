import random
import Funcoes
from time import sleep

def multilacaoRegenerativa (jogador, monstro):
    print("Voce se multila com as unhas e oferece seu sangue a xaoc")
    jogador.mana -= 4
    dano = random.randint(1,int(jogador.inteligencia/3))
    jogador.vida -= dano
    print(f"-{dano} HP | -4 MP")
    sleep(0.5)
    if jogador.vida <= 0:
        input("Você morreu... !:")
    else:
        jogador.dano = int(jogador.inteligencia/2)+(random.randint(1,int(jogador.inteligencia/2)))+jogador.ataque
        Funcoes.calculaDano(jogador, monstro)
        jogador.vida += int(jogador.danoReal/1.4)
        monstro.vida -= jogador.danoReal
        print(f"você inflinge {jogador.danoReal} pontos de dano")
        sleep(0.5)
        print(f"Você se cura {int(jogador.danoReal/2)} pontos de vida")
        sleep(0.5)
        Funcoes.vidaLimite(jogador)
        print(f"Vida atual: {jogador.vida}")
        sleep(0.5)
        jogador.passar = True
        jogador.dano = 0

def rapDeAcademia (jogador, efeito):
    jogador.mana -= 2
    aumentarDano = jogador.ataque + int(jogador.defesa/7)
    jogador.danoAumentado = aumentarDano
    efeito.danoAumentado = 1
    print(f"-2 MP | +{aumentarDano} dano no proximo ataque")
    sleep(0.5)
    efeito.monstroAgir = 1
    efeito.podeAgir = 5
    jogador.passar = True

def organizarAMente (jogador):
    jogador.mana -= 2
    jogador.vida += int(jogador.inteligencia/2)
    input("-2 MP | Você organiza sua mente, sua resiliencia aumenta e seu proximo golpe será critico ")
    sleep(0.5)
    jogador.criticoGarantido = True
    jogador.passar = True

def curaLeve (jogador):
    jogador.mana -= 4
    cura = 2+jogador.inteligencia+random.randint(1, int(jogador.inteligencia/1.1))
    jogador.vida += cura
    print(f" +{cura}HP \n")
    sleep(0.5)
    if jogador.acaoBonus == True:
        jogador.acaoBonus = False
        print("Você usou sua ação Bonus")
    else:
        jogador.passar = True
    
def pancadaAtordoante (jogador, monstro):
    jogador.mana -= 3
    sorte = random.randint(0,100)
    if sorte > 49:
        monstro.podeAgir = False
        print(f"O MONSTRO É ATORDOADO!!!")
    jogador.dano = (int(jogador.ataque*0.8) + (random.randint(0, int(jogador.ataque*0.5))))
    Funcoes.calculaDano(jogador, monstro)
    print(f"VOCÊ INFLINGE: {jogador.danoReal}")
    monstro.vida -= jogador.danoReal