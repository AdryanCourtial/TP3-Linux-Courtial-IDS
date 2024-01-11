from sys import argv
import os
import argparse
import __future__

# Argument 
parser= argparse.ArgumentParser()
parser.add_argument( "-build", "--build", action="store_const", const=1, help="construit un fichier JSON qui contient un état des choses qu'on a demandé à surveiller")
parser.add_argument( "-check", "--check", action="store_const", const=1, help="vérifie que l'état actuel est conforme à ce qui a été stocké dans | /var/ids/db.json | ")
arg = parser.parse_args()

#FONCTION##############################################################################
def CreateFileConf():
    if os.path.exists("/etc/ids.json"):
        return
    else:
        open("/etc/ids.json", "x")


def CreateCloneJson():
    if os.path.isdir("/etc/ids"):
        return 
    else:
        os.mkdir("/etc/ids")
        os.open("/etc/ids/db.json", "x")

#######################################################################################
        




if __name__ == '__main__':

    CreateFileConf()
    CreateCloneJson()

    #Verif Quelle arguement est passé
    if arg.build == 1:
        print("build")




    #Verif Quelle arguement est passé
    if arg.check == 1:
        print("check")






