import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

prom = pd.read_csv("datospromedio.csv")
st.title("Indicadores del Promedio de notas en la Universidad")
tab1, tab2 = st.tabs(["Análisis Univariado", "Análisis Bivariado"])

with tab1:
    fig, ax = plt.subplots(1, 4, figsize=(10, 4))
    #promediouni
    ax[0].hist(prom["colGPA"])
    #edad
    ax[1].hist(prom["age"])
    #genero
    conteo = prom["male"].value_counts()
    ax[2].bar(conteo.index, conteo.values)
    #Acceso a PC
    conteo = prom["PC"].value_counts()
    ax[3].bar(conteo.index, conteo.values)
    fig.tight_layout()
    st.pyplot(fig)

with tab2:
    fig, ax = plt.subplots(1, 3, figsize=(10, 4))
    #edad vs promedionotas
    sns.scatterplot(data=prom, x="age", y="colGPA", ax=ax[0])
    #genero vs promedionotas
    sns.violinplot(data=prom, x="male", y="colGPA", ax=ax[1])
    #acceso a computador vs promedionotas
    sns.boxplot(data=prom, x="PC", y="colGPA", ax=ax[2])
    fig.tight_layout()
    st.pyplot(fig)

