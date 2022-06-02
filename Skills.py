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
    jogador.mana -= 3
    aumentarDano = jogador.ataque + int(jogador.defesa/7)
    jogador.danoAumentado = aumentarDano
    efeito.danoAumentado = 1
    print(f"-3 MP | +{aumentarDano} dano no proximo ataque")
    sleep(0.5)
    if jogador.acaoBonus == True:
        jogador.acaoBonus = False
        print("Você usou sua ação Bonus")
    else:
        jogador.passar = True

def organizarAMente (jogador):
    jogador.mana -= 3
    cura = int(jogador.inteligencia/2)
    jogador.vida += cura
    print(F"-3 MP | +{cura} HP | Você organiza sua mente, sua resiliencia aumenta e seu proximo golpe será critico ")
    sleep(0.5)
    jogador.criticoGarantido = True
    jogador.passar = True

def curaLeve (jogador):
    jogador.mana -= 5
    cura = 3+int(jogador.inteligencia*0.7)+random.randint(1, int(jogador.inteligencia*0.5))
    jogador.vida += cura
    print(f"+{cura} HP | -4 MP | Você sente sua energia ser drenada, mas seu corpo se recupera\n")
    sleep(0.5)
    if jogador.acaoBonus == True:
        jogador.acaoBonus = False
        print("Você usou sua ação Bonus")
    else:
        jogador.passar = True
    
def pancadaAtordoante (jogador, monstro, efeito):
    jogador.mana -= 3
    print("-3 MP |")
    sorte = random.randint(0,100)
    if sorte > 49:
        efeito.monstroAgir = 1
        print(f"O MONSTRO É ATORDOADO!!!")
    jogador.dano = (int(jogador.ataque*0.8) + (random.randint(0, int(jogador.ataque*0.5))))
    Funcoes.calculaDano(jogador, monstro)
    print(f"VOCÊ INFLINGE: {jogador.danoReal}")
    monstro.vida -= jogador.danoReal
    jogador.passar = True

def enfraquecerOponente (jogador, monstro, efeito):
    jogador.mana -= 2
    print(f"-3 MP | DANO MONSTRO -50%")
    sleep(0.5)
    efeito.ataque = int(monstro.ataque/2)
    if jogador.acaoBonus == True:
        jogador.acaoBonus = False
        print("Você usou sua ação Bonus")
    else:
        jogador.passar = True