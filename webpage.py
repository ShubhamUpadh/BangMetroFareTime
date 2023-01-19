# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 23:46:10 2022

@author: 91995
"""
import dash
import dash_bootstrap_components as dbc
from dash import html, Input, Output, dcc
import networkx as nx
import matplotlib.pylab as plt

pathLength = 0

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

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = dict()

        for start, end in self.edges:
            ''' 
            if start in self.graph_dict:
                self.graph_dict[start].append(end)

            elif end in self.graph_dict:
                self.graph_dict[end].append(start)

            elif end not in self.graph_dict:
                self.graph_dict[end] = [start]

            elif start not in self.graph_dict:
                self.graph_dict[start] = [end]


            '''
            if self.graph_dict.get(start, "DNE") != "DNE":  # and end not in self.graph_dict[start]:
                (self.graph_dict[start]).append(end)

            if self.graph_dict.get(end, "DNE") != "DNE":  # and start not in self.graph_dict[end]:
                (self.graph_dict[end]).append(start)

            if self.graph_dict.get(start, "DNE") == "DNE":
                self.graph_dict[start] = [end]

            if self.graph_dict.get(end, "DNE") == "DNE":
                self.graph_dict[end] = [start]

    def printEdges(self):
        count = 0
        for key in self.graph_dict:
            count += 1
            print(f"Station {count} = {key} is connected with = {self.graph_dict[key]}", end=" \n")
        # print(self.graph_dict)

    def bfsPath(self, start, goal):

        explored = []

        # Queue for traversing the
        # graph in the BFS
        queue = [[start]]

        # If the desired node is
        # reached
        if start == goal:
            print("Same Node")
            return 1

        # Loop to traverse the graph
        # with the help of the queue
        while queue:
            path = queue.pop(0)
            node = path[-1]

            # Condition to check if the
            # current node is not visited
            if node not in explored:
                neighbours = self.graph_dict[node]

                # Loop to iterate over the
                # neighbours of the node
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    global pathLength
                    pathLength = pathLength + 1
                    # Condition to check if the
                    # neighbour node is the goal
                    if neighbour == goal:
                        print("Shortest path = ", *new_path)
                        return len(new_path)
                explored.append(node)

        # Condition when the nodes
        # are not connected
        print("So sorry, but a connecting" \
              "path doesn't exist :(")
        return len(new_path)

    def fareCalc(self, numstations):
        numstations = numstations - 1
        stationsTravelled = {
            0: 10, 1: 10, 2: 15, 3: 15, 4: 18, 5: 20, 6: 22, 7: 25, 8: 28, 9: 30, 10: 30, 11: 35, 12: 35, 13: 38,
            14: 40, 15: 42, 16: 45, 17: 45, 18: 50, 19: 50, 20: 52, 21: 55, 22: 58, 23: 60, 24: 60
        }
        return stationsTravelled[numstations]


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
            dbc.Col(width=4),
            dbc.Col(html.Div(dcc.Dropdown(
                options=stationsList,
                value="Select from station", searchable=True, id="fromStation"
            ), style={'textAlign': 'left'}), width=4),
            dbc.Col(width=4)
        ]),

        dbc.Row([html.Div(html.B("To Station : "),
                          style={'fontSize': 20, 'color': '#FFF', 'textAlign': 'center',
                                 'marginBottom': 10, 'marginTop': 20})
                 ]),

        dbc.Row([
            dbc.Col(width=4),
            dbc.Col(html.Div(dcc.Dropdown(
                options=stationsList,
                value="Select to station", searchable=True, id="toStation"
            ), style={'textAlign': 'left'}), width=4),
            dbc.Col(width=4)
        ]),

        html.Hr(style={'color': "#000", 'marginTop': 20, 'marginBottom': 20}),

        dbc.Row([
            dbc.Col(width=1),
            dbc.Col(html.Div(id="my-output"), style={'textAlign': 'center', 'color': '#FFFFFF','fontSize': 30}, width=10),
            dbc.Col(width=1)
        ]),

        html.Br()

    ])

])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    [Input(component_id='fromStation', component_property='value'),
     Input(component_id='toStation', component_property='value')]
)
def update_output_div(fromst, tost):
    if fromst == "Select from station" or tost == "Select to station":
        return "No station selected"

    routes = [
        ("Majestic", "Mantri Square Sampige"),
        ("Mantri Square Sampige", "Srirampura"),
        ("Majestic", "Chikpet"),
        ("Central College", "Majestic"),
        ("KSR Bengaluru Railway Junction", "Majestic"),
        ("KSR Bengaluru Railway Junction", "Magadi Road"),
        ("Baiyappanahalli", "Swami Vivekananda Road"),
        ("Swami Vivekananda Road", "Indiranagar"),
        ("Indiranagar", "Halasuru"),
        ("Halasuru", "Trinity"),
        ("Trinity", "M.G. Road"),
        ("M.G. Road", "Cubbon Park"),
        ("Cubbon Park", "Vidhana Soudha"),
        ("Vidhana Soudha", "Central College"),
        ("Magadi Road", "Hosahalli"),
        ("Hosahalli", "Vijayanagar"),
        ("Vijayanagar", "Attiguppe"),
        ("Attiguppe", "Deepanjali Nagar"),
        ("Deepanjali Nagar", "Mysore Road"),
        ("Nagasandra", "Dasarahalli"),
        ("Jalahalli", "Dasarahalli"),
        ("Jalahalli", "Peenya Industry"),
        ("Goreguntepalaya", "Peenya"),
        ("Peenya", "Peenya Industry"),
        ("Goreguntepalaya", "Yeshwanthpur"),
        ("Yeshwanthpur", "Sandal Soap Factory"),
        ("Sandal Soap Factory", "Mahalaxmi"),
        ("Mahalaxmi", "Rajajinagar"),
        ("Rajajinagar", "Kuvempu Road"),
        ("Kuvempu Road", "Srirampura"), ("Mantri Square Sampige", "Srirampura"),
        ("Chikpet", "K.R. Market"), ("K.R. Market", "National College"),
        ("National College", "Lalbagh"), ("Lalbagh", "South End Circle"),
        ("South End Circle", "Jayanagar"), ("Jayanagar", "R.V. Road"),
        ("R.V. Road", "Banashankari"), ("Banashankari", "JP Nagar"), ("JP Nagar", "Yelechenhalli")
    ]

    metroRoute = Graph(routes)
    k = metroRoute.bfsPath(fromst, tost)
    fare = f"The fare between {fromst} and {tost} is Rs {metroRoute.fareCalc(k)}"
    return fare


if __name__ == "__main__":
    app.run_server(debug=True)
