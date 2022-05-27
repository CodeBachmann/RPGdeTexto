import os
import time

os.system('cls') or None


for a in range(17):
  time.sleep(0.01) 
  os.system('cls') or None
  b = 16-a
  print(f"  O                   O   ")
  print(f" /|\{a*' '}-{b*' '  }/|\  ")
  print(f" / \                 / \  ")

