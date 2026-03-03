import mysql.connector
 

# Connexion a la base de donnees
mysql_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Cecilia13,",
    database="laplateforme"
)
# Creation d'un curseur pour executer les requetes SQL
cursor = mysql_db.cursor()
# Requete SQL pour recuperer les informations de tous les etudiants
cursor.execute("SELECT * FROM etudiant")
# Recuperation de tous les resultats de la requete
resultats = cursor.fetchall()
# Affichage 
for resultat in resultats:
    print(resultat)
# Fermeture 
cursor.close()
mysql_db.close()