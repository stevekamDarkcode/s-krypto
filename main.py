#!/usr/bin/env python

from os import path as ospath
from sys import exit
import base64
from newstore import*

try: from pathlib import Path
except ImportError as es: exit(str(es))

tiger_start()
erase, encrypt = False, False
method_get, path_get, secret_get, erase_get = get_method(), get_path(), get_secret(), get_erase()


def main_process():

    if var_exist(method_get):
        path = path_get
        key = base64.b64encode(b""+str.encode(secret_get))

        print("[-] Checking the path")
        if(ospath.exists(path)):
            if(ospath.isfile(path)):
                print("[-] verifiez le mots de passe entre")
                do_stuff(method_get, str(path), key, erase)
            else:
                if(ospath.isdir(path)):
                    # if it start with .
                    if (check_blacklist(path)):
                        print("[-] Skipping: ", path)
                    else:
                        print("[-] In "+path)
                        for path in Path(path).glob('**/*'):
                            # because path is object not string
                            # encrypt or decrypt if it's only a file
                            do_stuff(method_get, str(path), key, erase)
                else: print("[=]ce chemin(path) " + str(path) + " n'est pas valide, s'il vous plait veuillez le verifier.")
        else: print("[=] ce chemin(path) " + str(path) + " (file/directory) n'est pas valide.")

   ## else: error_oooo()


def main():

    if "ecraser" in str(erase_get): erase = True

    main_process()
    tiger_end()

if __name__ == '__main__':
	main()