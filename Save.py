def salvar (jogador):
    jogador.listaSave = []
    jogador.listaSave.append(jogador.nome)
    jogador.listaSave.append(jogador.vida)
    jogador.listaSave.append(jogador.vidaMax)
    jogador.listaSave.append(jogador.ataque)
    jogador.listaSave.append(jogador.defesa)
    jogador.listaSave.append(jogador.classe)
    jogador.listaSave.append(jogador.critico)
    jogador.listaSave.append(jogador.inteligencia)
    jogador.listaSave.append(jogador.mana)
    jogador.listaSave.append(jogador.manaMax)
    jogador.listaSave.append(jogador.regenMana)
    jogador.listaSave.append(jogador.habilidades)
    jogador.listaSave.append(jogador.ouro)
    jogador.listaSave.append(jogador.caminhado)
    jogador.listaSave.append(jogador.artefatos)

    save = open(r'C:\Users\pcadmin\Documents\GitHub\RPGdeTexto\save.txt','a')
    texto = ''
    for i in jogador.listaSave:
        texto+= str(i)+' '
    save.writelines('\n', texto)
    save.close

def carregar(jogador)
    save = open(r'C:\Users\pcadmin\Documents\GitHub\RPGdeTexto\save.txt','r')
    lista = (save.read).splitlines()
    cont = 0
    contSave = 10
    for i in lista:
        linha = i.split(' ')
        if jogador.nome in linha:
            contSave = cont
        cont+= 1

    jogador.listaSave = lista[contSave]
    jogador.nome = jogador.listaSave[0]
    jogador.vida = jogador.listaSave[1]
    jogador.vidaMax = jogador.listaSave[2]
    jogador.ataque = jogador.listaSave[3]
    jogador.defesa = jogador.listaSave[4]
    jogador.classe = jogador.listaSave[5]
    jogador.critico = jogador.listaSave[6]
    jogador.inteligencia = jogador.listaSave[7]
    jogador.mana = jogador.listaSave[8]
    jogador.manaMax = jogador.listaSave[9]
    jogador.regenMana = jogador.listaSave[10]
    jogador.habilidades = jogador.listaSave[11]
    jogador.ouro = jogador.listaSave[12]
    jogador.caminhado = jogador.listaSave[13]
    jogador.artefatos = jogador.listaSave[14]
    