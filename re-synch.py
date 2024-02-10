osuSongsPath = "C:/Users/XXX/AppData/Local/osu!/Songs"

urlForDownload = "https://beatconnect.io/b/"

####################
# Part 1

def createAllList() :
    print("Chemin dans lequel est exécuté le programme de récupération des maps : " + osuSongsPath)

    from os import listdir
    from os.path import isfile, join
    beatmapList = [f for f in listdir(osuSongsPath)]

    for number in beatmapList :
        allList.append(number)
        if (number.split()[0].isdigit()) :
            valideList.append(number)
            splitList.append(number.split()[0])
        else :
            invalideList.append(number)
    
    print("Nombre de map détecté : " + str(len(allList)))
    print("Nombre de map valide : " + str(len(valideList)))
    print("Nombre de map invalide : " + str(len(invalideList)))

def writeList() :

    createAllList()

    name = input("Nom du fichier à écrire (sans .csv, espace, accent ni caractère spéciaux)\n")
    file = open(name + ".csv", "w")

    for ligne in splitList:
        file.write(ligne + "\n")

    file.close()
    
    print("Le fichier " + name + ".csv a été créé/modifié avec succès.")

####################
# Part 2

def compareList():
    print("Le premier fichier csv\n")
    listOrigine = getList()
    print("Le second fichier csv\n")
    listReference = getList()
    name = input("Le nom du fichier à écrire (sans .csv, espace, accent ni caractère spéciaux)\n")

    difference = set(listOrigine) ^ set(listReference)
    needToDownloadList = list(difference)

    fichierNeed = open(name + ".csv", "w")
    for ligne in needToDownloadList:
        fichierNeed.write(ligne + "\n")
    fichierNeed.close()
    
    print("Le fichier " + name + ".csv a été créé avec succès.")

def getList() :
    file = open(selectFile(), "r")
    lines = file.readlines()
    file.close()
    listO = []
    for line in lines:
        listO.append(line.strip())
    return listO
    
####################
# Part 3

def doBeatmapDownload(id) :
    import requests
    url = urlForDownload + str(id)

    # Envoyer une requête GET à l'URL
    response = requests.get(url)

    # Vérifier le code de réponse
    if response.status_code == 200:
        # Obtenir le nom du fichier
        fileName = str(id) + ".osz"

        # Ouvrir le fichier en écriture binaire
        with open(fileName, "wb") as file:
            # Écrire le contenu de la réponse dans le fichier
            file.write(response.content)

        print(f"La beatmap '{fileName}' a été téléchargée avec succès.")
    else:
        print(f"Échec du téléchargement : {response.status_code}")

def doAllBeatmapDownload() :
    name = input("Nom du fichier à lire (sans .csv, espace, accent ni caractère spéciaux)\n")
    fichier = open(name + ".csv", "r")
    lignes = fichier.readlines()
    fichier.close()
    for ligne in lignes:
        needToDownloadList.append(ligne.strip())

    if (len(needToDownloadList) > 0) :
        print("Début des téléchargements")
        i = 0
        y = len(needToDownloadList)
        for id in needToDownloadList :
            doBeatmapDownload(id)
            i = i + 1
            print(str(i/y*100) + "% des téléchargements effectué (" + i + "/" + y + ")")
        print("Fin des téléchargements")
        print("Vous n'avez plus qu'à allez dans votre dossier et exécuter les maps")
    else :
        print("Aucune map à téléchargé dans le fichier " + name + ".csv")

    
####################
# Part 4

def afficherList() :
    name = input("Nom du fichier à lire (sans .csv, espace, accent ni caractère spéciaux)\n")

    fichier = open(name + ".csv", "r")

    lignes = fichier.readlines()

    fichier.close()

    tableau = []

    for ligne in lignes:
        tableau.append(ligne.strip())

    print(tableau)

    return name

####################
# Part 5

def changePath() :
    print(" Le chemin du dossier \"Songs\" est actuellement : " + osuSongsPath)
    print(" Choissisez le dossier Songs, exemple : C:/Users/XXX/AppData/Local/osu!/Songs \n")
    osuSongsPath = selectFolder()
    print(" Le nouveau chemin du dossier \"Songs\" est : " + osuSongsPath)

####################
# Part 6

def printInfo() :
    print(" Le chemin du dossier \"Songs\" est actuellement : " + osuSongsPath)
    print(" Le site par lequelle passe le téléchargement des beatmaps Osu : " + urlForDownload)

####################
# Part Select File/Folder

def selectFile():
    import tkinter as tk
    from tkinter import filedialog

    fileName = filedialog.askopenfilename(title="Sélectionnez un fichier")
    if fileName:
        return fileName
    else :
        print("Problème, aucune action effectuer ")

def selectFolder():
    import tkinter
    from tkinter import filedialog

    folder_path = filedialog.askdirectory(title="Sélectionnez un dossier")
    if folder_path:
        return folder_path
    else :
        print("Problème, aucune action effectuer ")

####################
# Affichage

def afficherBoucle():
    print(
"--------------------------------------------------------\n"
"                                                  #     \n"+
"                                                  #     \n"+
" # ##    ###           ###   #   #  # ##    ###   # ##  \n"+
" ##  #  #   #  #####  #      #   #  ##  #  #   #  ##  # \n"+
" #      #####          ###   #  ##  #   #  #      #   # \n"+
" #      #                 #   ## #  #   #  #   #  #   # \n"+
" #       ###          ####       #  #   #   ###   #   # \n"+
"                             #   #                      \n"+
"                              ###                       \n"+
"--------------------------------------------------------")

    print("\033[0;36m Que voulez vous faire : \033[0m")
    print("(1) - Crée la liste de vos beatmap actuelle")
    print("(2) - Comparer deux liste")
    print("(3) - Télécharger toutes les beatmaps d'une liste")
    print("(4) - Affichez une liste")
    print("(5) - Changer le chemin vers le dossier Songs")
    print("(6) - Affichez les informations sur les données configurer")
    print("(7) - Quittez")

### Inutilisé
def printAdvise() :

    print("\n\n")

    print("\033[0;31m Important :\033[0m choses à savoir avant de commencer")

    print("\033[0;32m 1 :\033[0m À la première ligne du fichier re-synch.py il y a une variable qui " +
    "contient le chemin vers le dossier Songs de osu\n     qu'il faut soit modifier temporairement grâce " +
    "à la fonctionnalité (5) ou en dur dans le code")

    print("\033[0;32m 2 :\033[0m Les entrées de valeurs sont sensibles à la casse (je vérifie rien) donc faîtes attention")

    print("\033[0;32m 3 :\033[0m Le programme est prévue pour windows donc il peut ne pas fonctionner pour Linux,Mac,...")

    print("\033[0;32m 4 :\033[0m Le programme crée les fichiers de sauvegarde dans le répértoire courant (là où est exécuté le programme)")

    print("\033[0;32m 5 :\033[0m Pareil pour l'endroit où les maps sont téléchargé")

    print()

####################
# Main

allList = []
valideList = []
splitList = []
invalideList = []
needToDownloadList = []

finish = False

#printAdvise()

while not finish :

    afficherBoucle()
    
    answer = input("Choissisez parmi 1 à 7\n")

    match answer : 
        case "1" :
            writeList()
        case "2" :
            compareList()
        case "3" :
            doAllBeatmapDownload()
        case "4" :
            tmp = afficherList()
            print("Pour plus de lisibilité allez lire " + tmp + ".csv")
        case "5" :
            changePath()
        case "6" :
            printInfo()
        case "7" :
            finish = True
    
    if not (finish) :
        input("\nAppuyez sur (Entrée) pour passer à la suite")



    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

print("Fin du programme")


















#liste1 = ["a", "b", "c", "d", "e"]
#liste2 = ["a", "b", "d", "f", "g"]

# Convertir les listes en ensembles
#ensemble1 = set(liste1)
#ensemble2 = set(liste2)

# Obtenir la différence entre les deux ensembles
#differences = ensemble1.difference(ensemble2)

# Convertir l'ensemble en liste
#differences = list(differences)

# Afficher la liste des différences
#print(differences)