from dash import Dash, html, dcc, callback, Output, Input
import plotly.graph_objects as go
import pandas as pd
from yfinance_data import yfinance  # Assuming 'yfinance_api' is the name of your yfinance file
import dash_bootstrap_components as dbc


external_stylesheets=[dbc.themes.CERULEAN]
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1("Stock Analysis Dashboard", className='display-5', style={'textAlign': 'center', 'margin-bottom': '20px','color':'black','font-weight': 'bold','font-style': 'italic'}),
    html.Div([
        html.Label("Enter the Name of stock:- "),
        dcc.Input(id='input-on-submit', type='text', className='form-control', style={'width': '150px', 'height': '40px', 'margin-right': '10px'}),
        html.Label("Enter the Duration : "),
        dcc.Dropdown(
            id='duration-selection',
            
            options=[
                {'label': '1 Day', 'value': '1D'},
                {'label': '5 Days', 'value': '5D'},
                {'label': '1 Month', 'value': '1Mo'},
                {'label': '3 Months', 'value': '3Mo'},
                {'label': '6 Months', 'value': '6Mo'},
                {'label': 'Year to Date', 'value': 'YTD'},
                {'label': '1 Year', 'value': '1Y'},
                {'label': '2 Years', 'value': '2Y'},
                {'label': '5 Years', 'value': '5Y'},
                {'label': 'Max', 'value': 'MAX'}
            ],
            value='1D',
            style={'width': '150px', 'height': '40px', 'margin-right': '10px'}
        ),
        html.Label("Enter the interval for candles:- "),
        dcc.Dropdown(
            id='interval-selection',
            options=[
                {'label': '1 hour', 'value': '1h'},
                {'label': '1 day', 'value': '1D'},
                {'label': '1 week', 'value': '1wk'},
            ],
            value='1D',
            style={'width': '150px', 'height': '40px', 'margin-right': '10px'}
        ),
        html.Button('Submit', id='submit-val', className='btn btn-primary', n_clicks=0, style={'width': '100px', 'height': '40px'}),
    ],
        style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'margin-bottom': '20px'}),
    html.Div([
        html.H2(id='stock-name', className='display-5', style={'textAlign': 'center', 'margin-bottom': '20px'}),
        dcc.Graph(id='stock-graph')
    ], style={'margin': '0 auto', 'width': '80%'})
], style={'padding': '20px','background-color': '#a5c2c2'})

@app.callback(
    Output('stock-graph', 'figure'),
    [Input('submit-val', 'n_clicks')],
    [Input('duration-selection', 'value')],
    [Input('interval-selection','value')],
    [Input('input-on-submit', 'value')]
)
def update_graph(n_clicks, duration, interval, stock_name):
    if n_clicks > 0 and stock_name:
        stock_data = yfinance(stock_name).fetch_stock_data(duration, interval)

        fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                             open=stock_data['Open'],
                                             high=stock_data['High'],
                                             low=stock_data['Low'],
                                             close=stock_data['Close'])])
        
        title = stock_name.split(".")[0] 
        fig.update_layout(title=dict(text=f'<a href="https://in.tradingview.com/symbols/{title}">{stock_name.split(".")[0]}</a>', font=dict(size=24, color='white')),
                          xaxis_title=dict(text='Date', font=dict(color='white')),
                          yaxis_title=dict(text='Stock Price', font=dict(color='white')),
                          plot_bgcolor='black', 
                          paper_bgcolor='black',
                          xaxis=dict(showgrid=False,rangebreaks=[dict(values=yfinance(stock_name).list_holiday(duration, interval))]),
                          yaxis=dict(showgrid=False),
                          xaxis_rangeslider_visible=False,
                          )
    

        fig.update_xaxes(tickfont=dict(color='white'))
        fig.update_yaxes(tickfont=dict(color='white'))

        return fig
    else:
        return go.Figure()



if __name__ == '__main__':
    app.run_server(debug=True)
