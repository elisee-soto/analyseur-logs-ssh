# Analyseur de logs SSH

Petit projet Python réalisé pour m'entraîner à lire des logs système et à repérer des tentatives de connexion suspectes sur un service SSH.

L'idée était de partir d'un fichier de logs simple, puis d'extraire les adresses IP qui reviennent souvent dans les échecs d'authentification. Ce n'est pas un outil de sécurité complet, mais plutôt un script d'analyse de base pour comprendre le fonctionnement des logs.

## Objectif

Le script permet de :
- lire un fichier de logs SSH ;
- repérer les lignes contenant un échec de connexion ;
- extraire l'adresse IP source ;
- compter le nombre d'échecs par IP ;
- afficher les adresses qui dépassent un certain seuil.

## Pourquoi ce projet

Je voulais faire un exercice concret autour de l'administration système et de la cybersécurité. Les logs SSH sont un bon point de départ parce qu'ils contiennent beaucoup d'informations utiles, tout en restant assez lisibles pour un premier projet.

## Fichiers du projet

- `ssh_log_analyzer.py` : script principal
- `sample_auth.log` : exemple de fichier de logs
- `README.md` : présentation du projet

## Pré-requis

- Python 3

## Utilisation

Lancer le script avec :

```bash
python ssh_log_analyzer.py