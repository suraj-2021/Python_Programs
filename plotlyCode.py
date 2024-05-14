# Import required libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

# Initialize the app
app = dash.Dash(__name__)

# Define the app
app.layout = html.Div(children=[
    html.H1(children='Simple Plotly Dash App'),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                go.Scatter(
                    x = np.random.randint(10, size=10), # random x values
                    y = np.random.randint(10, size=10), # random y values
                    mode = 'lines', # line plot
                    name = 'Random Data'
                )
            ],
            'layout': go.Layout(
                title='Random Line Plot',
                xaxis=dict(title='X Axis'),
                yaxis=dict(title='Y Axis'),
            )
        }
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
