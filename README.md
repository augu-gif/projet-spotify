# Analyse des Données d'Écoute Spotify

Ce projet analyse les données d'écoute d'un utilisateur Spotify pour extraire des insights sur ses habitudes d'écoute musicale.

## Fonctionnalités

- Analyse des artistes et morceaux les plus écoutés
- Analyse temporelle des écoutes (par jour et par heure)
- Analyse des comportements d'écoute (shuffle, skip)
- Visualisations des données
- Statistiques détaillées sur les habitudes d'écoute

## Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/[votre-username]/projet-spotify.git
cd projet-spotify
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation

Exécutez le script d'analyse :
```bash
python code/analyse_spotify.py
```

Le script générera :
- Des statistiques dans la console
- Des visualisations dans le dossier `code/` :
  - `top_artists.png` : Top 10 des artistes les plus écoutés
  - `hourly_plays.png` : Distribution des écoutes par heure
  - `daily_plays.png` : Distribution des écoutes par jour

## Dépendances

- pandas >= 1.5.0
- numpy >= 1.21.0
- matplotlib >= 3.5.0
- seaborn >= 0.11.0
- plotly >= 5.13.0

## Résultats 

![image](https://github.com/user-attachments/assets/5e955e6c-6f3f-41ca-a3b5-694f75b4b976)

![image](https://github.com/user-attachments/assets/fd15638b-21ec-45ef-a9f1-b1dc5281f5ff)

![image](https://github.com/user-attachments/assets/e0158dec-0d6a-4eec-8906-f7dafb57c6c8)


Statistiques générales
Total de morceaux écoutés : 149 648

Période couverte : du 08/07/2013 au 15/12/2024

Artistes différents : 4 105

Titres uniques : 13 801

Top 10 artistes
Artiste	Écoutes
The Beatles	13 620
The Killers	6 876
John Mayer	4 851
Bob Dylan	3 808
Paul McCartney	2 697
Led Zeppelin	2 476
Johnny Cash	2 470
The Rolling Stones	2 390
Radiohead	2 303
The Black Keys	2 231

Top 10 morceaux
Titre	Artiste	Écoutes
Ode To The Mets	The Strokes	207
In the Blood	John Mayer	181
Dying Breed	The Killers	166
Caution	The Killers	164
19 Dias y 500 Noches (live)	Joaquín Sabina	148
Concerning Hobbits	Howard Shore	142
All These Things That I've Done	The Killers	142
Come Together (Remastered 2009)	The Beatles	137
Yesterday (Remastered 2009)	The Beatles	134
Crucify Your Mind	Rodríguez	131

Habitudes d’écoute
Par jour de la semaine
Jour	Écoutes
Vendredi	25 623
Mercredi	23 333
Jeudi	21 364
Lundi	21 013
Mardi	20 691
Samedi	19 385
Dimanche	18 239

Par heure de la journée
Écoute assez nocturne. Gros pics à minuit, 20h et 23h.
Creux vers 8h-10h du mat (logique).

Comportement utilisateur
Mode aléatoire (shuffle) activé dans 75 % des cas

Skip environ 5 % des morceaux

Graphiques générés
Les visuels sont dispos dans le dossier code/ :

top_artists.png

hourly_plays.png

daily_plays.png

Détails techniques
Durée moyenne d’un morceau écouté : 128 secondes

Plateformes les plus utilisées
Plateforme	Écoutes
Android	139 821
Cast to device	3 893
iOS	2 842
Windows	1 691
macOS	1 176

Raisons de fin d’écoute
Raison	Cas
Fin normale	77 110
Appui sur suivant	53 462
Fin du morceau naturellement	10 116
Déconnexion	4 367
Retour arrière	2 182



[Retour sur Mon Portfolio](https://github.com/augu-gif/mon-portfolio-data-analyst/blob/main/README.md)
