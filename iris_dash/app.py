from dash import Dash, html, dcc
import dash
app = Dash(__name__, use_pages=True)

app.layout = html.Div([
html.H1("Application Multi-Pages", style={"textAlign": "center"}),
html.Div([
dcc.Link(page["name"], href=page["path"], style={"textDecoration": "none",
    "color": "black",
    "fontSize": "18px",
    "margin": "0 20px",
    "fontWeight": "bold"})
for page in dash.page_registry.values()
],style={"textAlign": "center"}),
html.Hr(),
dash.page_container
])
if __name__ == "__main__":
 app.run(debug=True)