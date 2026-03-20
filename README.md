# Analyseur de logs SSH

## Description
Ce projet est un script Python permettant d'analyser un fichier de logs SSH afin de détecter des tentatives de connexion suspectes.

Il identifie les adresses IP ayant plusieurs échecs de connexion, ce qui peut indiquer une attaque par brute force.

## Fonctionnalités
- Lecture d'un fichier de logs SSH
- Détection des tentatives de connexion échouées
- Extraction des adresses IP
- Comptage des tentatives par IP
- Identification des IP suspectes

## Technologies utilisées
- Python 3

## Utilisation

1. Placer un fichier de logs nommé `sample_auth.log` dans le dossier
2. Lancer le script :

```bash
python ssh_log_analyzer.py