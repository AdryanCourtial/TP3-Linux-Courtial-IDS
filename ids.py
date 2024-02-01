#!/usr/bin/env python3
""" Lib 


"""
from os.path import getctime, getsize, getmtime, exists, isdir
from os import mkdir, stat
from argparse import ArgumentParser
from json import load, dumps
from subprocess import run
from hashlib import md5,sha256,sha512
from datetime import datetime
from psutil import net_connections, CONN_LISTEN
# from dirhash import dirhash


now = datetime.now()
# Argument
parser= ArgumentParser()
parser.add_argument( "-build", "--build",
                    action="store_const", const=1,
                    help="""construit un fichier JSON qui contient un état
                    des chosesqu'on a demandé à surveiller""")
parser.add_argument( "-check", "--check",
                    action="store_const", const=1,
                    help="""vérifie que l'état actuel est conforme à
                    ce qui a été stocké dans | /var/ids/db.json | """)
parser.add_argument( "-init", "--init",
                    action="store_const", const=1,
                    help="""Commande à Lancer des la PREMIERE UTILISATION""")
arg = parser.parse_args()


def string_to_json(path, arg, to_jsonify):
    if exists(path) is True:
        with open(path, arg, encoding="utf8") as json_file:
            json_file.truncate(0)
            conf_json = dumps(to_jsonify)
            json_file.write(conf_json)



def create_file_conf():
    """ 
    
    Cree le fichier de conf
    """
    if exists("/etc/ids.json") is False:
        with open("/etc/ids.json", "w", encoding="utf8") as json_file:
            conf_json = dumps(base_data_conf)
            json_file.write(conf_json)


def create_clone_json():
    """

    Cree le Fichier Json
    """
    if isdir("/var/ids") is False:
        mkdir("/var/ids")
        with open("/var/ids/db.json", "x", encoding="utf-8") as _:
            ...


def create_logs():
    """

    Cree le Fichier Logs
    """


    if exists("/var/log/ids.log"):
        return
    with open("/var/log/ids.log", "x", encoding="utf-8") as _:
        pass


def create_bin():
    """

    Create le bin
    """


    if exists("/var/local/bin/ids.py"):
        return
    #Bouger de place le fichier exe ids.py dans var/local/bin/ids.py


def create_right():
    """
    
    Cree les Droits pour L'app
    """


    run(['useradd', '-p', 'ids', 'ids'], check=False)
    run(['chmod', '-R', 'u+rw', '/etc/ids.json'], check=False)
    run(['chmod', '-R', 'u+rw', '/var/ids/db.json'], check=False)
    run(['chmod', '-R', 'u+rw', '/var/log/ids.log'],check=False)
    run(['chown', '-R', 'ids:ids', '/var/log/ids.log' , '/etc/ids.json', '/var/ids/db.json'],
         check=False)


def is_init() -> bool:
    """
    
    Verif si Lutilisateur as deja fais un init
    """


    if exists("/etc/ids.json"):
        return True
    return False


def recup_json_conf():
    """
    
    Recuperere la Conf Json Pour la Traiter
    """
    with open("/etc/ids.json", "r", encoding="utf-8") as jsonfile:
        conf = load(jsonfile)
        print("Read Succes")
        return conf


def is_file(conf)->bool:
    """

    Verifie Si la Fichier est un Fichier 
    """


    if conf['file'] == []:
        return False
    return True


def is_dir(conf)->bool:
    """
    
    Verifie is Le fichier est un Dossier
    """


    if conf['dir'] == []:
        return False
    return True


def if_port(conf)-> bool :
    """
    
    Verifie si Les ports doivent etre verifié 
    """

    if conf['port'] is False:
        return False
    return True


def hash_sha512(file):
    """
    
    Hash Le fichier en Sha512
    """


    sha512_hash = sha512()
    with open(file, "rb") as f:
        #Lie un Chunk
        for chunk in iter(lambda: f.read(4096), b""):
            sha512_hash.update(chunk)
    return sha512_hash.hexdigest()


def hash_sha256(file):
    """
    
    Hash Le Fichier en Sha256
    """


    sha256_hash = sha256()
    with open(file, "rb") as f:
        #Lie un Chunk
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()


def hash_md5(file):
    """
    
    Hash Le Fichier en MD5
    """


    md5_hash = md5()
    with open(file, "rb") as f:
        #Lie un Chunk
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)

    return md5_hash.hexdigest()


def create_db_file(conf):
    """
    
    Cree la Copie des File a verif
    """


    for file in conf['file']:
        file_info = stat(file)
        data_db_info = {
            'name':file,
            "sha512":hash_sha512(file),
            "sha256":hash_sha256(file),
            "md5":hash_md5(file),
            "last_change":getctime(file),
            "date_creation":getmtime(file),
            "owner":file_info.st_uid,
            "group":file_info.st_gid,
            "size":getsize(file)
        }
        print("Essaie")
        data_db.append(data_db_info)


def create_db_dir(conf):
    """
    
    Cree la Copie des Dir a Verif
    """
    for dir in conf['dir']:
        dir_info = stat(dir)
        data_db_info = {
            'name':dir,
            # "sha512":dirhash(dir, sha512),
            # "sha256":dirhash(dir, sha256),
            # "md5":dirhash(dir, md5),
            "last_change":getctime(dir),
            "date_creation":getmtime(dir),
            "owner":dir_info.st_uid,
            "group":dir_info.st_gid,
            "size":getsize(dir)
        }
        print("Essaie")
        data_db.append(data_db_info) #IL FAUT REGARDER SI LE DOSSIER ET REMPLIE ET AUUUSI VERIF LES SOUS FICHIERS (LE BORDEL EN GROS) (ON VA FAIRE QUE LE DOSSIER POUR LINSTANT)


def create_db_port():
    connections = net_connections(kind='inet')

# filter to get only ports equal to LISTEN
    my_ports = [conn.laddr.port for conn in connections if conn.status == CONN_LISTEN]

# Exclude duplicate ports
    my_ports = list(set(my_ports))

# Order from smallest to largest port
    my_ports.sort()

# Show the TCP ports that is waiting for connection (LISTENING)
    for port in my_ports:
        print(f"My Open TCP port= {port}  is LISTENING  for TCP connection")
        ports = {
            "name": port
        }
        port_db.append(ports)


def write_json_db():
    """
    
    On Va ecrire tous ce qu'il y as dans l'obj db dans le ficheir db.json 
    """
    ... 

    
    


# Data #######################################################################################


base_data_conf = {
    "file":[],
    "dir":[],
    "port":False 
}


data_db_map = {
    "date": "",
}

data_db = []

port_db = []


################################################################################################


if __name__ == '__main__':


    #Verif Quelle arguement est passé
    if arg.init == 1:
        if is_init() is False:
            create_file_conf()
            create_clone_json()
            create_logs()
            create_bin()
            create_right()
        else:
            print("Le Init a Déja etais Utilisé")

    #Verif Quelle arguement est passé
    if arg.build == 1:
        if is_init() is False:
            print("ERREUR: Utililse (-init) La premiere fois")
        else:
            data_conf = recup_json_conf()
            data_db_map["infos"] = data_db
            #Date Actuelle lors de la Creatrion Du fichier
            data_db_map['date'] = now.strftime("%d/%m/%Y %H:%M:%S")
            #Verif Si il y a des Fichier dans la Conf
            if is_file(data_conf) is True:
                create_db_file(data_conf)
            if is_dir(data_conf) is True:
                create_db_dir(data_conf)
            if if_port(data_conf) is True:
                create_db_port()

            #Ajout a Mon Objet Final de Tout
            data_db_map["infos"] = data_db
            data_db_map["port_listen"] = port_db
            string_to_json("/var/ids/db.json", "wr+", data_db_map)


    #Verif Quelle arguement est passé
    if arg.check == 1:
        if is_init() is False:
            print("ERREUR: Utililse (-init) La premiere fois")
        else:
            print("check")
