import mysql.connector

# Connexion a la base de donnees
mysql_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Cecilia13,",
    database="laplateforme"
)

# Creation d'un curseur buffered pour executer plusieurs requetes
cursor = mysql_db.cursor(buffered=True)

# Table etudiant
cursor.execute("SELECT * FROM etudiant")
print("=== TABLE ETUDIANT ===")
for resultat in cursor.fetchall():
    print(resultat)

# Table salle
cursor.execute("SELECT * FROM salle")
print("\n=== TABLE SALLE ===")
for resultat in cursor.fetchall():
    print(resultat)

# Table etage
cursor.execute("SELECT * FROM etage")
print("\n=== TABLE ETAGE ===")
for resultat in cursor.fetchall():
    print(resultat)

# Fermeture
cursor.close()
mysql_db.close()