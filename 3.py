class PQueue:
    def __init__(self):
        self.dict = {}
        self.keys = []
        self.sorted = False

    def push(self, k, v):
        self.dict[k] = v
        self.sorted = False

    def _sort(self):
        self.keys = sorted(self.dict, key=self.dict.get, reverse=True) # type: ignore

    def pop(self):
        if not self.sorted:
            self._sort()
        try:
            key = self.keys.pop()
            value = self.dict[key]
            self.dict.pop(key)
            return key, value
        except IndexError:
            return None

def path_costs(path):
    c = {}
    with open(path, 'r') as file:
        for line in file:
            line = line.split(" ")
            v = int(line.pop())
            e1 = line.pop()
            e2 = line.pop()
            print("Value of v, e1, e2:", v, e1, e2)
            if e1 not in c:
                c[e1] = {}
            if e2 not in c:
                c[e2] = {}
            c[e1][e2] = c[e2][e1] = v
    print("C value:", c)
    return c

def a_star(start, goal, heuristics, path_cost):
    frontier = PQueue()
    frontier.push(start, heuristics[start])
    while True:
        path, cost = frontier.pop() # type: ignore
        print(path + " " + str(cost))
        end = path.split("->")[-1]
        cost = cost - heuristics[end]
        if goal == end:
            break
        for node, weight in path_cost[end].items():
            new_cost = cost + weight + heuristics[node]
            new_path = path + "->" + node
            frontier.push(new_path, new_cost)


graph_file_path = 'C:\\Users\\DELL\\graph.txt'
heuristics = {
    'Arad': 366,
    'Zerind': 374,
    'Oradea': 380,
    'Sibiu': 253,
    'Fagaras': 178,
    'Bucharest': 0,
    'Timisoara': 329,  
    'Lugoj': 244,      
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 160,
    'RimnicuVilcea': 193,
    'Pitesti': 98
    
}
path_cost = path_costs(graph_file_path)
start=input("Which city do you want to start with?\n")
a_star(start,"Bucharest", heuristics, path_cost)


"""     'Zerind': {'Arad': 75, 'Oradea': 71},
        'Arad': {'Zerind': 75, 'Timisoara': 118},
        'Oradea': {'Zerind': 71, 'Sibiu': 151},
        'Sibiu': {'Oradea': 151, 'Fagaras': 99, 'RimnicuVilcea': 80},
        'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
        'Bucharest': {'Fagaras': 211, 'Pitesti': 101},
        'Timisoara': {'Arad': 118, 'Lugoj': 111},
        'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
        'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
        'Drobeta': {'Mehadia': 75, 'Craiova': 120},
        'Craiova': {'Drobeta': 120, 'RimnicuVilcea': 146, 'Pitesti': 138},
        'RimnicuVilcea': {'Craiova': 146, 'Pitesti': 97, 'Sibiu': 80},
        'Pitesti': {'RimnicuVilcea': 97, 'Craiova': 138, 'Bucharest': 101}"""