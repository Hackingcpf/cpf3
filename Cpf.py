#!/usr/bin/python3
import time
import os
senha = input("qual a senha: ")
if senha < "67":
    print("acesso não liberado")
    exit()
elif senha == "68":
    print("acesso liberado")
    time.sleep(3)
    os.system("clear")
else:
    print("bem vindo a puxar dados")
print("loading")
time.sleep(2)
print("▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒")
print("▒▒█▒▒▒▄██████████▄▒▒▒▒")
print("▒█▐▒▒▒████████████▒▒▒▒")
print("▒▌▐▒▒██▄▀██████▀▄██▒▒▒")
print("▐┼▐▒▒██▄▄▄▄██▄▄▄▄██▒▒▒")
print("▐┼▐▒▒██████████████▒▒▒")
print("▐▄▐████─▀▐▐▀█─█─▌▐██▄▒")
print("▒▒█████──────────▐███▌")
print("▒▒█▀▀██▄█─▄───▐─▄███▀▒")
print("▒▒█▒▒███████▄██████▒▒▒")
print("▒▒▒▒▒██████████████▒▒▒")
print("▒▒▒▒▒█████████▐▌██▌▒▒▒")
print("▒▒▒▒▒▐▀▐▒▌▀█▀▒▐▒█▒▒▒▒▒")
print("▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▌▒▒▒▒▒")

print("1: CPF")
escolha = False

while escolha == False:
    nível = int(input("Qual opção: "))
    if (nível == 1):
      os.sistem("apt update")
    
       
    
    
