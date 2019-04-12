import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go




df = pd.read_csv("bay_area_sample.csv",sep='\t')

col = ['ID', 'Birth_Year', 'Gender', 'Skill_1', 'Skill_1_Weight', 'Skill_2', 'Skill_2_Weight', "City_Of_Profile",
          'Country_Of_Profile', 'Education', 'Elite_Institution', 'Start_Date', 'Valid_Start_Date',
           'End_Date', 'Valid_End_Date', 'Current_Employer', 'Length_At_Job', 'Role', 'Department',
          'Company', 'Normalized_Company', 'Ticker', 'Exchange', 'Publicly_Traded', 'Location_Of_Employment',
           'Industry', 'Education_Flag', 'Degree_Type', 'Elite_Flag', 'Majors', 'Major_Categories' , 'Unknown1', 'Unknown2']
df.columns = col
df['Gender'] = df['Gender'].replace({0:'Unknown', 1:'Female', 2:'Male'})
df['Education'] = df['Education'].replace({0: 'Unknown', 1:'High School', 2:'Vocational Degree', 3:'Associate', 4:'Bachelor', 5:'Masters', 6:'MBA', 7:'PHD/JD/MD'})

app = dash.Dash(__name__)

opt1 = [{'label':i,'value':i} for i in df['Gender'].unique()]



app.layout = html.Div([

    html.Div([
        html.H1('Employment Dynamics in the Bay Area'),

        html.Div([
            dcc.Dropdown(
                id='selected_gender',
                options=opt1,
            )], style={'width': '48%', 'display': 'inline-block'}),

        dcc.Graph(id='my-graph') ])
])




@app.callback(Output('my-graph','figure'),
                      [Input('selected_gender','value')]
)
def callbackForDropdown(gender):
    dff = df[df['Gender'] == gender]

    trace1 = go.Bar( x=dff['Education'].value_counts() )

    return {
        'data': [trace1],
        'layout': go.Layout(

            title=f'Education Level: {gender}',
            colorway=["#EF963B", "#EF533B"],
            hovermode='closest',
            xaxis={
                'title': 'Education Level',
                'titlefont': {
                    'color': 'black',
                    'size': 14},
                'tickfont': {
                    'size': 9,
                    'color': 'black'

                }
            },
            yaxis={
                'title': 'Number of People',
                'titlefont': {
                    'color': 'black',
                    'size': 14,

                },

                'tickfont': {
                    'color': 'black'

                }
            }
        )

    }


server = app.server

if __name__== '__main__':
    app.run_server(debug=True)
