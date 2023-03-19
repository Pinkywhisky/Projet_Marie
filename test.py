import datetime
import os

def convert(date_time):
    format = '%H:%M:%S'  # The format
    datetime_str = datetime.datetime.strptime(date_time, format)

    return datetime_str

os.system("cls")

heureDebut = "10:00:00"
heureFin = "12:30:00"

heureDebut = convert(heureDebut)
heureFin = convert(heureFin)

delta = heureFin - heureDebut

print(delta)