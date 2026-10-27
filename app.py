import streamlit as st
import pandas as pd
import plotly.express as px

# cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# encabezado
st.header('Análisis de Vehículos Usados')

# casilla para histograma
build_histogram = st.checkbox('Mostrar histograma')

if build_histogram:
    st.write('Histograma del kilometraje de los vehículos')

    fig = px.histogram(
        car_data,
        x='odometer',
        title='Distribución del kilometraje'
    )

    st.plotly_chart(fig)

# casilla para gráfico de dispersión
build_scatter = st.checkbox('Mostrar gráfico de dispersión')

if build_scatter:
    st.write('Relación entre precio y kilometraje')

    fig = px.scatter(
        car_data,
        x='odometer',
        y='price',
        title='Precio vs Kilometraje'
    )

    st.plotly_chart(fig)

