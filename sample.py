import dash
import dash_cytoscape as cyto
import dash_html_components as html
import pickle
import math
from dash.dependencies import Input, Output, State
import dash_core_components as dcc


# Load extra layouts
cyto.load_extra_layouts()


app = dash.Dash(__name__)

# Load elements
pickleFile = open("pickle.txt", 'rb')
test = pickle.load(pickleFile)
pickleFile.close()


app.layout = html.Div([
cyto.Cytoscape(
    id='cytoscape-layout-4',
    elements=test,
    style={'width': '100%', 'height': '800px'},
    layout={
        'name': 'dagre'
    },
    stylesheet=[
        # Group selectors
        {
            'selector': 'node',
            'style': {
                'content': 'data(label)'
            }
        },

        # Class selectors
        {
            'selector': '.red',
            'style': {
                'background-color': 'red',
                'line-color': 'red'
            }
        }
    ]
)
])


if __name__ == '__main__':
    app.run_server(debug=True)
