import csv
import random
    
# Nom du fichier à créer
filename = "data/dum_prediction.csv"
# Création du fichier CSV
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "TARGET"])  # En-têtes
    
    start_id = 225000
    for i in range(75000):
        writer.writerow([start_id + i, random.randint(0, 1)])  # 0 ou 1 aléatoire
    
print(f"Fichier '{filename}' créé avec succès !")