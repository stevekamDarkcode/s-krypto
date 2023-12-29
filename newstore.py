import getpass
from os import  path as ospath, remove as osremove, stat as osstat
import os 

try: import pyAesCrypt
except ImportError as es: exit(str(es))

os.system("cls")

# encryption / Decryption buffer size - 64K
bufferSize = 64 * 1024


def tiger_start():
    os.system('color 0A')
    print("...........  ............. ............. ....               .... .............")
    print("...........  ............. .............  ....             ....  .............")
    print("....              ....     ....            ....           ....   ....         ")
    print("....              ....     ....             ....         ....    ....         ")
    print("...........       ....     .............     ....       ....     .............")
    print("...........       ....     .............      ....     ....      .............")
    print("        ...       ....     ....                ....   ....       ....         ")
    print("        ...       ....     ....                 .... ....        ....         ")
    print("...........       ....     .............         .......         .............")
    print("...........       ....     .............          .....          .............")
    print("")
    print("\n[=][=][=][=][=][=][=][=][=][=][=][=][=][=][=][=][=][=]")
    print("------------------------------------------------------")
    print("[=]     Bienvvenue sur stevesoft le programe""       [=]")
    print("[=]          qui protege vos fichier""               [=]")
    print("[=]    ecrit part steve kambea the darkwebmaker""    [=]")
    print("------------------------------------------------------")
    print("[=][=][=][=][=][=][=][=][=][=][=][=][=][=][=][=][=][=]\n")


def tiger_end():

    print("\n[+] -----------------------------------------------------------------------------")
    print("[+] Merci d'avoir utiliser stevesoft...................")
    print("[+] Si  mon programme t'a plue tu peux me contacter ndjeumous@gamil.com")
    print("[+] -----------------------------------------------------------------------------\n")
    


def encrypt(path, key):
    print("[+] encryptage ", path)
    # encrypt
    with open(path, "rb") as fIn:
        with open(path+".crp0", "wb") as f0ut:
            pyAesCrypt.encryptStream(fIn, f0ut, str(key), bufferSize)
            print("[+]", path, " encryptage effectue")
            pass
        pass
    os.remove(path)



def decrypt(path, key):
    print("[+] decriptage ", path)
    # get encrypted file size
    enc_file_size = osstat(path).st_size
    # decrypt
    with open(path, "rb") as fIn:
        with open(path.replace(".crp0", ""), "wb") as fOut:
            try:
                # decrypt file stream
                pyAesCrypt.decryptStream(fIn, fOut, str(key), bufferSize, enc_file_size)
                print("[+]", path, " decryptage effectue")
            except ValueError:
                # remove output file on error
                exit("[+] Erreur, veuillez verifier la cle")
                # osremove(path)



def check_encrypt_or_decrypt(do, path, key, erase_it):

    if("encrypt" in str(do).lower()):
        if ".crp0" not in path and ".crp__" not in path:
            print("[+] traitement de : ", path)
            encrypt(path, key)
            if erase_it == True:
                print("[+] enlever l'original de : ", path.replace(".crp0", ""))
                try:
                    osremove(path.replace(".crp0", ""))
                except:
                    print("[+] impossible de supprimer")
                    print("[+] Ignorer: ", path.replace(".crp0", ""))
        else: print("[+] Ignorer: ", path)
    elif("decrypt" in str(do).lower()):
        if ".crp0" in path:
            print("[+] traitemennt de: ", path)
            decrypt(path, key)
            osremove(path)
        else: print("[+] ", path)
    else: exit("[+] Choisir une commande 'encrypt' et 'decrypt'")


def do_stuff(do, path, key, erase_it):

    if(ospath.isfile(path)):
        check_encrypt_or_decrypt(do, path, key, erase_it)
    elif(ospath.isdir(path)):
        print("[+] ----------")
        print("[+] dans "+path)
    else: exit("[+] pas de traitement..")



def var_exist(varr):
    if varr in locals() or varr in globals():
        return True
    return False



def get_method():
    method = input("[+] quel operation voulez vous effectuer? \n[+] Method: (e / d) or (en / de):")
    if "d" in method.lower() or "de" in method.lower():
        return "decrypt"
    elif "e" in method.lower() or "en" in method.lower():
        encrypt = True
        return "encrypt"
    else: exit("[+] Erreur, Veuillez choisir la bonne operation..")



def get_path():
    path = input("[+] Veuillez entre la direction de votre fichier \n[+] le chemin est : ")
    path = ' '.join(path.split())
    if ospath.isfile(path) == False and ospath.isdir(path) == False:
        exit("[+] Erreur, veuillez choisir le bonn chemin.....")
    else:
        if " " in path :
            path = '"' + path + '"'
        return path



def get_secret():
    secret = getpass.getpass("[+] Veuiller entrez le code secret.........")
    if len(secret) > 0: return secret
    else: exit("[+] Erreur, veuillez entre le code secret............")



def get_erase():
    print("permettez moi de vous rappele que crypter les infomation d'une machine qui ne vous\n"
                 "appartient pas est concidere comme du vole et c'est punit par la loi" )


def check_blacklist(path):
    if('\.' in path.lower() or '/.' in path.lower() or '/framework/' in path.lower() or '\\framework\\' in path.lower() or '/vendors/' in path.lower() or '\\vendors\\' in path.lower() or '/bundles/' in path.lower() or '\\bundles\\' in path.lower() or '/lib/' in path.lower() or '\\lib\\' in path.lower()or '/plugins/' in path.lower() or '\\plugins\\' in path.lower() or '.min.' in path.lower() or '/bower_components/' in path.lower() or '\\bower_components\\' in path.lower()  or '/node_components/' in path.lower() or '\\node_components\\' in path.lower()):
        return True
    return False