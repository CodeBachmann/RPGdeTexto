import random
print("CLASSES!!!!!!")
print("DUELISTA(D) \nATAQUE : 03\nDEFESA : 01\nVIDA : 08")
print("GUERREIRO(G) \nATAQUE = 02\n DEFESA = 01\n VIDA = 10")
print("REISCH(R) \nATAQUE = 03\n DEFESA = 01\n VIDA = 7")
passar = False
encerrarCombate = False
#METODOS PARA MOSTRAR STATUS DE MONSTRO E JOGADOR
def statusMonstro():
    print(f"STATUS DO MONSTRO\nVida : {vidaM}\nAtaque : {ataqueM}\nDefesa : {defesaM}")
    return "\b"


def statusJogador():
    print(f"STATUS DO JOGADOR\nVida : {vida}\nAtaque : {ataque}\nDefesa : {defesa}")
    return "\b"

def mostrarHabilidades(x):
    for habilidade in x:
        print(habilidade)

def escolherHabilidades(x):
    if x == "MR":
        vida -= 2
        print("Você se multila e perde 2 pontos de vida")
        cura = random.randint(1,(inteligencia*2))
        print(f"Você se cura {cura} pontos de vida")
        if vida > vidaMax:
            vida = vidaMax

habilidades = []
#ESCOLHA DE CLASSE
while passar == False:
    decisaoClasse = input("Digite a letra inicial da sua classe : ")
    if decisaoClasse == "G":
        ataque = 2
        defesa = 2
        vida = 10
        vidaMax = 10
        mana = 4
        inteligencia = 1
        critico = 6
        passar = True
        habilidades.append("")
    elif decisaoClasse == "D":
        ataque = 3
        defesa = 1
        vida = 8
        vidaMax = 8
        mana = 6
        inteligencia = 2
        critico = 8
        passar = True
    if decisaoClasse == "R":
        ataque = 3
        defesa = 1
        vida = 7
        vidaMax = 7
        mana = 9
        critico = 3
        inteligencia = 2
        passar = True
        habilidades.append("CRESCIMENTO ACELERADO(PASSIVA)")
        habilidades.append("MULTILAÇÃO REGENERATIVA (MR)")
#ENQUANTO A VIDA DO JOGADOR FOR MAIOR QUE 0 O JOGO VAI CONTINUAR RODANDO
while vida > 0:
    print("O que você deseja: \n(D)DESCANSAR\n(C)CAMINHAR")
    decisao = input("Qual sua escolha: ")
    if decisao == "D":
        descanso = int(input("QUANTOS TURNOS VOCÊ DESEJA DESCANSAR: "))
    #A PARTIR DE UMA INT ALEATORIA É ESCOLHIDO UM MONSTRO PARA BATALHAR
    decisaoMonstro = random.randint(0,1)
    if decisaoMonstro == 0:
        print("UM SLIME APARECE!!!")
        vidaM = 6
        vidaMaxM = 6
        ataqueM = 2
        defesaM = 3

    elif decisaoMonstro == 1:
        print("UM GOBLIN APARECE!!!")
        vidaM = 5
        vidaMaxM = 5
        ataqueM = 3
        defesaM = 2

    #O COMBATE VAI OCORRER ENQUANTO A CONDIÇÃO "encerrarCombate" FOR FALSA
    encerrarCombate = False
    while encerrarCombate == False:
        dano = 0
        if efeitoDefesa == 0:
            defesaMitigada = defesa
        else:
            efeitoDefesa -= 1

        passar = False
        statusMonstro()
        input("PRESSIONE ENTER PARA CONTINUAR!")
        print("AÇÕES :\n(A)ATACAR\n(D)DEFENDER\n(H)HABILIDADES\n(F)FUGIR ")
        while passar == False:
            decisaoCombate = input("ESCOLHA UMA AÇÃO")
            if decisaoCombate == "A":
                dano = (ataque*random.randint(0,ataque))-defesaM
                if random.randint(0,100)<critico:
                    dano *= 2
                    print("DANO CRITICO!!!")
                vidaM -= dano
                passar = True
                print(f"Você inflinge {dano}(-{defesaM}) pontos de dano")

            if decisaoCombate == "D":
                defesa *=2
                efeitoDefesa = 2
                passar = True

            if decisaoCombate == "H":
                mostrarHabilidades(habilidades)
                decisaoHabilidade = input("ESCOLHA UMA HABILIDADE")
                escolherHabilidades(decisaoHabilidade)
                passar = True

            if decisaoCombate == "F":
                encerrarCombate = True
                passar = True

            else:
                print("DECISÃO INVALIDA!!!")

        danoM = (ataqueM + (random.randint(0,ataqueM))) - defesaMitigada
        if vidaM > 0:
            vida -= danoM
            print(f"Você sofreu {danoM}(-{defesaMitigada}) pontos de dano\n")
        else:
            print("O MONSTRO MORREU!")
            encerrarCombate = True



