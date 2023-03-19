# Imports
import os
from datetime import datetime
from datetime import timedelta


def convert(date_time):
    format = '%H:%M:%S'  # The format
    datetime_str = datetime.strptime(date_time, format)
    return datetime_str

def get_sec(time_str):
    """Get seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

os.system("cls")
repertoire = input("Quel est le chemin complet pour accéder au fichier ? \n") + "\\"
#fichier = input("Quel est le nom du fichier ? \n")
fichier = repertoire + "Calendrier-octobre-test.csv"


# Récupération des informations du fichier
f = open(fichier,"r")
test_read = f.read()
f.close()
#os.system("rem " + repertoire + fichier)

# Traitement des informations
test_read = test_read.replace('"','')
lines = test_read.splitlines()
lines.pop(0)


# On cherche à déduire le temps passé pour 1 activité

tps_adm_com = convert("00:00:00")
tps_reu_ent = convert("00:00:00")
tps_act_ter = convert("00:00:00")
tps_act_jeu = convert("00:00:00")
tps_ran_tri = convert("00:00:00")
tps_ani_sta = convert("00:00:00")

print("ATTENTION CES LIGNES N'ONT PAS DE CATEGORIE ")
for line in lines:
    line = line.split(",")
    #print(line)
    #os.system("pause")
    timeEnd = convert(line[4])
    timeStart = convert(line[2])
    tps_delta = timeEnd - timeStart
    #tps_delta = get_sec(tps_delta)

    if len(line) == 6:
        if line[5] == 'Administratif/communication': tps_adm_com += tps_delta
        if line[5] == 'Réunion-Entretien': tps_reu_ent += tps_delta
        if line[5] == 'Rangement/tri/déménagement': tps_ran_tri += tps_delta
        if line[5] == 'Action terrain': tps_act_ter += tps_delta
        if line[5] == 'Action jeunesse': tps_act_jeu += tps_delta
        if line[5] == 'Animation-Stand': tps_ani_sta += tps_delta
    if len(line) < 6:
        print(line)       
    
print("---------------------------------------")
print("Administratif/communication : ",tps_adm_com)
print("Réunion-Entretien : ",tps_reu_ent)
print("Rangement/tri/déménagement : ",tps_ran_tri)
print("Action terrain : ",tps_act_ter)
print("Action jeunesse : ",tps_act_jeu)
print("Animation-Stand : ",tps_ani_sta)