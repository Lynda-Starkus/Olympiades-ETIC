##azizaziza17
##azizaziza18
import streamlit as st
import pandas as pd

st.title("Gestion des contacts ETIC")
st.subheader("Entrez les infos")

df = pd.read_csv('database_contacts.csv')
print(df.drop(columns=df.columns[0], inplace=True))

print(df)

with st.form("form1", clear_on_submit=True):
    entreprise = st.text_input("Entrez le nom de l'entreprise")
    contact = st.text_input("Entrez le nom et prénom du contact de l'entreprise")
    numero = st.number_input("Numéro de téléphone du contact")

    submitted = st.form_submit_button("Ajouter le contact")

    if submitted:
        st.write("Contact ajouté wohoo !")
        list_row = []
        list_row.append(entreprise)
        list_row.append(contact)
        list_row.append(numero)
        df.loc[len(df)] = list_row

df.to_csv("database_contacts.csv")