import dash
from dash import html, dcc, Output, Input
import plotly.express as px

df = px.data.iris()

dash.register_page(__name__, path="/histogramme")

layout = html.Div([

    html.H2("Histogramme de Sepal Length"),

    dcc.Slider(
        id="bins-slider",
        min=5,
        max=50,
        step=1,
        value=10,
        marks={i: str(i) for i in range(5, 55, 5)}
    ),

    dcc.Graph(id="histogramme-graph")
])

@dash.callback(
    Output("histogramme-graph", "figure"),
    Input("bins-slider", "value")
)
def update_histogram(bins):
    fig = px.histogram(
        df,
        x="sepal_length",
        nbins=bins,
        title=f"Histogramme avec {bins} bins"
    )
    return fig
