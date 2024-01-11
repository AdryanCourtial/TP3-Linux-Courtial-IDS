from sys import argv
import os
import argparse

# Argument 

parser= argparse.ArgumentParser()
parser.add_argument( "-build", "--build", action="store_const", const=1, help="construit un fichier JSON qui contient un état des choses qu'on a demandé à surveiller")
parser.add_argument( "-check", "--check", action="store_const", const=1, help="vérifie que l'état actuel est conforme à ce qui a été stocké dans | /var/ids/db.json | ")
arg = parser.parse_args()



if arg.build == 1:
    print("build")

if arg.check == 1:
    print("check")

