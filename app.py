import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import seaborn as sns

tips = sns.load_dataset('tips')
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1('Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    html.Div(children = [
    
    html.Div([
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': tips['smoker'], 'y': tips['tip'], 'type': 'box', 'name': 'smoker'},
                {'x': tips['sex'], 'y': tips['tip'], 'type': 'violin', 'name': 'sex'}
            ],
            'layout': {
                'title': 'Tips Dash Data Visualization'
            }
        }
    )
    ], className = 'col-4'),
    # import plotly.graph_objs as go
    html.Div(children = dcc.Graph(
                id = 'graph-scatter',
                figure = {'data': [
                    go.Scatter(
                        x = tips[tips['day'] == i]['tip'],
                        y = tips[tips['day'] == i]['total_bill'],
                        mode='markers',
                        name = 'Day {}'.format(i)
                        ) for i in tips['day'].unique()
                    ],
                    'layout':go.Layout(
                        xaxis= {'title': 'Tip'},
                        yaxis={'title': ' Total Bill'},
                        title= 'Tips Dash Scatter Visualization',
                        hovermode='closest'
                    )
                }
            ), className = 'col-5'),

    html.Div(children = dcc.Graph(
        id = 'pie chart',
        figure = {
            'data':[
        go.Pie(labels = [i for i in tips['sex'].unique()], 
        values= [tips[tips['sex'] == i]['tip'].mean() for i in tips['sex'].unique()]
        )],
        'layout': go.Layout(title = 'Tip mean divided by Sex')}
    ), className = 'col-3')

    ], className = 'row')
])

if __name__ == '__main__':
    app.run_server(debug=True)