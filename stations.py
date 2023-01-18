import networkx as nx
import matplotlib.pylab as plt

pathLength = 0


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
        numstations = numstations -1
        stationsTravelled = {
            0: 10, 1: 10, 2: 15, 3: 15, 4: 18, 5: 20, 6: 22, 7: 25, 8: 28, 9: 30, 10: 30, 11: 35, 12: 35, 13: 38,
            14: 40, 15: 42, 16: 45, 17: 45, 18: 50, 19: 50, 20: 52, 21: 55, 22: 58, 23: 60, 24: 60
        }
        return stationsTravelled[numstations]



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
    # metroRoute.printEdges()
    # print(routeStations,"\n",len(routeStations))
    k = metroRoute.bfsPath("Peenya Industry", "Peenya")
    print(metroRoute.fareCalc(k))
'''
    G = nx.Graph(metroRoute.graph_dict)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos,connectionstyle="Bar")
    nx.draw_networkx_labels(G, pos,font_size=5)
    plt.show()
'''
# metroRoute.printEdges()
