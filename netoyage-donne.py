import pandas as pd

# Charger les données depuis le fichier CSV
donnees = pd.read_csv("D:/Epsi_2023-2024/MSPR/resultats-france.csv")

# Analyser les données
print("Nombre total de lignes et de colonnes : ", donnees.shape)
print("Informations sur les types de données :")
print(donnees.dtypes)
print("Statistiques descriptives :")
print(donnees.describe())

# Traitement des valeurs manquantes
# donnees = donnees.dropna()  # Supprimer les lignes avec des valeurs manquantes

# Supprimer les doublons
donnees = donnees.drop_duplicates()

# Conversion des types de données
donnees['colonne_date'] = pd.to_datetime(donnees['colonne_date'])  # Conversion en type date

# Vérification de la consistance
# (par exemple, vérifier que certaines colonnes respectent des contraintes logiques)

# Sauvegarder les données nettoyées dans un nouveau fichier CSV
donnees.to_csv("donnees_nettoyees.csv", index=False)

print("Nettoyage et prétraitement des données terminés.")
