import dash
from dash import html, dcc, Output, Input
import plotly.express as px

df = px.data.iris()

dash.register_page(__name__, path="/scatterplot")

layout = html.Div([

    html.H2("Scatter Plot : Sepal Length vs Petal Length"),

    dcc.Dropdown(
        id="species-dropdown",
        options=[{"label": s, "value": s} for s in df["species"].unique()],
        value="setosa",
        clearable=False
    ),

    dcc.Graph(id="scatter-graph")
])

@dash.callback(
    Output("scatter-graph", "figure"),
    Input("species-dropdown", "value")
)
def update_scatter(species):
    filtered_df = df[df["species"] == species]

    fig = px.scatter(
        filtered_df,
        x="sepal_length",
        y="petal_length",
        title=f"Espèce : {species}"
    )
    return fig
