'''
TRANSFORMATION DU FICHIER CSV EN .JSON avec deux methodes........
deuxieme methode à transformer en function pour le faire automatiquement.....
'''



import csv
import json

#lire les lignes
'''
with open('c.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('test.json', 'w') as fp:
        for row in reader:
            dict_data = {           
                'article' : row[0],
                'link_image' : row[1],
                'vendeur' : row[2],
                'prix' : row[3]    
            }
            print(dict_data)
            json.dump(dict_data, fp, indent=6)
'''

csvfile = open('c.csv', 'r')
jsonfile = open('test.json', 'w')


fieldnames = ("article","url_image","vendeur","price")
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ], indent=4 )
jsonfile.write(out)