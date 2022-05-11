import random
from re import S

def vidaLimite (vida, vidaMax):
    if vida > vidaMax:
        vida = vidaMax
        return vida

def calculaDano(vida, ataque, criticoGarantido, critico, foiCritico, passivaCabeloColorido, danoMitigadoMonstro, danoAumentado):

    dano = ataque + random.randint(1, ataque)
    
    if random.randint(0, 100) < critico or criticoGarantido == True:
        dano *= 2
        print("DANO CRITICO!!!")
        foiCritico = True
    if passivaCabeloColorido == True and foiCritico == True:
        dano += danoMitigadoMonstro
    dano += danoAumentado
    dano -= danoMitigadoMonstro
    vida -= dano

    print(f"Você inflinge {dano}(-{danoMitigadoMonstro}) pontos de dano")
    return vida

def status(vida, ataque, defesa, nome):
    print(f"STATUS {nome} \nVida : {vida}\nAtaque : {ataque}\nDefesa : {defesa}")
    return "\b"

def continuar():
    input("PRESSIONE ENTER PARA CONTINUAR")

def danoMitigado (defesa):
    danoMitigado = defesa
    return danoMitigado
#Magias
def magiaMultilacaoRegenerativa (vida, vidaMax, inteligencia):
    dano = random.randint(0,3)
    vida -= dano
    print(f"Você perdeu {dano} pontos de vida")
    if vida <= 0:
        input("Você morreu... !:")
        return vida
    else:
        print("Você se multila e perde 2 pontos de vida")
        cura = random.randint(1, (inteligencia * 2))
        print(f"Você se cura {cura} pontos de vida")
        vida = vidaLimite(vida,vidaMax)
        print(f"Vida atual: {vida}")
        return vida
#Loja
def comprarNaLoja (self, ouro, ataque, defesa, inteligencia, artefato, magia):
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
            print(f"Saldo atual: {self.ouro}")
            decisao = input("O que você deseja comprar: ")
            if decisao == podeComprarPocao:
                if precoPocao <= ouro:
                    if decisao == "PA":
                        self.ataque += 1
                        self.ouro -= precoPocao
                        print("Item comprado com sucesso")
                    elif decisao == "PD":
                        self.defesa += 1
                        self.ouro -= precoPocao
                        print("Item comprado com sucesso")
                    elif decisao == "PI":
                        self.inteligencia += 1
                        self.ouro -= precoPocao
                        print("Item comprado com sucesso")
                else:
                    print("Você não tem ouro o suficiente")
            elif decisao == podeComprarArtefato:
                if decisao == "ALB":
                    if precoArtefato <= ouro:
                        self.artefato = podeComprarArtefato
                        self.ouro -= precoArtefato
                        print("Item comprado com sucesso")
                elif decisao == "AGG":
                    if precoArtefato <= ouro:
                        self.artefato = podeComprarArtefato
                        self.ouro -= precoArtefato
                        print("Item comprado com sucesso")
            elif decisao == podeComprarMagia:
                if decisao == "MCL":
                    if precoMagia <= ouro:
                        self.magia = podeComprarMagia
                        self.ouro -= precoArtefato
                        print("Item comprado com sucesso")
            elif decisao == "S":
                compraRealizada = True
                fecharLoja = True
                print("Você sai da loja")
