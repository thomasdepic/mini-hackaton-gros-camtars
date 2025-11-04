import csv

def soumission_csv(model,df_data,filename="prediction"):
    filename = "data/" + filename + ".csv"

    prediction = model.predict(df_data)

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "TARGET"])  # En-têtes
        for id,index in enumerate(df_data["ID"]) :
            writer.writerow([id, prediction[index]])
    print(f"Fichier '{filename}' créé avec succès !")
    return