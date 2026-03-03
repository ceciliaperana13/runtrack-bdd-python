--John Doe ne fait plus partie des étudiants, supprimez-le de la base de données.
DELETE FROM etudiant
WHERE nom = 'Doe' AND prenom = 'John';