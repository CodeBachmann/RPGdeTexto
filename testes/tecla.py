import time
import keyboard # pip3 install keyboard
import os


os.system('cls') or None

# PRINT ra


vida = 3
vidaM = 30

while vida > 0:  
  time.sleep(0.3) 
  os.system('cls') or None
  print("(A)ataque: 3 dano   --  (R)recuperar: 2 vida\n")  
  print(f"vida:{vida} - monstro:{vidaM}")  
  while True:
      if keyboard.read_key() == "A":
          print("ATAQUE")
          vidaM -= 3
          break
      if keyboard.read_key() == "R":
          print("RECUPERAR")   
          vida += 2  
          break
      vida -= 1
  
        

        

                    