#!/usr/bin/env python3
from sys import argv
import os
import argparse
import __future__
import json
import subprocess
import hashlib

# Argument 
parser= argparse.ArgumentParser()
parser.add_argument( "-build", "--build", action="store_const", const=1, help="construit un fichier JSON qui contient un état des choses qu'on a demandé à surveiller")
parser.add_argument( "-check", "--check", action="store_const", const=1, help="vérifie que l'état actuel est conforme à ce qui a été stocké dans | /var/ids/db.json | ")
parser.add_argument( "-init", "--init", action="store_const", const=1, help="Commande à Lancer des la PREMIERE UTILISATION")
arg = parser.parse_args()

#FONCTION ##############################################################################

def CreateFileConf():
    if os.path.exists("/etc/ids.json"):
        return
    else:
        open("/etc/ids.json", "x")
        #Write Json Conf
        ConfJson = json.dumps(BaseDataConf)
        with open("/etc/ids.json", "w") as jsonfile:
            jsonfile.write(ConfJson)
            print("Write Succes")

def CreateCloneJson():
    if os.path.isdir("/var/ids"):
        return 
    else:
        os.mkdir("/var/ids")
        open("/var/ids/db.json", "x")

def CreateLogs():
    if os.path.exists("/var/log/ids.log"):
        return
    else:
        open("/var/log/ids.log", "x")

def CreateBin():
    if os.path.exists("/var/local/bin/ids.py"):
        return
    else:
        pass
        #Bouger de place le fichier exe ids.py dans var/local/bin/ids.py



def CreateRight():
    subprocess.run(['useradd', '-p', 'ids', 'ids'])
    subprocess.run(['chmod', '-R', 'u+rw', '/etc/ids.json'])
    subprocess.run(['chmod', '-R', 'u+rw', '/var/ids/db.json' ])
    subprocess.run(['chmod', '-R', 'u+rw', '/var/log/ids.log' ])
    subprocess.run(['chown', '-R', 'ids:ids', '/var/log/ids.log' , '/etc/ids.json', '/var/ids/db.json'])


def IsInit() -> bool:
    if os.path.exists("/etc/ids.json"):
        return True
    else:
        return False
    
def RecupJsonConf():
    with open("/etc/ids.json", "r") as jsonfile:
        DataConf = json.load(jsonfile)
        print("Read Succes")
        return DataConf

def IfFile(DataConf)->bool:
    if DataConf['file'] == []:
        return False
    else: 
        return True

def ifDir(DataConf)->bool:
    if DataConf['dir'] == []:
        return False
    else:
        return True

def ifPort(DataConf)-> bool :
    if DataConf['port'] == False:
        return False
    else:
        return True
    
def HashSha512(file):
    with open(file, "rb") as f:
        digest = hashlib.sha256(f)
        return digest.hexdigest()  

def HashSha256(file):
    with open(file, "rb") as f:
        digest = hashlib.sha512(f)
        return digest.hexdigest()  

def HashMD5(file):
    with open(file, "rb") as f:
        digest = hashlib.md5(f)
        return digest.hexdigest()  
    
def CreateDbFile(DataConf):
    for file in DataConf['file']:
        file_info = os.stat(file)
        DataDBInfo = {
            'name':file,
            "sha512":HashSha512(file),
            "sha256":HashSha256(file),
            "md5":HashMD5(file),
            "last_change":os.path.getctime(file),
            "date_creation":os.path.getmtime(file),
            "owner":file_info.st_uid,
            "group":file_info.st_gid,
            "size":os.path.getsize(file)
        }
        print("Essaie")
        DataDB.append(DataDB)



# Data #######################################################################################

global DataConf

BaseDataConf = {
    "file":[],
    "dir":[],
    "port":False 
}


DataDBmap = {
    "date": "eeee",
    "port": {},
}

DataDB = []

DataDBInfo = {
    "name":"",
    "sha512":"",
    "sha256":"",
    "md5":"",
    "last_change":"",
    "date_creation":"",
    "owner":"",
    "group":"",
    "size":""
}


################################################################################################


if __name__ == '__main__':


    #Verif Quelle arguement est passé
    if arg.init == 1:
        if IsInit() == False:
            CreateFileConf()
            CreateCloneJson()
            CreateLogs()
            CreateBin()
            CreateRight()
        else:
            print("Le Init a Déja etais Utilisé")

    #Verif Quelle arguement est passé
    if arg.build == 1:
        if IsInit() == False:
            print("ERREUR: Utililse (-init) La premiere fois")
        else:
            DataConf = RecupJsonConf() 
            DataDBmap["infos"] = DataDB
            if IfFile(DataConf) == True:
                CreateDbFile(DataConf)
            
            DataDBmap["infos"] = DataDB
            print(DataDBmap)
            pass



    #Verif Quelle arguement est passé
    if arg.check == 1:
        if IsInit() == False:
            print("ERREUR: Utililse (-init) La premiere fois")
        else:
            print("check")
