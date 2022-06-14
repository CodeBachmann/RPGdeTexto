def salvar (jogador, salvado):
    salvado.listaSave = []
    salvado.listaSave.append(jogador.nome)
    salvado.listaSave.append(jogador.vida)
    salvado.listaSave.append(jogador.vidaMax)
    salvado.listaSave.append(jogador.ataque)
    salvado.listaSave.append(jogador.defesa)
    salvado.listaSave.append(jogador.classe)
    salvado.listaSave.append(jogador.critico)
    salvado.listaSave.append(jogador.inteligencia)
    salvado.listaSave.append(jogador.mana)
    salvado.listaSave.append(jogador.manaMax)
    salvado.listaSave.append(jogador.regenMana)
    salvado.listaSave.append(jogador.habilidades)
    salvado.listaSave.append(jogador.ouro)
    salvado.listaSave.append(jogador.caminhado)
    salvado.listaSave.append(jogador.artefatos)

    save = open(r'C:\Users\Aluno\Documents\GitHub\RPGdeTexto\save.txt','w+')
    lista = save.read().splitlines()
    
    cont = 0
    for i in lista:
        linha = i.split(' ')
        if jogador.nome in linha:
            salvado.contSave = cont
        cont+= 1
    if salvado.contSave != 50:
        texto2 = ''
        for i in salvado.listaSave:
            texto2 += (str(i)+' ')
        lista[salvado.contSave] = texto2
    else:
        lista.append(salvado.listaSave)
    textoNovo = ''
    for i in lista:
        textoNovo += (str(i)+"\n")
    save.write(textoNovo)
    save.close()


def carregar(jogador, salvado):
    save = open(r'C:\Users\Aluno\Documents\GitHub\RPGdeTexto\save.txt','r')
    lista = save.read().splitlines()
    
    save.close()
    cont = 0
    for i in lista:
        linha = i.split(' ')
        if jogador.nome in linha:
            salvado.contSave = cont
        cont+= 1
    
    texto2 = linha[salvado.contSave]
    lista2 = texto2.split(' ')

    lista2 = texto2
    jogador.nome = lista2[0]
    jogador.vida = int(lista2[1])
    jogador.vidaMax = int(lista2[2])
    jogador.ataque = int(lista2[3])
    jogador.defesa = int(lista2[4])
    jogador.classe = lista2[5]
    jogador.critico = int(lista2[6])
    jogador.inteligencia = int(lista2[7])
    jogador.mana = int(lista2[8])
    jogador.manaMax = int(lista2[9])
    jogador.regenMana = int(lista2[10])
    jogador.habilidades = lista2[11]
    jogador.ouro = int(lista2[12])
    jogador.caminhado = int(lista2[13])
    jogador.artefatos = lista2[14]
    