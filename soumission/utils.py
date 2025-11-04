import csv

def soumission_csv(model,df_data,filename="../data/prediction.csv"):

    indexes = df_data["ID"]
    features = df_data.drop(columns=["ID"], errors='ignore')

    prediction = model.predict(features)

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "TARGET"])  # En-têtes
        for index,id in enumerate(indexes) :
            writer.writerow([id, prediction[index]])
    print(f"Fichier '{filename}' créé avec succès !")
    return