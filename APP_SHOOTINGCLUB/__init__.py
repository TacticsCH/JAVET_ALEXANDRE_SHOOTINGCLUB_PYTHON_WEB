# Un objet "obj_mon_application" pour utiliser la classe Flask
# Pour les personnes qui veulent savoir ce que signifie __name__ une démonstration se trouve ici :
# https://www.studytonight.com/python/_name_-as-main-method-in-python
# C'est une chaîne de caractère qui permet de savoir si on exécute le code comme script principal
# appelé directement avec Python et pas importé.
from flask import Flask, flash, render_template
from APP_SHOOTINGCLUB.DATABASE import connect_db_context_manager


# Objet qui fait "exister" notre application
obj_mon_application = Flask(__name__, template_folder="templates")
# Flask va pouvoir crypter les cookies
obj_mon_application.secret_key = '_vogonAmiral_)?^'

# Doit se trouver ici... soit après l'instanciation de la classe "Flask"
# OM 2020.03.25 Tout commence ici par "indiquer" les routes de l'application.
from APP_SHOOTINGCLUB import routes
from APP_SHOOTINGCLUB.CONCOURS import routes_gestion_concours
from APP_SHOOTINGCLUB.PERSONNE import routes_gestion_personne
from APP_SHOOTINGCLUB.PERSONNE_CONCOURS import routes_gestion_genres_films
from APP_SHOOTINGCLUB.ARME import routes_gestion_arme
from APP_SHOOTINGCLUB.MUNITION import routes_gestion_munition
from APP_SHOOTINGCLUB.TYPE_ARME import routes_gestion_type_arme
from APP_SHOOTINGCLUB.STAND_DE_TIR import routes_gestion_stand_de_tir
