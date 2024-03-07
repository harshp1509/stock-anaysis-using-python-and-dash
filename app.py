from dash import Dash,html,dcc
import plotly.express as px
import pandas as pd

app=Dash(__name__)

app.layout=html.Div([
    html.Div([]),
html.Div([
    dcc.Input(id='input-on-submit', type='text',style={'flex':'1','padding':'10px'})
    ]),
html.Div([dcc.Dropdown(['1D','5D','1M','3M','6M','YTD','1Y','2Y','5Y','MAX'],
                 '1D', 
                 id='duration-selection',
                 style={'flex':'1','padding':'10px'}
                 )
    ]),
html.Div([ html.Button('Submit',id='submit-val',n_clicks=0,style={'flex':'1','padding':'10px'})])
],
style={'display':'flex', 'border': '1px solid #000'})

    
   


if __name__ =='__main__':
    app.run(debug=True)

