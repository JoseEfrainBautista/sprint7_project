'''Importamos las librerías necesarias para leer el dataset y graficar los datos'''
import plotly.express as px
import streamlit as st
import pandas as pd

# Tratamos de leer los datos del dataset, controlando si el archivo existe
RUTA = 'vehicles_us.csv'
try:
    df_car_data = pd.read_csv(RUTA)
except FileNotFoundError:
    print("El archivo vehicle_data.csv no se encuentra en el directorio actual.")
else:
    print("El archivo vehicle_data.csv se ha cargado correctamente.")

# Eliminamos los datos nulos de la columna model_year
df_car_data = df_car_data.dropna(subset=['model_year'])

# Convertimos la columna model_year a entero
df_car_data['model_year'] = df_car_data['model_year'].astype(int)

# Crear encabezado para la aplicación en Streamlit
st.header('Análisis exploratorio de datos - Vehículos en venta')

# Crear una casilla de verificación
build_histogram = st.checkbox('Construir histograma')

# Funcionalidad del checkbox para crear un histograma
if build_histogram:
    # Escribir un mensaje
    st.write('Construir un histograma por odómetro')
    # Crear el histograma
    fig = px.histogram(df_car_data, x='odometer')
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear botón para construir un gráfico de dispersión
build_dispersion = st.checkbox(
    'Construir gráfico de dispersión de odómetro y precio')

# Funcionalidad del checkbox para crear un gráfico de dispersión
if build_dispersion:
    # Escribir un mensaje
    st.write('Construir gráfico de dispersión por odómetro y precio')
    # Crear el gráfico de dispersión
    fig = px.scatter(df_car_data, x='odometer', y='price')
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear botón para construir un gráfico de barras
build_bar = st.checkbox('Construir gráfico de barras')

# Funcionalidad del checkbox para crear un gráfico de barras
if build_bar:
    # Escribir un mensaje
    st.write('Construir gráfico de barras de los carros en venta por decada')
    # Carros por decada
    df_car_data['decade'] = (df_car_data['model_year'] // 10) * 10
    decade_counts = df_car_data['decade'].value_counts().sort_index()
    # Creamos un gráfico de barras
    fig = px.bar(decade_counts, x=decade_counts.index, y=decade_counts.values,
                 labels={'x': 'Década', 'y': 'Número de vehículos'},
                 title='Número de vehículos en venta por década')
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
