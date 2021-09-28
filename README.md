# OpenClassRoom - Projet 9 - LIT Review

Ce projet a pour but de créer un script Python permettant d'aller chercher des infos sur des livres via le site https://books.toscrape.com/index.html .

# Utilisation

## Environnement virtuel

Pour mettre en place l'environnement virtuel nécessaire pour faire fonctionner le script, procéder comme suit :

Dans un terminal ouvert dans le dossier où vous avez cloné le repository, créez un environnement virtuel a l'aide de 
venv :

```bash
python3 -m venv [nom environnement]
```

Une fois que l'environnement est créé, activez l'environnement (dans cet exemple, 'env' est le nom de mon environnement) :

Windows

```bash
.\env\Scripts\activate
```

Mac / Linux 

```bash
source env/bin/activate
```

Si l'environnement c'est bien activé, le nom de l'environnement s'affichera à gauche de l'indicateur de position 
dans le terminal

Installez tout les packages listé dans le fichier 'requirements.txt' dans votre environnement virtuel :

```bash
pip install -r requirements.txt
```

Vérifier que tout les packages sont bien installé a l'aide de la commande `pip freeze`.

## Lancement

Pour lancer le serveur, entrez cette commande dans un invite de commande :
```bash
python .\manage.py runserver
```

Dans votre navigateur favoris, entrez l'adresse : 127.0.0.1:8000 pour arriver sur le site
