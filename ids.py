from sys import argv
import os
import argparse

# Argument 

parser= argparse.ArgumentParser()
parser.add_argument( "-b", "--build", default=False, help="construit un fichier JSON qui contient un état des choses qu'on a demandé à surveiller")
parser.add_argument( "-c", "--check", default=False, help="vérifie que l'état actuel est conforme à ce qui a été stocké dans | /var/ids/db.json | ")
arg = parser.parse_args()

if argv[1] == "build":
    print("build")

if argv[1] == "check":
    print("check")

