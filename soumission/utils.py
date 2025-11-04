import csv

def soumission_csv(model,df_data,indexes,filename="../data/prediction.csv"):
    """
    Génère un fichier csv de predictions reponse à soumettre à partir d'un model entrainé et d'un data_frame.
        
    Paramètres :
    - model, model entrainé 
    - df_data : data frame des données à predir, dois contenir la colone "ID" et les meme features que le model entrainé
    - filename : nom du fichier créé par la fonction
        
    Retour :
    - X_train_pca, X_test_pca : listes de matrices transformées
    - pca_list : liste des objets PCA par état
    - top_features_dict : dict avec top features par état
    """
    features = df_data.drop(columns=["ID"], errors='ignore')

    prediction = model.predict(features)

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "TARGET"])  # En-têtes
        for index,id in enumerate(indexes) :
            writer.writerow([id, prediction[index]])
    print(f"Fichier '{filename}' créé avec succès !")
    return