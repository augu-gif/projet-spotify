# Analyse des données Spotify

## Objectif
Ce projet vise à classifier et visualiser les préférences musicales d'un utilisateur Spotify.

## Données
Les données proviennent de l'API Spotify et incluent des informations sur: l'URI Spotify, le moment où la lecture du titre s'est arrêtée, Plateforme utilisée lors de la diffusion du titre,Nombre de millisecondes pendant lesquelles le flux a été lu,Nom de la piste, Nom de l'artiste, Nom de l'album, Pourquoi le morceau a commencé, Pourquoi la piste s'est terminée, VRAI ou FAUX selon que le mode aléatoire a été utilisé lors de la lecture de la piste, VRAI ou FAUX selon que l'utilisateur est passé à la chanson suivante.
[projet kaggle](https://www.kaggle.com/code/devraai/analyzing-spotify-streaming-history-insights)

## Notebook

### première étape: importer les bibliotheques dont nous avons besoin sur python pour analyser, trier et visualiser les données.

Grâce aux commandes: 

![tableau jupyter](https://github.com/augu-gif/projet-spotify/blob/main/import-library.png?raw=true)

Nous allons pouvoir nettoyer, trier analyser et visualiser les données:

-import numpy as np = Permet de manipuler les tableaux et calculs numériques.
-import pandas as pd = Permet de  Manipuler et analyser des données tabulaires.
-import seaborn as sns =Permet de Visualiser des données statistiques
-import matplotlib.pyplot as plt = Permet de créer des graphiques en 2D
-plt.switch_backend('Agg') = Permet d'afficher correctement des images sans affichage interactif (backend)
-%matpotlib inline = Permet d'afficher dirrectement les graphiques dans un notebook jupyter
 

## Technologies utilisées
- Python
- Pandas, Matplotlib, Seaborn, Numpy

## Retour vers mon portfolio

[Mon-portfolio-data-analyst](https://github.com/augu-gif/mon-portfolio-data-analyst)

