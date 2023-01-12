import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from plotly import graph_objects as go
import pandas as pd

app = dash.Dash(
    __name__,
)
server = app.server

df = pd.read_csv("./data/weatherHistory.csv")

app.layout = html.Div(
    [
        html.Div(
            [
                html.H2(
                    "Weather analysis",
                    style={
                        "display": "inline",
                        "float": "left",
                        "font-size": "2.65em",
                        "margin-left": "7px",
                        "font-weight": "bolder",
                        "font-family": "Product Sans",
                        "color": "rgba(117, 117, 117, 0.95)",
                        "margin-top": "15px",
                        "margin-bottom": "0",
                    },
                ),
            ]
        ),
        dcc.Dropdown(
            id="weather_feature_input",
            options=["Temperature (C)", "Humidity", "Wind Speed (km/h)"],
            value=[],
            multi=True,
        ),
        dcc.Checklist(
            ["Feature distribution", "Mean feature heatmap", "Mean feature line plot"],
            inline=True,
            id="checklist",
        ),
        html.Div(id="graphs"),
    ],
    className="container",
)


def preprocess_data(df: pd.DataFrame):
    df["Formatted Date"] = pd.to_datetime(df["Formatted Date"], utc=True)
    df = df.sort_values(by="Formatted Date")
    df["month"] = df["Formatted Date"].dt.month
    df["year"] = df["Formatted Date"].dt.year
    return df


def resample_data(df: pd.DataFrame):
    df = df.set_index("Formatted Date")
    df = df.resample("M").mean()
    return df


@app.callback(
    dash.dependencies.Output("graphs", "children"),
    [
        dash.dependencies.Input("weather_feature_input", "value"),
        dash.dependencies.Input("checklist", "value"),
    ],
)
def update_graph(features, checklist):
    graphs = []
    if not features:
        graphs.append(
            html.H3(
                "Select a feature to display.",
                style={"marginTop": 20, "marginBottom": 20},
            )
        )
    else:
        for feature in features:
            preprocessed_df = preprocess_data(df)
            preprocessed_df = resample_data(preprocessed_df)
            figures = []
            if checklist is not None:
                if "Feature distribution" in checklist:
                    histogram_fig = px.histogram(
                        x=df[feature], nbins=20, title="Distribution of " + feature
                    )
                    figures.append(histogram_fig)

                if "Mean feature line plot" in checklist:
                    line_fig = px.line(
                        x=preprocessed_df.index,
                        y=preprocessed_df[feature],
                        title="Line plot of Mean " + feature + " value per month",
                    )
                    line_fig.update_xaxes(
                        rangeslider_visible=True,
                        rangeselector=dict(
                            buttons=list(
                                [
                                    dict(
                                        count=1,
                                        label="1m",
                                        step="month",
                                        stepmode="backward",
                                    ),
                                    dict(
                                        count=6,
                                        label="6m",
                                        step="month",
                                        stepmode="backward",
                                    ),
                                    dict(
                                        count=1,
                                        label="1y",
                                        step="year",
                                        stepmode="backward",
                                    ),
                                    dict(step="all"),
                                ]
                            )
                        ),
                    )
                    figures.append(line_fig)

                if "Mean feature heatmap" in checklist:
                    heatmap_data = [
                        go.Heatmap(
                            x=preprocessed_df["year"],
                            y=preprocessed_df["month"],
                            z=preprocessed_df[feature],
                            colorscale="Jet",
                        )
                    ]
                    layout = go.Layout(
                        title="Heatmap of Mean " + feature + " value per month",
                        xaxis={"title": "Day"},
                        yaxis={"title": "Time"},
                    )
                    heatmap_fig = go.Figure(data=heatmap_data, layout=layout)
                    figures.append(heatmap_fig)
            else:
                graphs.append(
                    html.H3(
                        "Select a plot to display.",
                        style={"marginTop": 20, "marginBottom": 20},
                    )
                )
            if len(figures) > 0:
                for figure in figures:
                    graphs.append(dcc.Graph(id=feature, figure=figure))
    return graphs


if __name__ == "__main__":
    app.run_server(debug=True)
