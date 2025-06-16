import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

# Configuration de l'affichage
plt.style.use('default')  # Utilisation du style par défaut
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

# Lecture des données
print("Chargement des données...")
try:
    spotify_history = pd.read_csv('code/spotify_history.csv')
    data_dictionary = pd.read_csv('code/spotify_data_dictionary.csv')
except FileNotFoundError:
    print("Erreur : Impossible de trouver les fichiers de données.")
    print("Assurez-vous que les fichiers 'spotify_history.csv' et 'spotify_data_dictionary.csv' sont dans le dossier 'code/'")
    exit(1)

# Nettoyage des données
spotify_history = spotify_history.dropna(subset=['reason_start', 'reason_end'])

# Conversion des timestamps
spotify_history['ts'] = pd.to_datetime(spotify_history['ts'])
spotify_history['date'] = spotify_history['ts'].dt.date
spotify_history['hour'] = spotify_history['ts'].dt.hour
spotify_history['day_of_week'] = spotify_history['ts'].dt.day_name()

# 1. Statistiques générales
print("\n=== Statistiques générales ===")
print(f"Nombre total d'écoutes : {len(spotify_history):,}")
print(f"Période d'écoute : du {spotify_history['date'].min()} au {spotify_history['date'].max()}")
print(f"Nombre d'artistes uniques : {spotify_history['artist_name'].nunique():,}")
print(f"Nombre de morceaux uniques : {spotify_history['track_name'].nunique():,}")

# 2. Top 10 des artistes les plus écoutés
top_artists = spotify_history.groupby('artist_name').size().sort_values(ascending=False).head(10)
print("\n=== Top 10 des artistes les plus écoutés ===")
print(top_artists)

# 3. Top 10 des morceaux les plus écoutés
top_tracks = spotify_history.groupby(['track_name', 'artist_name']).size().sort_values(ascending=False).head(10)
print("\n=== Top 10 des morceaux les plus écoutés ===")
print(top_tracks)

# 4. Analyse temporelle
# Écoutes par jour de la semaine
daily_plays = spotify_history.groupby('day_of_week').size()
print("\n=== Écoutes par jour de la semaine ===")
print(daily_plays)

# Écoutes par heure de la journée
hourly_plays = spotify_history.groupby('hour').size()
print("\n=== Écoutes par heure de la journée ===")
print(hourly_plays)

# 5. Analyse des comportements
print("\n=== Analyse des comportements ===")
print(f"Pourcentage de morceaux en mode shuffle : {(spotify_history['shuffle'].mean() * 100):.2f}%")
print(f"Pourcentage de morceaux skipés : {(spotify_history['skipped'].mean() * 100):.2f}%")

# 6. Création de visualisations
try:
    # Top 10 des artistes
    plt.figure(figsize=(12, 6))
    top_artists.plot(kind='bar', color='skyblue')
    plt.title('Top 10 des artistes les plus écoutés', pad=20)
    plt.xlabel('Artiste')
    plt.ylabel('Nombre d\'écoutes')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('code/top_artists.png')
    plt.close()

    # Écoutes par heure de la journée
    plt.figure(figsize=(12, 6))
    hourly_plays.plot(kind='line', marker='o', color='green')
    plt.title('Écoutes par heure de la journée', pad=20)
    plt.xlabel('Heure')
    plt.ylabel('Nombre d\'écoutes')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('code/hourly_plays.png')
    plt.close()

    # Écoutes par jour de la semaine
    plt.figure(figsize=(12, 6))
    daily_plays.plot(kind='bar', color='purple')
    plt.title('Écoutes par jour de la semaine', pad=20)
    plt.xlabel('Jour')
    plt.ylabel('Nombre d\'écoutes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('code/daily_plays.png')
    plt.close()

    print("\nLes visualisations ont été sauvegardées dans le dossier 'code/' :")
    print("- top_artists.png")
    print("- hourly_plays.png")
    print("- daily_plays.png")

except Exception as e:
    print(f"\nErreur lors de la création des visualisations : {str(e)}")

# 7. Statistiques supplémentaires
print("\n=== Statistiques supplémentaires ===")
print("\nDurée moyenne d'écoute par morceau :")
print(f"{spotify_history['ms_played'].mean() / 1000:.2f} secondes")

print("\nTop 5 des plateformes utilisées :")
print(spotify_history['platform'].value_counts().head())

print("\nRaisons de fin d'écoute les plus courantes :")
print(spotify_history['reason_end'].value_counts().head()) 