import pandas as pd
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table

app = dash.Dash()

app.layout = html.Div([
    html.H1('Basic Conference Demo'),
     dcc.Slider(
        id='my-slider',
        min=0,
        max=20,
        step=0.1,
        value=1,
        tooltip = { 'always_visible': True }
    ),
    
    dash_table.DataTable(id='table')
])

@app.callback([Output(component_id='table', component_property='data'), 
             Output(component_id='table', component_property='columns')],
            [Input('my-slider', 'value')])
def update_table(user_selection):
    """
    For user selection, return the relevant data 
    """
    df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    df =df[df.sepal_length==user_selection]
    columns = [{'name': col, 'id': col} for col in df.columns]
    data = df.to_dict(orient='records')
    return data, columns

app.run_server()