# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 23:46:10 2022

@author: 91995
"""
import dash
import dash_bootstrap_components as dbc
from dash import html, Input, Output, dcc

colors = {
    'background': '#000000'
}

borderInf = {
    'Inf': '5px solid gray',
    'Inf1': '1px #898989'
}

textCol = {
    'text': '#FFF'
}

# grad ={
# 'gr': 'linearGradient('red','yellow')'
# }
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

stationsList = ["Attiguppe", "Baiyappanahalli", "Banashankari", "Central College", "Chikpet", "Cubbon Park",
                "Dasarahalli", "Deepanjali Nagar", "Goreguntepalaya", "Halasuru", "Hosahalli", "Indiranagar",
                "Jalahalli", "Jayanagar", "JP Nagar", "K.R. Market", "KSR Bengaluru Railway Junction", "Kuvempu Road",
                "Lalbagh", "M.G. Road", "Magadi Road", "Mahalaxmi", "Majestic", "Mantri Square Sampige", "Mysore Road",
                "Nagasandra", "National College", "Peenya", "Peenya Industry", "R.V. Road", "Rajajinagar",
                "Sandal Soap Factory", "South End Circle", "Srirampura", "Swami Vivekananda Road", "Trinity",
                "Vidhana Soudha", "Vijayanagar", "Yelechenhalli", "Yeshwanthpur"
                ]

app.title = "Bangalore Metro Fare"

app.layout = html.Div(style={'paddingTop': 50}, children=[

    dbc.Container([

        dbc.Row([
            html.Div(html.B("Namma Fare Calculator"), style={'fontSize': 40, 'color': '#FFF', 'textAlign': 'center',
                                                             'marginBottom': 10})

        ]),

        html.Hr(style={'color': "#FFF"}),

        dbc.Row([html.Div(html.B("From Station : "),
                          style={'fontSize': 20, 'color': '#FFF', 'textAlign': 'center',
                                 'marginBottom': 10})
                 ]),

        dbc.Row([
            dbc.Col(width=3),
            dbc.Col(html.Div(dcc.Dropdown(
                options=stationsList,
                value="Select from station", searchable=True, id="fromStation"
            ), style={'textAlign': 'left'}), width=6),
            dbc.Col(width=3)
        ]),

        dbc.Row([html.Div(html.B("To Station : "),
                          style={'fontSize': 20, 'color': '#FFF', 'textAlign': 'center',
                                 'marginBottom': 10, 'marginTop': 20})
                 ]),

        dbc.Row([
            dbc.Col(width=3),
            dbc.Col(html.Div(dcc.Dropdown(
                options=stationsList,
                value="Select to station", searchable=True, id="toStation"
            ), style={'textAlign': 'left'}), width=6),
            dbc.Col(width=3)
        ]),

        dbc.Row([html.Div(html.B("Enter the alphabets that the word SHOULD NOT contain : "),
                          style={'fontSize': 20, 'color': '#FFF', 'textAlign': 'center',
                                 'marginBottom': 5, 'marginTop': 15})
                 ]),

        dbc.Row(
            [html.Div(dcc.Input(id='my-input', value='', type='text'),
                      style={'marginTop': 0, 'textAlign': 'center', 'fontSize': 20, 'color': '#FFF'})
             ]),

        html.Br(),

        dbc.Row([html.Div(html.B("LONGEST POSSIBLE WORD IS : ", id='my-output'),
                          style={'marginTop': 15, 'textAlign': 'center', 'fontSize': 20, 'color': '#FFF'})
                 ]),

    ])

])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    if len(input_value) == 0:
        return "NO INPUT DETECTED"
    z = list()
    for alpha in input_value:
        if alpha.isalpha() and not alpha in z:
            z.append(alpha)

    print(z)

    lenWord = 0
    longestWord = ""

    with open("dictionaryedited1.csv", mode='r') as file:
        fileF = csv.reader(file)
        for lines in fileF:

            flag = True

            for alphabet in z:
                if alphabet.lower() in str(lines) or alphabet.upper() in str(lines):
                    flag = False
                    break

            if flag and lenWord < len(str(lines)):
                longestWord = str(lines)
                lenWord = len(str(lines))

    if longestWord == "":
        return "No such word exists :( "

    else:
        return str(longestWord[2:-2]).upper()


if __name__ == "__main__":
    app.run_server(debug=True)
