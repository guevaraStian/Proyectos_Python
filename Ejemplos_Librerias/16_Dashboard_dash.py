# En este programa se muestra un ejemplo de un dashboard 
# en este tablero se muestra informacion relacionada a la vida y el pib de un pais
# Primero se instala dash con el siguiente comando "pip install dash"
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Crear la aplicación Dash
app = dash.Dash(__name__)

# Cargar datos de ejemplo
df = px.data.gapminder().query("year == 2007")

# Crear un gráfico interactivo
figura = px.scatter(
    df,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
    title="Esperanza de vida vs PIB per cápita (2007)"
)

# Definir el layout del dashboard
app.layout = html.Div([
    html.H1("Dashboard en Python con Dash", style={"textAlign": "center"}),
    html.P("Visualización de datos del mundo - Gapminder", style={"textAlign": "center"}),
    dcc.Graph(id="grafico", figure=figura)
])

# Iniciar el servidor
if __name__ == '__main__':
    app.run(debug=True)