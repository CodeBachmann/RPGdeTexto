import personagens
import random
def monstroEscolhido(efeito, marcadorArea, enfrentarMonstroComum, enfrentarMonstroElite, caminhoChefe):
        decisaoMonstro = random.randint(0,1)
        if marcadorArea == 0:
            if decisaoMonstro == 0 and enfrentarMonstroComum:

                print("UM SLIME APARECE!!!\n")
                monstro = personagens.npc(vida = 22, vidaMax= 22, ataque= 5, defesa= 24,
                    nome="SLIME", critico= 5, ouro= 23, podeAgir = True, dano = 0, danoReal = 0)
                efeito.monstroAgir = 0
                

            elif decisaoMonstro == 1 and enfrentarMonstroComum:
                print("UM GOBLIN APARECE!!!\n")
                monstro = personagens.npc(vida = 17, vidaMax= 17, ataque= 7, defesa= 15,
                    nome="GOBLIN", critico= 7, ouro=23, podeAgir = True, dano = 0, danoReal = 0)
                efeito.monstroAgir = 0
                

            elif decisaoMonstro == 0 and enfrentarMonstroElite:
                print("UM GOLEM BEBE APARECE!!!\n")
                monstro = personagens.npc(vida = 40, vidaMax= 40, ataque= 8, defesa= 41,
                    nome="GOLEM BEBE", critico= 0, ouro= 55, podeAgir = True, dano = 0, danoReal = 0)
                efeito.monstroAgir = 1
                

            elif decisaoMonstro == 1 and enfrentarMonstroElite:
                print("UM CULTISTA XAOC APARECE!!!\n")
                monstro = personagens.npc(vida = 28, vidaMax= 28, ataque= 11, defesa= 15,
                    nome="CULTISTA XAOC", critico= 0, ouro= 55, podeAgir = True, dano = 0, danoReal = 0)
                efeito.monstroAgir = 0
                

            elif caminhoChefe and marcadorArea == 1:
                print("O REI SLIME SE IRRITOU COM SEUS ATOS!!!\n")
                monstro = personagens.npc(vida = 63, vidaMax= 63, ataque= 10, defesa= 34,
                    nome="REI SLIME", critico= 0, ouro= 100, podeAgir = True, dano = 0, danoReal = 0)
                
                marcadorArea = 1
        return monstro