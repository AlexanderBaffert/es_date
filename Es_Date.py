#Baffert
#Es data

import datetime

#stampare la data corrente

Orario_C = datetime.datetime.now()
print(Orario_C)

#creazione della nostra data di compleanno e stamparla

compleanno = datetime.datetime(2006, 9, 25)

print(compleanno)

#stampa compleanno con stringa

stringa = datetime.datetime(2018, 6, 1)

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%A"+  x.strftime(" %B")))

#calcolo della differenza tra data corrente ela nostra

