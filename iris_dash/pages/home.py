import dash
from dash import html
import dash.dash_table as dt
import plotly.express as px

df = px.data.iris()
dash.register_page(__name__, path="/")
layout = html.Div([
    html.H2("table de filter du dataset Iris"),
    dt.DataTable(
        data=df.head().to_dict("records"),
        columns=[{"name": col, "id": col} for col in df.columns],
        page_size=5,
        style_cell={"textAlign": "center"},
        style_table={"overflowX": "auto"}
    )
])