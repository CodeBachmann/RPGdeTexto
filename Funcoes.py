import random

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
def comprarNaLoja (itemLojaPocao, artefato, magia):
    fecharLoja = False
    itemLojaPocao = random.randint(0,99)
    itemLojaArtefato = random.randint(0,99)
    itemLojaMagia = random.randint(0,99)

    while fecharLoja == False:
        input("Você adentra a loja.. !:")
        if itemLojaPocao < 34:
            print("Pocao de Ataque - 50g(PA)")
            podeComprarPocao = "Ataque"
        elif itemLojaPocao < 67:
            print("Pocao de Defesa - 50g(PD)")
            podeComprarPocao = "Defesa"
        elif itemLojaPocao < 100:
            podeComprarPocao = "Inteligencia"
            print("Pocao de Inteligencia - 50g(PI)")
        if itemLojaArtefato < 50:
            podeComprarArtefato = "Lagrima do Berserker"
        elif itemLojaArtefato < 100:
            podeComprarArtefato = ""