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

![image](https://github.com/user-attachments/assets/225ce00c-aeeb-44d1-a0c7-82e5a05a6ba6)

=== Statistiques générales ===
Nombre total d'écoutes : 149,648
Période d'écoute : du 2013-07-08 au 2024-12-15
Nombre d'artistes uniques : 4,105
Nombre de morceaux uniques : 13,801

=== Top 10 des artistes les plus écoutés ===
artist_name
The Beatles           13620
The Killers            6876
John Mayer             4851
Bob Dylan              3808
Paul McCartney         2697
Led Zeppelin           2476
Johnny Cash            2470
The Rolling Stones     2390
Radiohead              2303
The Black Keys         2231
dtype: int64

=== Top 10 des morceaux les plus écoutés ===
track_name                         artist_name
Ode To The Mets                    The Strokes       207
In the Blood                       John Mayer        181
Dying Breed                        The Killers       166
Caution                            The Killers       164
19 Dias y 500 Noches - En Directo  Joaquín Sabina    148
Concerning Hobbits                 Howard Shore      142
All These Things That I've Done    The Killers       142
Come Together - Remastered 2009    The Beatles       137
Yesterday - Remastered 2009        The Beatles       134
Crucify Your Mind                  Rodríguez         131
dtype: int64

=== Écoutes par jour de la semaine ===
day_of_week
Friday       25623
Monday       21013
Saturday     19385
Sunday       18239
Thursday     21364
Tuesday      20691
Wednesday    23333
dtype: int64

=== Écoutes par heure de la journée ===
hour
0     10869
1      9377
2      9016
3      8541
4      6345
5      7150
6      7363
7      4409
8      2312
9      1695
10     1207
11      903
12      724
13     1658
14     2759
15     3725
16     6735
17     9181
18     8932
19     8146
20    10467
21     8926
22     8706
23    10502
dtype: int64

=== Analyse des comportements ===
Pourcentage de morceaux en mode shuffle : 74.54%
Pourcentage de morceaux skipés : 5.18%

Les visualisations ont été sauvegardées dans le dossier 'code/' :
- top_artists.png
- hourly_plays.png
- daily_plays.png

=== Statistiques supplémentaires ===

Durée moyenne d'écoute par morceau :
128.29 secondes

Top 5 des plateformes utilisées :
platform
android           139821
cast to device      3893
iOS                 2842
windows             1691
mac                 1176
Name: count, dtype: int64

Raisons de fin d'écoute les plus courantes :
reason_end
trackdone    77110
fwdbtn       53462
endplay      10116
logout        4367
backbtn       2182
Name: count, dtype: int64


[Retour sur Mon Portfolio](https://github.com/augu-gif/mon-portfolio-data-analyst/blob/main/README.md)
