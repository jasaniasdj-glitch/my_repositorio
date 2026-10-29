
## Análisis de Vehículos Usados
Descripción del proyecto
Este proyecto consiste en el desarrollo de una aplicación web interactiva para el análisis exploratorio de anuncios de vehículos usados en Estados Unidos.

La aplicación permite visualizar información mediante gráficos interactivos creados con Plotly y presentados a través de Streamlit.

## Objetivo
El objetivo es proporcionar una herramienta visual para explorar los datos de vehículos usados y analizar características como el precio, el kilometraje y la condición de los vehículos.

## Conjunto de datos
El proyecto utiliza el archivo:

vehicles_us.csv

## El conjunto de datos contiene información sobre anuncios de vehículos usados, incluyendo:

* Precio
* Año del modelo
* Modelo
* Condición
* Combustible
* Kilometraje
* Transmisión
* Tipo de vehículo
* Color

## Tecnologías utilizadas
Python
Pandas
Plotly Express
Streamlit
Jupyter Notebook
GitHub
Render

## Análisis exploratorio de datos
Se realizó un análisis exploratorio utilizando Jupyter Notebook para:

* Revisar la estructura del conjunto de datos.
* Analizar valores faltantes.
* Obtener estadísticas descriptivas.
* Explorar la distribución de precios.
* Analizar la distribución de kilometraje.
* Evaluar la relación entre precio y kilometraje.
* Visualizaciones incluidas
* Histograma
* Muestra la distribución del kilometraje de los vehículos.

## Visualizaciones incluidas
La aplicación web incluye las siguientes visualizaciones interactivas:

## Histograma
Muestra la distribución del kilometraje (odometer) de los vehículos del conjunto de datos.

## Gráfico de dispersión
Muestra la relación entre el precio y el kilometraje de los vehículos.

## Cómo ejecutar la aplicación
1. Crear un entorno virtual:
python -m venv vehicles_env
2. Activar el entorno virtual:
vehicles_env\Scripts\activate
3. Instalar dependencias:
pip install -r requirements.txt
4. Ejecutar la aplicación:
streamlit run app.py

## Estructura del repositorio 
my_repositorio
│ 
├── app.py 
├── requirements.txt 
├── vehicles_us.csv 
├── EDA.ipynb 
├── README.md 
└── .gitignore

## Aplicación desplegada
La aplicación se encuentra disponible en:

[https://TU-APP.onrender.com](https://my-repositorio.onrender.com)
srv-dbft57a9lscs739fpmo0
https://dashboard.render.com/web/srv-dbft57a9lscs739fpmo0/deploys

## Autor
Araceli Jasania Sanchez
