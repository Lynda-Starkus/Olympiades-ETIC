import pandas as pd 


df = pd.DataFrame(columns=['entreprise', 'contact', 'numero'])

df.to_csv("database_contacts.csv")