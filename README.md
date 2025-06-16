# Analyse des Données d'Écoute Spotify

Ce projet analyse les données d'écoute d'un utilisateur Spotify pour extraire des insights sur ses habitudes d'écoute musicale.

## Fonctionnalités

- Analyse des artistes et morceaux les plus écoutés
- Analyse temporelle des écoutes (par jour et par heure)
- Analyse des comportements d'écoute (shuffle, skip)
- Visualisations des données
- Statistiques détaillées sur les habitudes d'écoute

## Structure du Projet

```
projet-spotify/
├── code/
│   ├── analyse_spotify.py
│   ├── spotify_history.csv
│   └── spotify_data_dictionary.csv
├── requirements.txt
└── README.md
```

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

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails. 