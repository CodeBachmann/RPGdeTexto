import random
from re import S

def vidaLimite (jogador):
    if jogador.vida > jogador.vidaMax:
        jogador.vida = jogador.vidaMax
        

def calculaDano(jogador, danoMitigadoMonstro, passivaCabeloColorido, danoAumentado, criticoGarantido):

    dano = jogador.ataque + random.randint(1, jogador.ataque)
    
    if random.randint(0, 100) < jogador.critico or criticoGarantido == True:
        dano *= 2
        print("DANO CRITICO!!!")
        foiCritico = True
    if passivaCabeloColorido == True and foiCritico == True:
        dano += danoMitigadoMonstro
    dano += danoAumentado
    dano -= danoMitigadoMonstro
    jogador.vida -= dano

    print(f"Você inflinge {dano}(-{danoMitigadoMonstro}) pontos de dano")
    

def status(jogador):
    print(f"STATUS {jogador.nome} \nVida : {jogador.vida}\nAtaque : {jogador.ataque}\nDefesa : {jogador.defesa}\n")
    return "\b"

def continuar():
    input("PRESSIONE ENTER PARA CONTINUAR")

def danoMitigado (defesa):
    danoMitigado = defesa
    return danoMitigado
#Magias
def magiaMultilacaoRegenerativa (jogador):
    dano = random.randint(0,2)
    jogador.vida -= dano
    print(f"Você perdeu {dano} pontos de vida")
    if jogador.vida <= 0:
        input("Você morreu... !:")
    else:
        cura = random.randint(1, (jogador.inteligencia * 2))
        jogador.vida += cura
        print(f"Você se cura {cura} pontos de vida")
        jogador.vida = vidaLimite(jogador.vida,jogador.vidaMax)
        print(f"Vida atual: {jogador.vida}")
        
#Loja
def comprarNaLoja (jogador):
    fecharLoja = False
    itemLojaPocao = random.randint(0,99)
    itemLojaArtefato = random.randint(0,99)
    itemLojaMagia = random.randint(0,99)
    
    while not fecharLoja:
        compraRealizada = False
        input("Você adentra a loja.. !:")
        print("Sair da loja(S)")
        if itemLojaPocao < 34:
            print("Pocao de Ataque - 50g(PA)")
            podeComprarPocao = "PA"
            precoPocao = 50
        elif itemLojaPocao < 67:
            print("Pocao de Defesa - 50g(PD)")
            podeComprarPocao = "PD"
            precoPocao = 50
        elif itemLojaPocao < 100:
            podeComprarPocao = "PI"
            precoPocao = 50
            print("Pocao de Inteligencia - 50g(PI)")
        if itemLojaArtefato < 50:
            podeComprarArtefato = "ALG"
            precoArtefato = 120
            print(f"Lagrima do Berserker 120g(ALB)")
        elif itemLojaArtefato < 100:
            podeComprarArtefato = "AGG"
            precoArtefato = 132
            print(f"Golpe Ganancioso 132g(AGG)")
        if itemLojaMagia < 100:
            podeComprarMagia = "MCL"
            precoMagia = 100
            print(f"Pergaminho de magia Cura Leve (MCL) 100g")
        while not compraRealizada:
            print(f"Saldo atual: {jogador.ouro}")
            decisao = input("O que você deseja comprar: ")
            if decisao == podeComprarPocao:
                if precoPocao <= jogador.ouro:
                    if decisao == "PA":
                        jogador.ataque += 1
                        jogador.ouro -= precoPocao
                        print("Item comprado com sucesso")
                    elif decisao == "PD":
                        jogador.defesa += 1
                        jogador.ouro -= precoPocao
                        print("Item comprado com sucesso")
                    elif decisao == "PI":
                        jogador.inteligencia += 1
                        jogador.ouro -= precoPocao
                        print("Item comprado com sucesso")
                else:
                    print("Você não tem ouro o suficiente")
            elif decisao == podeComprarArtefato:
                if decisao == "ALB":
                    if precoArtefato <= jogador.ouro:
                        jogador.artefato = podeComprarArtefato
                        jogador.ouro -= precoArtefato
                        print("Item comprado com sucesso")
                elif decisao == "AGG":
                    if precoArtefato <= jogador.ouro:
                        jogador.artefato = podeComprarArtefato
                        jogador.ouro -= precoArtefato
                        print("Item comprado com sucesso")
            elif decisao == podeComprarMagia:
                if decisao == "MCL":
                    if precoMagia <= jogador.ouro:
                        jogador.magia = podeComprarMagia
                        jogador.ouro -= precoArtefato
                        print("Item comprado com sucesso")
            elif decisao == "S":
                compraRealizada = True
                fecharLoja = True
                print("Você sai da loja")
