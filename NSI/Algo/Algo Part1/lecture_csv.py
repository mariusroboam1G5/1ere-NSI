"""
import csv
fichier = open("données.csv", "r")
lecture_fichier = csv.DictReader(fichier, delimiter=',')

liste_personnes = []
for ligne in lecture_fichier:
    liste_personnes.append(dict(ligne))
fichier.close()

for personne in liste_personnes :
    print(personne)
"""
import csv
fichier = open("ballon2019.csv", "r", encoding="utf-8")
lecture_fichier=csv.DictReader(fichier, delimiter’,’)
liste_enregistrement = []
for ligne in lecture_fichier :
    liste_enregistrements.append(dict(ligne))
fichier.close()
horaire_tmp_min = ''
tmp_min = 100.

for enregistrement in liste_enregistrements:
    if  float(enregistrement(['Temp Ext C']))<tmp_min:
        tmp_min=float(enregistrement(['Temp Ext C'])
        horaire_tmp_min=enregistrement['Horaire']
print(horaire_tmp_min,tmp_min)