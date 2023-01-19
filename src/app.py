#imports
import os
import pathlib

import dash

from dash import dcc
from dash import html


import dash_bootstrap_components as dbc
# import dash_core_components as dcc
# import dash_html_components as html
from dash.dependencies import Input, Output, State

import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
import numpy as np


#--------------------------------------------------------------------------------------------


#create (dash object) the app
app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.SUPERHERO] #SUPERHERO, BOOTSTRAP
)
server = app.server
app.title = "Life SuperHero LCA/LCC"
# app._favicon = "logo-life-superhero-menu.png"

APP_PATH = str(pathlib.Path(__file__).parent.resolve())

#--------------------------------------------------------------------------------------------

# leggi tabella excel
# df = pd.read_excel('data.xlsx')

#--------------------------------------------------------------------------------------------

# definizione elementi dash
# navbar, checklis, dropdown, tabelle

def navbar():
    return dbc.Navbar(
        dbc.Container([
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=app.get_asset_url("logo-life-superhero-menu.png"), height="50px")),
                        # dbc.Col(dbc.NavbarBrand("Life SuperHERO Tool")),
                    ],
                ),
                href="https://www.lifesuperhero.eu/it/",
                style={
                    "textDecoration": "none",
                },
            ),
        ]
    ),
    color="dark",
    dark=True,
)

#--------------------------------------------------------------------------------------------

def tab():
    return html.Div([
        dcc.Tabs(
            id="tabs-styled-with-props", 
            value='tab-2',
            className="custom-tabs",
            children=[
                dcc.Tab(
                    id='tab_1',
                    label='Roof Types',
                    value='tab-1',
                    className="custom-tab",
                    selected_className="custom-tab--selected"
                ),
                dcc.Tab(
                    id='tab_2',
                    label='LCC',
                    value='tab-2',
                    className="custom-tab",
                    selected_className="custom-tab--selected"
                ),
                dcc.Tab(
                    id='tab_3',
                    label='LCA',
                    value='tab-3',
                    className="custom-tab",
                    selected_className="custom-tab--selected"
                ),
            ],
        ),
    html.Div(id='tabs-content-props')
])

#--------------------------------------------------------------------------------------------

# inputdata_name = ['Years', 'Nominal Interest Rate', 'Inflation', 'Nominal Wage GDP', 'Electricity Price Growth']

def data_box():
    return html.Div([
        html.Hr(),
        html.H5(
            children='Macroeconomical Input Data',
            style={'text-align' : 'center'}
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H6('Years'),
                        dcc.Input(
                            id='input_data1',
                            type='number',
                            value=15,
                            min=0,
                            max=50,
                            step=1,
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        html.H6('Nominal Interest Rate'),
                        dcc.Input(
                            id='input_data2',
                            type='number',
                            value=0.04,
                            min=0,
                            max=1,
                            step=0.01
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        html.H6('Inflation'),
                        dcc.Input(
                            id='input_data3',
                            type='number',
                            value=0.02,
                            min=0,
                            max=1,
                            step=0.01
                        ),
                    ]
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H6('Nominal Wage GDP'),
                        dcc.Input(
                            id='input_data4',
                            type='number',
                            value=0.01,
                            min=0,
                            max=1,
                            step=0.01
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        html.H6('Electricity Price Growth'),
                        dcc.Input(
                            id='input_data5',
                            type='number',
                            value=0.05,
                            min=0,
                            max=1,
                            step=0.01
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        html.H6('Service Life [years]'),
                        dcc.Input(
                            id='input_data6',
                            type='number',
                            value=10,
                            min=0,
                            max=50,
                            step=1
                        ),
                    ]
                ),
            ]
        ),
        html.Hr(),
        html.H5(
            children='Costs Input Data',
            style={'text-align' : 'center'}
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H6('Initial Investment Cost [€]'),
                        dcc.Input(
                            id='input_data7',
                            type='number',
                            value=40.42,
                            min=0,
                            max=10000,
                            step=0.01,
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        html.H6('Annual Maintenance Cost [€/years]'),
                        dcc.Input(
                            id='input_data8',
                            type='number',
                            value=0.88,
                            min=0,
                            max=10000,
                            step=0.01
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        html.H6('Energy Efficiency [-]'),
                        dcc.Input(
                            id='input_data9',
                            type='number',
                            value=1,
                            min=0,
                            max=50,
                            step=0.01
                        ),
                    ]
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H6('Cooling Consumption (pre) [kWh/year]'),
                        dcc.Input(
                            id='input_data10',
                            type='number',
                            value=100.63,
                            min=0,
                            max=10000,
                            step=0.01,
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        html.H6('Cooling Consumption (post) [kWh/year]'),
                        dcc.Input(
                            id='input_data11',
                            type='number',
                            value=16.47,
                            min=0,
                            max=10000,
                            step=0.01
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        html.H6('Energy Tariff [€/kWh]'),
                        dcc.Input(
                            id='input_data12',
                            type='number',
                            value=0.186,
                            min=0,
                            max=50,
                            step=0.001
                        ),
                    ]
                ),
            ]
        ),
        html.Hr(),
        html.Div(id="number-out"),
    ],
    style={
        'text-align' : 'center',
    },
)

@app.callback(
    Output("number-out", "children"),
    [Input("input_data1", "value"),
    Input("input_data2", "value"),
    Input("input_data3", "value"),
    Input("input_data4", "value"),
    Input("input_data5", "value"),
    Input("input_data6", "value"),
    Input("input_data7", "value"),
    Input("input_data8", "value"),
    Input("input_data9", "value"),
    Input("input_data10", "value"),
    Input("input_data11", "value"),
    Input("input_data12", "value")]
)  

def number_render(input_data1, input_data2, input_data3, input_data4, input_data5, input_data6, input_data7, input_data8, input_data9, input_data10, input_data11, input_data12):
    # return "Anni: {}, Nominal Interest Rate {}, Inflation {}, GDP {}, Electricity Price Growth {}".format(input_data1, input_data2, input_data3, input_data4, input_data5)   
    anni = int('{}'.format((input_data1)))
    itn = float('{}'.format(input_data2))
    pit = float('{}'.format(input_data3))
    gdp = float('{}'.format(input_data4))
    opg = float('{}'.format(input_data5))
    
    sl = float('{}'.format(input_data6))
    ci = float('{}'.format(input_data7))
    cm = float('{}'.format(input_data8))
    nh = float('{}'.format(input_data9))
    pepre = float('{}'.format(input_data10))
    pepost = float('{}'.format(input_data11))
    ent = float('{}'.format(input_data12))

    df = pd.DataFrame(
        {
            'Years' : list(range(1, int('{}'.format(input_data1+1)))),
            'Nominal Interest Rate' : [itn]*anni,
            'Inflation' : [pit]*anni,
            'Nominal Wage GDP' : [gdp]*anni,
            'Electricity Price Growth' : [opg]*anni
        }
    )

    output_data = pd.DataFrame(
        {
            'Real Discount Rate' : (df['Nominal Interest Rate'] - df['Inflation'])/(1+df['Inflation']),
            '(1/1+dt)' : 1/(1+((df['Nominal Interest Rate'] - df['Inflation'])/(1+df['Inflation']))),
            'Discount Factor' : (1/(1+((df['Nominal Interest Rate'] - df['Inflation'])/(1+df['Inflation']))))**df['Years'],
            'Real Wage' : (df['Nominal Wage GDP'] - df['Inflation'])/(1+df['Inflation']),
            '1 + eL' : 1+ (df['Nominal Wage GDP'] - df['Inflation'])/(1+df['Inflation']),
            'Price Dev Rate (Labour)' : (1+ (df['Nominal Wage GDP'] - df['Inflation'])/(1+df['Inflation']))**df['Years'],
            'Real Oil Price Growth' : (df['Electricity Price Growth'] - df['Inflation'])/(1+df['Inflation']),
            '1 + eE' : 1+(df['Electricity Price Growth'] - df['Inflation'])/(1+df['Inflation']),
            'Price Dev Rate (Energy)' : (1+(df['Electricity Price Growth'] - df['Inflation'])/(1+df['Inflation']))**df['Years']
        }
    )

    presentvalue = pd.DataFrame(
        {
            'Annual Energy Cost' : [((pepost/nh)*ent)]*anni,
            'Present Value Energy' : ([((pepost/nh)*ent)]*anni)*output_data['Price Dev Rate (Energy)']*output_data['Discount Factor'],
            'Present Value Labour' : ([cm]*anni)*output_data['Price Dev Rate (Labour)']*output_data['Discount Factor']
        }
    )

    costs = pd.DataFrame(
        {
            'Initial Investment [€]' : [0]*anni,
            'Annual Maintenance cost [€/year]' : presentvalue['Present Value Labour'],
            'Replacement Costs [€]' : ([0]*anni)*output_data['Discount Factor']*output_data['Price Dev Rate (Labour)'],
            'Savings [€]' : ((pepre-pepost)*ent)*output_data['Discount Factor']*output_data['Price Dev Rate (Energy)'],
        }
    )
    costs.at[0, 'Initial Investment [€]']=ci
    i=0
    while sl*i <= anni-1:
        costs.at[sl*(i), 'Replacement Costs [€]']=ci
        i += 1
    costs.at[0, 'Replacement Costs [€]']=0
    costs.at[0, 'Savings [€]']=0

    pbp = pd.DataFrame(
        {
            'Payback Period' : (costs['Initial Investment [€]']+costs['Annual Maintenance cost [€/year]']+costs['Replacement Costs [€]'])-costs['Savings [€]']
        }
    )
    pbp2 = pd.concat([df['Years'], pbp.cumsum()], axis=1)
    fig = go.Figure(
        [
            go.Bar(
                x = pbp2['Years'].values.tolist(),
                y = pbp2['Payback Period'].values.tolist(),
            )
        ]
    )
    fig.update_layout(
        plot_bgcolor='#1E2130', 
        paper_bgcolor='#1E2130',
        font_color='white',
        font_size=15,
    )

    presentvalue_energy = presentvalue['Present Value Energy'].sum()
    presentvalue_labour = presentvalue['Present Value Labour'].sum()
    global_cost = ci+presentvalue_energy+presentvalue_labour

    return html.Div(
        [
            html.H4('Global Cost'),
            html.H4(global_cost.round(3)),
            html.Hr(),
            html.H4('Payback Period'),
            dbc.Table.from_dataframe(pbp2.T.reset_index().round(3), striped=True, bordered=True, hover=True, header=0),
            dcc.Graph(figure=fig),
            html.Hr(),
            html.H4('Input Macroeconomical Data'),
            dbc.Table.from_dataframe(df.T.reset_index(), striped=True, bordered=True, hover=True, header=0),
            html.Hr(),
            html.H4('Output Macroeconomical Data'),
            dbc.Table.from_dataframe(output_data.T.reset_index().round(3), striped=True, bordered=True, hover=True, header=0),
            html.Hr(),
            html.H4('Present Values'),
            dbc.Table.from_dataframe(presentvalue.T.reset_index().round(3), striped=True, bordered=True, hover=True, header=0),
            html.Hr(),
            html.H4('Costs and Savings'),
            dbc.Table.from_dataframe(costs.T.reset_index().round(3), striped=True, bordered=True, hover=True, header=0),
        ]
    )

#--------------------------------------------------------------------------------------------

app.layout = html.Div([
    navbar(),
    # html.H4(
    #     children='Life SuperHERO Tool',
    #     style={'text-align' : 'center'}
    # ),
    tab(),
])

#--------------------------------------------------------------------------------------------

@app.callback(
    Output('tabs-content-props', 'children'),
    Input('tabs-styled-with-props', 'value')
)

def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H4(
                children='Life SuperHERO Tool - TAB1',
                style={'text-align' : 'center'}
            ),
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H4(
                children='Life Cycle Cost',
                style={'text-align' : 'center'}
            ),
            data_box()
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H4(
                children='Life SuperHERO Tool - TAB3',
                style={'text-align' : 'center'}
            ),
        ])


#--------------------------------------------------------------------------------------------

#run app
if __name__ == '__main__':
    app.run_server(debug=True)