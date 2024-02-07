import pandas as pd

# Chemin vers le fichier Excel
chemin_fichier_excel = "D:/Epsi_2023-2024/MSPR/resultats-france.xlsx"

# Charger le fichier Excel dans un DataFrame Pandas
donnees_excel = pd.read_excel(chemin_fichier_excel)

# Afficher les premières lignes du DataFrame pour vérifier l'importation des données
# print(donnees_excel.head())

# Chemin pour sauvegarder le fichier CSV
chemin_fichier_csv = "resultats-france.csv"

# Sauvegarder le DataFrame au format CSV
donnees_excel.to_csv(chemin_fichier_csv, index=False)

print("Données sauvegardées au format CSV avec succès.")
