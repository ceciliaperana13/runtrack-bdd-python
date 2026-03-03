--compter le nombre d’étudiants mineurs présents en base de données.
SELECT COUNT(*) AS nombre_etudiants
FROM etudiant
WHERE age < 18;