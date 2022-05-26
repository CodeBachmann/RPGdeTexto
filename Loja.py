import random
import Funcoes
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
            precoArtefato = 95
            print(f"Lagrima do Berserker 95g(ALB)")
        elif itemLojaArtefato <= 100:
            podeComprarArtefato = "AGG"
            precoArtefato = 90
            print(f"Golpe Ganancioso 90g(AGG)")
        if itemLojaMagia <= 70:
            podeComprarHabilidade = "HCL"
            precoMagia = 70
            print(f"Pergaminho de magia Cura Leve (HCL) 70g")
        print("Recuperar 1/3 HP MAX - 25g(RV)")
        while not compraRealizada:
            print(f"Saldo atual: {jogador.ouro}")
            decisao = input("O que você deseja comprar: ")
            if decisao == "RV" and jogador.ouro >= 25:
                jogador.ouro -= 25
                jogador.vida += int(jogador.vida/3)
                jogador.vidaLimite(jogador)
                print(f"+{int(jogador.vida/3)}HP")

            elif decisao == podeComprarPocao and not pocaoComprado:
                if precoPocao <= jogador.ouro:
                    if decisao == "PA":
                        jogador.ataque += 2
                        jogador.ouro -= precoPocao
                        pocaoComprado = True
                        print("Item comprado com sucesso")
                    elif decisao == "PD":
                        jogador.defesa += 10
                        jogador.ouro -= precoPocao
                        pocaoComprado = True
                        print("Item comprado com sucesso")
                    elif decisao == "PI":
                        jogador.inteligencia += 2
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