# import personagens
# maicon = personagens.Personagem(5,4,7)
# print(maicon.vida)
import  personagens
habilidades = []
habilidades.append("RAP DE ANIME(RA)")
habilidades.append("MASOQUISTA DA ACADEMIA (PASSIVA)")
jogador = personagens.Personagem\
            (vida=10,
             vidaMax= 10,
             ataque=2,
             defesa=2,
             classe="MAICON",
             critico=6,
             inteligencia=2,
             mana=4,
             xp=0,
             nivel = 1,
             habilidades=habilidades)
jogador.habilidades.append("fosgo")

