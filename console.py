'''
console.py est prevu pour créer un affichage dans la console.

'''
from bs4 import BeautifulSoup
import requests
import time


def scrap_data(response, balise, attr, attr_name):
    soup = BeautifulSoup(response.text, features="html.parser")
    tag = soup.find(balise, {attr: attr_name})
    if not balise == 'img':
        print(f"{tag.text}")
        print()
        return tag.text
    else:
        print(f"{tag.get('src')}")
        print()
        return tag.get('src')


def create_screen(nb_title, nb_ligne, nb_espace):
    etoile= "*"
    espace= " "
    title = etoile + (nb_title*espace) + " Scrap V1.0 " + (nb_title*espace) + etoile
    ligne = nb_ligne*etoile
    ligne_vide = etoile + (nb_espace*espace) + etoile


    print(ligne)
    print(ligne_vide)
    print(ligne_vide)
    print(title)
    print(ligne_vide)
    print(ligne_vide)
    print(etoile + (espace*42) + "Vous devez remplir les questions proposées afin d'effectuer le scrapping.." + (42*espace) + etoile)
    print(ligne)


def question_screen():
    print("recherche du nom de l'article :")
    print("-------------------------------")
    balise1 = input(" - nom de la balise titre:   > ")
    attr1 = input(' - attribut:    >  ')
    name1 = input(' - nom attribut:  >  ')
    print()
    print("recherche de la photo :")
    print("-----------------------")
    balise2 = input(" - nom de la balise de la photo:   >  ")
    attr2 = input(' - attribut:    >  ')
    name2 = input(' - nom attribut:    >  ')
    print()
    print("recherche nom du vendeur :")
    print("--------------------------")
    balise3 = input(" - balise nom du vendeur:      >  ")
    attr3 = input(' - attribut:    >  ')
    name3 = input(' - nom attribut:  >   ')
    print()
    print("recherche du prix :")
    print("--------------------")
    balise4 = input(" - balise du prix:    > ")
    attr4 = input(' - attribut:     > ')
    name4 = input(' - nom attribut:     >  ')
    print()
    print("Nom du fichier a lire  .txt :")
    print("-------------------------------------")
    read_file = input(" - Nom du fichier à lire:    >  ")
    print()
    print(" - Nom du fichier à la fin mettre .csv :")
    print("-------------------------------------")
    namefile = input(" - Nom du fichier à créer:    >  ")
    print()

    with open('urls/'+ read_file, 'r') as file:
        with open('sauvegarde_data/' + namefile, 'w') as out:
            out.write('produit,image,vendeur,prix\n')
            for row in file:
                url = row.strip()
                response = requests.get(url)
                if response.ok:
                    title = scrap_data(response, balise1, attr1, name1)
                    image_url = scrap_data(response, balise2, attr2, name2)
                    vendeur = scrap_data(response, balise3, attr3, name3)
                    price = scrap_data(response, balise4, attr4, name4)
                    time.sleep(2)
                if title and image_url and vendeur and price:
                    out.write(title.replace(",", "") + ',' + image_url + ',' + vendeur  + ',' + price.replace("EUR", "").replace(",", ".") + '\n')

    csvfile = open('c.csv', 'r')
    jsonfile = open('test1.json', 'w')


    fieldnames = ("article","url_image","vendeur","price")
    reader = csv.DictReader( csvfile, fieldnames)
    out = json.dumps( [ row for row in reader ], indent=4 )
    jsonfile.write(out)