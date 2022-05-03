import random
import Funcoes
import personagens

# input("Quando você ver esse simbolo !: pressione enter para continuar")
# print("CLASSES!!!!!!")
# print("GREG(G) \nATAQUE: 3\nDEFESA: 1\nVIDA: 8\nINTELIGENCIA: 2")
# print("MAICON(M) \nATAQUE: 2\n DEFESA: 2\n VIDA: 10\nINTELIGENCIA: 2")
# print("REISCH(R) \nATAQUE: 3\n DEFESA: 1\n VIDA: 7\nINTELIGENCIA: 3")

#EVENTOS
passar = False
encerrarCombate = False
emboscada = False
podeAtacar = True
criticoGarantido = False
foiCritico = True

#EFEITOS
efeitoDefesa = 0
efeitoDanoAumentado = 0
efeitoPodeAgir = 0
efeitoMonstroPodeAtacar = 0

#STATUS
vidaM = 0
vida = 5
vidaMax = 0
vidaMaxM = 0
danoM = 0
dano = 2
defesa = 0
danoAumentado = 0
experiencia = 0
marcadorArea = 0
estresse = 0

#DECLARO AS PASSIVAS
passivaCabeloColorido = 0
passivaCrescimentoAcelerado = 0
passivaMasoquistaDaAcademia = 0

#ARTEFATOS
#artefatoGolpeGanancioso = 0
#METODOS PARA MOSTRAR STATUS DE MONSTRO E JOGADOR
vida = Funcoes.recebeDano(vida,dano)
print(vida)

def statusMonstro():
    print(f"STATUS DO MONSTRO\nVida : {vidaM}\nAtaque : {ataqueM}\nDefesa : {defesaM}")
    return "\b"

def continuar():
    input("PRESSIONE ENTER PARA CONTINUAR")

habilidades = []
Funcoes.statusJogador()

#ESCOLHA DE CLASSE
while passar == False:
    decisaoClasse = input("Digite a letra inicial da sua classe : ")
    decisaoClasse = decisaoClasse.upper()
    if decisaoClasse == "M":
        print("CLASSE MAICON ESCOLHIDA")
        nome = input("Digite seu nome: ")
        habilidades.append("RAP DE ANIME(RA)")
        habilidades.append("MASOQUISTA DA ACADEMIA (PASSIVA)")
        jogador = personagens.Personagem\
            (vida=10,
             vidaMax= 10,
             ataque=2,
             defesa=2,
             classe="MAICON",
             critico=6,
             nome=nome,
             inteligencia=2,
             mana=4,
             xp=0,
             nivel=1,
             habilidades=habilidades)
        #jogador.habilidades.append("fosgo")

    elif decisaoClasse == "G":
        print("CLASSE GREG ESCOLHIDA")
        ataque = 3
        defesa = 1
        vida = 8
        vidaMax = 8
        mana = 6
        inteligencia = 2
        critico = 8
        nivel = 1
        passar = True
        passivaCabeloColorido = 1
        habilidades.append("ORGANIZAR A MENTE(OM)")
        habilidades.append("CABELO COLORIDO(PASSIVO)")

    if decisaoClasse == "R":
        print("CLASSE REISCH ESCOLHIDA")
        ataque = 3
        defesa = 1
        vida = 7
        vidaMax = 7
        mana = 9
        critico = 3
        nivel = 1
        inteligencia = 3

        passar = True
        passivaCrescimentoAcelerado = 1
        habilidades.append("CRESCIMENTO ACELERADO(PASSIVA)")
        habilidades.append("MULTILAÇÃO REGENERATIVA (MR)")
#ENQUANTO A VIDA DO JOGADOR FOR MAIOR QUE 0 O JOGO VAI CONTINUAR RODANDO
while vida > 0:
    danoMitigado = defesa
    if marcadorArea == 0:
        input("Você adentra a floresta de Cornwood, o sol se torna apenas um borrão entre as árvores... !:")
    print("O que você deseja: \n(D)DESCANSAR\n(C)CAMINHAR")
    decisaoExplorar = input("Qual sua escolha: ")
    decisaoExplorar = decisaoExplorar.upper()
    if decisaoExplorar == "D":
        descanso = int(input("QUANTOS TURNOS VOCÊ DESEJA DESCANSAR: "))
        tempo = 0
        while tempo < descanso and emboscada == False:
            if random.randint(1,5) == 5:
                emboscada = True
            else:
                descansoVida = round(vida/5, 0)
                print(f"você recuperou {descansoVida}pontos de vida")
                vida += descansoVida
                if vida > vidaMax:
                    vida = vidaMax

    #A PARTIR DE UMA INT ALEATORIA É ESCOLHIDO UM MONSTRO PARA BATALHAR
    decisaoMonstro = 2#random.randint(0,2)
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

    elif decisaoMonstro == 2:
        print("UM GOLEM BEBE APARECE!!!")

        vidaM = 7
        vidaMax = 6
        ataqueM = 3
        defesaM = 4
        efeitoPodeAtacarMonstro = 1

    #O COMBATE VAI OCORRER ENQUANTO A CONDIÇÃO "encerrarCombate" FOR FALSA
    encerrarCombate = False
    danoMitigadoM = defesaM

    while encerrarCombate == False:
        passar = False
        #AREA QUE CONTROLA BUFFS QUE DURAM MAIS DE UM TURNO
        if efeitoDefesa == 0:
            danoMitigado = defesa
        else:
            efeitoDefesa -= 1
        if efeitoPodeAgir != 0 and efeitoPodeAgir != 5:
            podeAgir = False
            efeitoPodeAgir -= 1
        elif efeitoPodeAgir == 0:
            podeAgir = True
        elif efeitoPodeAgir ==5:
            podeAgir == True
            efeitoPodeAgir = 1

        if efeitoDanoAumentado == 0:
            danoAumentado = 0
        else:
            efeitoDanoAumentado -= 1
        #ATIVA A EMBOSCADA
        if emboscada == True:
            print("VOCÊ FOI EMBOSCADO!!!")
            danoM = (ataqueM + (random.randint(0, ataqueM))) - danoMitigado
            if danoM < 0:
                danoM = 0
            print(f"Você sofreu {danoM}(-{danoMitigadoM}) pontos de dano\n")
            vida -= danoM
        #MOSTRA OS STATUS ATUAIS DO JOGADOR E DO MONSTRO
        statusMonstro()
        Funcoes.statusJogador()
        continuar()
        #MOSTRA AS DECISOES DE COMBATE PARA O JOGADOR
        if podeAgir == True:
            while passar == False:
                print("AÇÕES :\n(A)ATACAR\n(D)DEFENDER\n(H)HABILIDADES\n(F)FUGIR ")
                decisaoCombate = input("ESCOLHA UMA AÇÃO: ")
                decisaoCombate = decisaoCombate.upper()
                if decisaoCombate == "A":
                    dano = ataque + random.randint(0, ataque)
                    if criticoGarantido == True:
                        dano*=2
                        criticoGarantido = False
                        print("DANO CRITICO!!!")
                        foiCritico = True
                    elif random.randint(0, 100) < critico:
                        dano *= 2
                        print("DANO CRITICO!!!")
                        foiCritico = True
                    if passivaCabeloColorido == 1 and foiCritico == True:
                        dano += danoMitigadoM
                    dano += danoAumentado
                    dano -= danoMitigadoM
                    vidaM -= dano
                    foiCritico = False
                    passar = True
                    print(f"Você inflinge {dano}(-{defesaM}) pontos de dano")

                elif decisaoCombate == "D":
                    danoMitigado = defesa*2
                    efeitoDefesa = 2
                    passar = True
                    print("SUA DEFESA FOI DOBRADA(2t)")
                #HABILIDADES
                elif decisaoCombate == "H":
                    while passar == False:
                        for habilidade in habilidades:
                            print(habilidade)
                        decisaoHabilidade = input("ESCOLHA UMA HABILIDADE")
                        decisaoHabilidade = decisaoHabilidade.upper()
                        if decisaoHabilidade == "MR":
                            vida -= 2
                            print("Você se multila e perde 2 pontos de vida")
                            cura = random.randint(1, (i * 2))
                            print(f"Você se cura {cura} pontos de vida")
                            if vida > vidaMax:
                                vida = vidaMax
                            passar = True
                        elif decisaoHabilidade == "OM":
                            estresse -= inteligencia
                            danoMitigado +=inteligencia/2
                            print("Você organiza sua mente, sua resiliencia aumenta e seus proximo golpe será critico")
                            criticoGarantido = True
                            passar = True

                        elif decisaoHabilidade == "RA":
                            danoAumentado = ataque+defesa
                            efeitoDanoAumentado = 1
                            print("Apos ouvir o RAP DO SAITAMA você sente que tem que dar tudo de si em um golpe final!!!")
                            efeitoPodeAtacarMonstro = 1
                            efeitoPodeAgir = 5
                            passar = True

                elif decisaoCombate == "F":
                    encerrarCombate = True
                    passar = True
                else:
                    print("DECISÃO INVALIDA")
            else:
                pr
        #CALCULA, APLICA E MOSTRA O DANO DO MONSTRO ALEM DE VERIFICAR SE UMA EMBOSCADA JA FOI REALIZADA

        if emboscada == True:
            emboscada = False
        elif vidaM > 0 and efeitoPodeAtacarMonstro == 0:
                danoM = (ataqueM + (random.randint(0, ataqueM))) - danoMitigado
                if danoM < 0:
                    danoM = 0
                print(f"Você sofreu {danoM}(-{danoMitigado}) pontos de dano\n")
                vida -= danoM
        elif efeitoPodeAtacarMonstro > 0:
            efeitoPodeAtacarMonstro -= 1
        if vidaM <=0:
            print("O MONSTRO MORREU!")
            encerrarCombate = True
            continuar()
