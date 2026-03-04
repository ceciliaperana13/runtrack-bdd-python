--insert un nouvel étudiant
INSERT INTO etudiant (nom, prenom, age, email)
VALUES ('Dupuis', 'Martin', 18, 'martin.dupuis@laplateforme.io');

--recuperer toute les informations de la famille dupuis
SELECT*
FROM etudiant
WHERE nom = 'Dupuis';