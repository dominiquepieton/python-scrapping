'''
Projet :    Scrap V1.0

Objectif du projet est de faire une application afin de pouvoir executer un scrapping en toute simplicité.
On utilisera : 
 - la bibliothèque bs4 pour parser le html.
 - la bibliothèque time pour espace le scrapping
 - la bibliothèque requests pour faire une requête


'''
import requests
import time
from tkinter import *
from bs4 import BeautifulSoup
from console import *

# Affichage en terminal
create_screen(73, 160, 158)
question_screen()