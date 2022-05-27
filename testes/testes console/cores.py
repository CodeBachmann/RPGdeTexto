# pensei duas formas:
#   funções que retornam o texto pintado 
#   variaveis que tem a cor (essa parece melhor)

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