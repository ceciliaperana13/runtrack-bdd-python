--comptabiliser la capacité totale de toutes les salles présentes en base de données.
SELECT SUM(capacite) AS capacite_totale
FROM salle;