# print('\n\n')

# print(Cor.RED)
# print("Greg")

# print(Cor.BLUE)
# print("Gustavo")

# print('\n')
# print(Cor.RED+" cor1 "+Cor.GREEN+" cor2")

# print('\n\n')


RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

print(f"{BLUE}ola {RED}Gustavo {BLUE}tudo bem com você?")



def Blue(text):
  return(BLUE+text+RESET)

  
def Red(text):
  return(RED+text+RESET)

print(Blue('ola ')+Red('Gustavo ')+Blue('tudo bem com você?'))


# print normal
nome = 'greg'
print("seu nome é +"+nome+", seja bem vindo ")


# da pra usar F antes das aspas para facilitar o uso de váriaveis 
nome = 'greg'
print(f"seu nome é {nome}, seja bem vindo ")


# da pra usar """ 3 aspas para fazer um print com várias linhas 
print("""Greg(G) 
  ATAQUE: 3
  DEFESA: 1
  VIDA: 8
  INTELIGENCIA: 2
""")


# da pra usar os dois 
print(f"""{nome}(G)) 
  ATAQUE: 3
  DEFESA: 1
  VIDA: 8
  INTELIGENCIA: 2
""")