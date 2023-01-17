import networkx as nx
import matplotlib.pylab as plt


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


if __name__ == "__main__":
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

    G = nx.Graph(metroRoute.graph_dict)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos,connectionstyle="Bar")
    nx.draw_networkx_labels(G, pos,font_size=5)
    plt.show()

    metroRoute.printEdges()
