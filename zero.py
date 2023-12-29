import os 

os.system('cls')

print("\n\n  Hello! \nje suppose que vous n'avez pas le necessaire pour utiliser skrypto\n\n")
print("[+] 1. Telecharger automatiquement le necessaire.")
print("[+] 2. quitter\n\n")
n = input("[+} >>>")

if n == "1":
    os.system('pip install PyCryptodome')
    os.system('pip install PyAes')
elif n == "2":
    quit()
else:
    print("[+] cette commende n'est pas reconnue")            