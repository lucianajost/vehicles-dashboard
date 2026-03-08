import pandas as pd
import plotly.express as px
import streamlit as st

# título do dashboard
st.header("Vehicle Sales Dashboard")

# ler os dados
car_data = pd.read_csv("vehicles_us.csv")

# checkbox para histograma
build_histogram = st.checkbox("Criar histograma")

if build_histogram:
    st.write("Criando histograma da quilometragem dos veículos")

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)


# checkbox para scatter plot
build_scatter = st.checkbox("Criar gráfico de dispersão")

if build_scatter:
    st.write("Relação entre preço e quilometragem")

    fig = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig, use_container_width=True)