import random
from re import S

def vidaLimite (jogador):
    if jogador.vida > jogador.vidaMax:
        jogador.vida = jogador.vidaMax

def manaLimite (jogador):
    if jogador.mana > jogador.manaMax:
        jogador.mana = jogador.manaMax

def adicionarHabilidade (jogador):
    habilidade = []
    if "HRDA" in jogador.habilidades:
        habilidade.append("(HRDA[2]) Rap de Academia -> Aumenta o dano do proximo ataque, se o inimigo sobreviver o jogador e atordoado ")
    if "HMR" in jogador.habilidades:
        habilidade.append("(HMR[5]) Multilação Regenerativa -> Perde até 2 de vida, causa dano baseado em INT + ATT, o dano causado é convertido em vida")
    if "HOAM" in jogador.habilidades:
        habilidade.append("(HOAM[2]) Organizar a Mente -> Recupera um pouco de vida, o proximo ataque será Critico")
    for elemento in habilidade:
        if elemento not in jogador.habilidadesDesc:
            jogador.habilidadesDesc.append(elemento)
            
def atacar(jogador, monstro):

    dano = jogador.ataque + random.randint(1, int(jogador.ataque/2))
    mitiga = (monstro.defesa/100)+1
    vidaReal = int(monstro.vidaMax*mitiga)
    danoReal = int((dano*monstro.vidaMax)/vidaReal)

    if random.randint(0, 100) < jogador.critico or jogador.criticoGarantido == True:
        dano *= 2
        print("DANO CRITICO!!!")
        jogador.foiCritico = True
    if "ACC" in jogador.artefatos and jogador.foiCritico == True:
        danoReal += int(dano - danoReal)
        jogador.vida += int(dano/4)
        print("Você penetra a armadura do oponente e rouba sua vitalidade ")
    dano += jogador.danoAumentado
   
    monstro.vida -= danoReal
    vidaLimite(jogador)
    jogador.danoAumentado = 0
    jogador.criticoGarantido = False
    jogador.foiCritico = False
    jogador.passar = True
    print(f"Você inflinge ({danoReal})-({dano-danoReal}) pontos de dano")


def status(jogador):
    print(f"STATUS {jogador.nome} \nVida : {jogador.vida}\nAtaque : {jogador.ataque}\nDefesa : {jogador.defesa}\n")
    return "\b"
def statusMonstro(monstro):
    print(f"STATUS {monstro.nome} \nVida : {monstro.vida}\nAtaque : {monstro.ataque}\nDefesa : {monstro.defesa}\n")
    return "\b"
def continuar():
    input("PRESSIONE ENTER PARA CONTINUAR")

#Loja
def comprarNaLoja (jogador):
    fecharLoja = False
    itemLojaPocao = random.randint(0,100)
    itemLojaArtefato = random.randint(0,100)
    itemLojaMagia = random.randint(0,100)
    pocaoComprado = False
    artefatoComprado = False
    habilidadeComprado = False

    while not fecharLoja:
        compraRealizada = False
        input("Você adentra a loja.. !:")
        print("Sair da loja(S)")
        if itemLojaPocao <= 34:
            print("Pocao de Ataque - 50g(PA)")
            podeComprarPocao = "PA"
            precoPocao = 50
        elif itemLojaPocao <= 67:
            print("Pocao de Defesa - 50g(PD)")
            podeComprarPocao = "PD"
            precoPocao = 50
        elif itemLojaPocao <= 100:
            podeComprarPocao = "PI"
            precoPocao = 50
            print("Pocao de Inteligencia - 50g(PI)")
        if itemLojaArtefato <= 50:
            podeComprarArtefato = "ALG"
            precoArtefato = 120
            print(f"Lagrima do Berserker 120g(ALB)")
        elif itemLojaArtefato <= 100:
            podeComprarArtefato = "AGG"
            precoArtefato = 132
            print(f"Golpe Ganancioso 132g(AGG)")
        if itemLojaMagia <= 100:
            podeComprarHabilidade = "HCL"
            precoMagia = 100
            print(f"Pergaminho de magia Cura Leve (HCL) 100g")
        print("Recuperar 5 pontos de Vida - 25g(RV)")
        while not compraRealizada:
            print(f"Saldo atual: {jogador.ouro}")
            decisao = input("O que você deseja comprar: ")
            if decisao == "RV" and jogador.ouro >= 25:
                jogador.ouro -= 25
                jogador.vida += 5
                vidaLimite(jogador)

            elif decisao == podeComprarPocao and not pocaoComprado:
                if precoPocao <= jogador.ouro:
                    if decisao == "PA":
                        jogador.ataque += 1
                        jogador.ouro -= precoPocao
                        pocaoComprado = True
                        print("Item comprado com sucesso")
                    elif decisao == "PD":
                        jogador.defesa += 10
                        jogador.ouro -= precoPocao
                        pocaoComprado = True
                        print("Item comprado com sucesso")
                    elif decisao == "PI":
                        jogador.inteligencia += 1
                        jogador.ouro -= precoPocao
                        pocaoComprado = True
                        print("Item comprado com sucesso")
                else:
                    print("Você não tem ouro o suficiente")

            elif decisao == podeComprarArtefato and not artefatoComprado:
                if decisao == "ALB":
                    if precoArtefato <= jogador.ouro:
                        jogador.artefatos.append(podeComprarArtefato)
                        jogador.ouro -= precoArtefato
                        artefatoComprado = True
                        print("Item comprado com sucesso")
                elif decisao == "AGG":
                    if precoArtefato <= jogador.ouro:
                        jogador.artefatos.append(podeComprarArtefato)
                        jogador.ouro -= precoArtefato
                        artefatoComprado = True
                        print("Item comprado com sucesso")

            elif decisao == podeComprarHabilidade and not habilidadeComprado:
                if decisao == "HCL":
                    if precoMagia <= jogador.ouro:
                        jogador.habilidades.append(podeComprarHabilidade)
                        jogador.ouro -= precoArtefato
                        habilidadeComprado = True
                        print("Item comprado com sucesso")
            elif decisao == "S":
                compraRealizada = True
                fecharLoja = True
                print("Você sai da loja")

def todosOsStatus(jogador):
    print(f"Vida: {jogador.vida}")
    print(f"Ataque: {jogador.ataque}")
    print(f"Inteligencia: {jogador.inteligencia}")
    print(f"Mana: {jogador.mana}")
    print(f"Defesa: {jogador.defesa}")
    print(f"Ouro: {jogador.ouro}")
    print(f"Habilidades: {jogador.habilidades}")
    print(f"Artefatos: {jogador.artefatos}")
    print(f"Critico: {jogador.critico}")


def apresentacaoDeClasse(classe, caracteristica):
  print(f"""{classe.classe}, {caracteristica}
  ATAQUE:       {classe.ataque}
  DEFESA:       {classe.defesa}
  VIDA:         {classe.vida}
  INTELIGENCIA: {classe.inteligencia}
  """)