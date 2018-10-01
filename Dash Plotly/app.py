import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from categoryplot import getPlot
import numpy as np

from data import dfTitanic, dfTitanicOutlier

table = {
    '1': dfTitanic,
    '2': dfTitanicOutlier,
}

app = dash.Dash(__name__)
server = app.server

app.title = 'Dash Plot Python'


app.layout = html.Div(children=[
    dcc.Tabs(id='tabs', value= 'tab-1',
        style = {
            'fontFamily': 'system-ui'
        },
        content_style = {
            'fontFamily': 'Arial',
            'borderLeft': '1px solid #d6d6d6',
            'borderRight': '1px solid #d6d6d6',
            'borderBottom': '1px solid #d6d6d6',
            'padding': '44px'
        },
        children=[
            dcc.Tab(label='Ujian Titanic Database', value='tab-1', children=[
                html.Div([
                    html.H1(
                        children='Table Titanic',
                        className='h1Tab'
                    ),
                    html.Table([
                    html.Tr([
                        html.Td(html.P('Table: ')),
                        html.Td(
                            dcc.Dropdown(
                                id='ddl-table',
                                options=[{'label': 'Titanic', 'value': '1'},
                                        {'label': 'Titanic Outlier Calculation', 'value': '2'}
                                ],
                                value='1'
                            )
                        )
                    ])
                ], style={'width': '300px'}),
                    html.Div(id='output-table', children=[])
                ])
            ]),
            dcc.Tab(label='Tips 2', value='tab-2', children=[
                html.Div([
                html.H1(
                    children='Categorical Plot Ujian Titanic',
                    className='h1Tab'
                ),
                html.Table([
                    html.Tr([
                        html.Td([
                            html.P('Jenis: '),
                            dcc.Dropdown(
                                id='ddl-jenis-plot-category',
                                options=[{'label': 'Bar', 'value': 'bar'},
                                        {'label': 'Violin', 'value': 'violin'},
                                        {'label': 'Box', 'value': 'box'}
                                ],
                                value='bar'
                            )
                        ]),
                        html.Td([
                            html.P('X Axis: '),
                            dcc.Dropdown(
                                id='ddl-x-plot-category',
                                options=[{'label': 'Survived', 'value': 'survived'},
                                        {'label': 'Sex', 'value': 'sex'},
                                        {'label': 'Ticket Class', 'value': 'class'},
                                        {'label': 'Embark Town', 'value': 'embark_town'},
                                        {'label': 'Who', 'value': 'who'},
                                        {'label': 'Outlier', 'value': 'outlier'}
                                ],
                                value='survived'
                            )
                        ])
                    ])
                ], style={'width': '900px'}),
                dcc.Graph(
                    id='categoricalPlot',
                    figure={
                        'data': []
                    }
                )
            ])
        ])
    ])
],
    style = {
            'maxWidth': '4000px',
            'margin': '0 auto'
        }
)

@app.callback(
    Output('output-table', 'children'),
    [Input('ddl-table', 'value')]
)

def output_table(output):
    return[
            html.P('Jumlah Data: ' + str(len(table[output]))),
            dcc.Graph(
                id='data-table-titanic',
                figure = {
                    'data':[
                            go.Table(
                            columnwidth = [90,500],
                            header=dict(
                                values=['<b>'+ col.capitalize() +'</b>'for col in table[output].columns],
                                fill = dict(color='#a1c3d1'),
                                font=dict(size=14),
                                height=30
                            ),
                            cells=dict(
                                values=[table[output][col] for col in table[output].columns],
                                fill = dict(color='#EDFAFF'),
                                font=dict(size=12),
                                align=['center'],
                                height=30 
                            ))
                        ],
                    'layout': dict(height=500, margin={'l': 40, 'b': 40, 't': 10, 'r': 10})
                }
            )            
    ]

@app.callback(
    Output('categoricalPlot', 'figure'),
    [Input('ddl-jenis-plot-category', 'value'), Input('ddl-x-plot-category', 'value')]
)

def update_category_graph(ddljeniscategory, ddlxcategory):
   return {
       'data': getPlot(ddljeniscategory, ddlxcategory),
       'layout': go.Layout(
                    xaxis={'title': ddlxcategory.capitalize()}, yaxis={'title': 'Fare (US$), Age(Year)'},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 0, 'y': 1}, hovermode='closest',
                    boxmode='group', violinmode='group'
                    # plot_bgcolor= 'black', paper_bgcolor= 'black',
                )
   }

if __name__ == '__main__':
    app.run_server(debug=True, port=2001)