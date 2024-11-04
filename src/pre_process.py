import pandas as pd

def preprocess_data(file_path):
    df = pd.read_csv(file_path)

    total_purchase_value = df.groupby("client_id")["purchase_value"].sum().reset_index()

    favorite_category = df.groupby(["client_id", "category"]).size().reset_index(name="freq")
    favorite_category = favorite_category.loc[favorite_category.groupby("client_id")["freq"].idxmax()].reset_index(drop=True)
    
    first_purchase_date = df.groupby("client_id")["purchase_date"].min().reset_index()
    last_purchase_date  = df.groupby("client_id")["purchase_date"].max().reset_index()
    
    unique_info = df.drop_duplicates(subset="client_id")[["client_id", "name", "email", "age", "gender", "location"]]

    final_df = pd.merge(unique_info, total_purchase_value, on='client_id')
    final_df = pd.merge(final_df, favorite_category[['client_id', 'category']], on='client_id')
    final_df = pd.merge(final_df, first_purchase_date, on='client_id')
    final_df = pd.merge(final_df, last_purchase_date, on='client_id')

    final_df.columns = ['client_id', 'name', 'email', 'age', 'gender', 'location', 'total_purchase_value', 'favorite_category', 'first_purchase_date', 'last_purchase_date']

    return final_df


result = preprocess_data("data/ebook_store.csv")
result.to_csv("data/ebook_store_preprocessed.csv", index=False)

print('Pré-processamento concluído e arquivo salvo como ebook_store_preprocessed.csv')

