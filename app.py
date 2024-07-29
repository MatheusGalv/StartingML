import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data/pizzas.csv")

modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x, y)

st.markdown("<h1 style='text-align: center;'>Prevendo valor de uma pizza</h1>", unsafe_allow_html=True)
st.divider()

diametro = st.number_input("Digite o tamnho do diâmetro da pizza: ")

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"O valor da pizza com diâmetro de {diametro:.2f}cm é de R${preco_previsto:.2f}")