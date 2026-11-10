from collections import deque
import heapq
import statistics



result={
  "7-12": [
    {
      "id": 138,
      "site_name": "M25/4546A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 62,
      "volume": 1243
    },
    {
      "id": 144,
      "site_name": "M25/4681A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 36,
      "volume": 1510
    },
    {
      "id": 479,
      "site_name": "M25/4806A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 48,
      "volume": 1337
    },
    {
      "id": 544,
      "site_name": "M25/4700A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 23,
      "volume": 1230
    },
    {
      "id": 547,
      "site_name": "M25/4515A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 55,
      "volume": 1091
    },
    {
      "id": 699,
      "site_name": "M25/4479A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 59,
      "volume": 1359
    },
    {
      "id": 752,
      "site_name": "M25/4475A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 60,
      "volume": 1368
    },
    {
      "id": 778,
      "site_name": "M25/4811A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 885,
      "site_name": "M25/4565A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 60,
      "volume": 1204
    },
    {
      "id": 1135,
      "site_name": "M25/4690A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 1221,
      "site_name": "M25/4757A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 1270,
      "site_name": "M25/4534A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 63,
      "volume": 1243
    },
    {
      "id": 1442,
      "site_name": "M25/4605A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 51,
      "volume": 1395
    },
    {
      "id": 1990,
      "site_name": "M25/4620A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 2005,
      "site_name": "M25/4483A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 2089,
      "site_name": "M25/4777A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 2097,
      "site_name": "M25/4497A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 61,
      "volume": 1104
    },
    {
      "id": 2149,
      "site_name": "M25/4826A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 54,
      "volume": 1651
    },
    {
      "id": 2419,
      "site_name": "M25/4617J",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 2486,
      "site_name": "M25/4509A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 55,
      "volume": 1097
    },
    {
      "id": 2530,
      "site_name": "M25/4752A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 2636,
      "site_name": "M25/4787A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 45,
      "volume": 1593
    },
    {
      "id": 3003,
      "site_name": "M25/4696A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 29,
      "volume": 1179
    },
    {
      "id": 3323,
      "site_name": "M25/4583A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 55,
      "volume": 1238
    },
    {
      "id": 3437,
      "site_name": "M25/4490A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 62,
      "volume": 1122
    },
    {
      "id": 3714,
      "site_name": "M25/4822A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 53,
      "volume": 1651
    },
    {
      "id": 3835,
      "site_name": "M25/4658A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 30,
      "volume": 1329
    },
    {
      "id": 3897,
      "site_name": "M25/4792A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 51,
      "volume": 1576
    },
    {
      "id": 4000,
      "site_name": "M25/4551A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 4092,
      "site_name": "M25/4522A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 58,
      "volume": 1216
    },
    {
      "id": 4145,
      "site_name": "M25/4501A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 57,
      "volume": 1113
    },
    {
      "id": 4202,
      "site_name": "M25/4662A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 47,
      "volume": 1460
    },
    {
      "id": 4223,
      "site_name": "M25/4617A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 4714,
      "site_name": "M25/4762A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 4719,
      "site_name": "M25/4470A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 59,
      "volume": 1148
    },
    {
      "id": 4761,
      "site_name": "M25/4747A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 4894,
      "site_name": "M25/4802A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 47,
      "volume": 1366
    },
    {
      "id": 5107,
      "site_name": "M25/4817A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 50,
      "volume": 1648
    },
    {
      "id": 5118,
      "site_name": "M25/4686A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 30,
      "volume": 1235
    },
    {
      "id": 5138,
      "site_name": "M25/4772A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 5176,
      "site_name": "M25/4767A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 38,
      "volume": 1536
    },
    {
      "id": 5261,
      "site_name": "M25/4742A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 34,
      "volume": 1432
    },
    {
      "id": 5288,
      "site_name": "M25/4592A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 46,
      "volume": 1311
    },
    {
      "id": 5526,
      "site_name": "M25/4637A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 54,
      "volume": 1355
    },
    {
      "id": 5546,
      "site_name": "M25/4783A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 37,
      "volume": 1595
    },
    {
      "id": 5712,
      "site_name": "M25/4653A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 5875,
      "site_name": "M25/4507A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 56,
      "volume": 1085
    },
    {
      "id": 5990,
      "site_name": "M25/4797A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 6156,
      "site_name": "M25/4537A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 65,
      "volume": 1182
    }
  ],
  "12-13": [
    {
      "id": 8,
      "site_name": "M25/4876A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 62,
      "volume": 1661
    },
    {
      "id": 1811,
      "site_name": "M25/4848A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 63,
      "volume": 1684
    },
    {
      "id": 1910,
      "site_name": "M25/4860A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 2952,
      "site_name": "M25/4866A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 63,
      "volume": 1647
    },
    {
      "id": 2992,
      "site_name": "M25/4832A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 60,
      "volume": 974
    },
    {
      "id": 3319,
      "site_name": "M25/4854A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 65,
      "volume": 1663
    },
    {
      "id": 5245,
      "site_name": "M25/4879A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 61,
      "volume": 1640
    },
    {
      "id": 5662,
      "site_name": "M25/4843A",
      "time": "2026-01-19T08:59:59",
      "average_mph": None,
      "volume": None
    },
    {
      "id": 5681,
      "site_name": "M25/4836A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 61,
      "volume": 1035
    }
  ],
  "13-14": [
    {
      "id": 279,
      "site_name": "M25/4909A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 41,
      "volume": 1555
    },
    {
      "id": 737,
      "site_name": "M25/4883A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 63,
      "volume": 1341
    },
    {
      "id": 3671,
      "site_name": "M25/4898A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 54,
      "volume": 1601
    },
    {
      "id": 4053,
      "site_name": "M25/4903A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 40,
      "volume": 1527
    },
    {
      "id": 4354,
      "site_name": "M25/4887A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 62,
      "volume": 1305
    },
    {
      "id": 5317,
      "site_name": "M25/4892A",
      "time": "2026-01-19T08:59:00",
      "average_mph": 57,
      "volume": 1310
    }
  ],
  "14-Heathrow": [
    {
      "id": 746,
      "site_name": "M25/7106B",
      "time": "2026-01-19T08:59:00",
      "average_mph": 34,
      "volume": 226
    }
  ],
  "A30": [
    {
      "id": 9005,
      "site_name": "6178/1",
      "time": "2026-01-19T08:59:00",
      "average_mph": 57,
      "volume": 330
    }
  ]
}
    


class nodes: 
    '''Used for the unweighted graphs for a junction node'''
    def __init__(self, value):
        self.value = value
        self.adjacent_nodes = []

    def add_adjacent_nodes(self, nodes):
        self.adjacent_nodes.append(nodes)

    def __repr__(self):
        return f"Node ({self.value})"


class weighted_junction:
    '''Used for the unweighted graphs for a junction node '''
    def __init__(self, name):
        ''' Method for junction  name and an empty dictionary of connected roads.'''
        self.name = name
        self.passages = {}

    def add_passage(self, weighted_junction, time):
        self.passages[weighted_junction] = time

    def __repr__(self):
        return f"Junction({self.name})"

    def __hash__(self):
        return hash(self.name)

    def __lt__(self, other):
        return self.name < other.name


def connect(a, b, time):
    '''Connects two junctions in both directions with the same travel time.'''
    a.add_passage(b, time)
    b.add_passage(a, time)


def travel_time(distance_miles, speed_mph):
    '''Calculates how many minutes it takes to travel a given distance at a given speed.'''
    if speed_mph == 0:
        return float("n/a")
    return (distance_miles / speed_mph) * 60


def average_speed(sensor_list):
    '''Returns the average speed from a list of sensors, ignoring any that have no reading.'''
    speeds = [s["average_mph"] for s in sensor_list if s["average_mph"] is not None]
    return statistics.mean(speeds) if speeds else 0


def route_time(path, junction_map):
    '''Adds up the total travel time in minutes for a given list of junction names.'''
    total = 0
    for i in range(len(path) - 1):
        a = junction_map[path[i]]
        b = junction_map[path[i + 1]]
        total += a.passages[b]
    return total


def graphs(webtris):
    '''Builds both the unweighted graph for BFS/DFS and the weighted graph for Dijkstra.'''
    speed_7_12 = average_speed(webtris["7-12"])
    speed_12_13 = average_speed(webtris["12-13"])
    speed_13_14 = average_speed(webtris["13-14"])
    speed_A30 = average_speed(webtris["A30"])

    J7v = nodes("J7")
    J12v = nodes("J12")
    J13v = nodes("J13")
    A30v = nodes("A30")
    Heathrowv = nodes("Heathrow")

    J7v.add_adjacent_nodes(J12v)

    J12v.add_adjacent_nodes(Heathrowv)
    J12v.add_adjacent_nodes(J13v)      

    J13v.add_adjacent_nodes(Heathrowv)

    J13v.add_adjacent_nodes(A30v)
    A30v.add_adjacent_nodes(Heathrowv)

    J7 = weighted_junction("J7")
    J12 = weighted_junction("J12")
    J13 = weighted_junction("J13")
    A30 = weighted_junction("A30")
    Heathrow = weighted_junction("Heathrow")

    connect(J7, J12, travel_time(23, speed_7_12))

    connect(J12, J13, travel_time(3, speed_12_13))
    connect(J13, Heathrow, travel_time(3, speed_13_14))

    connect(J12, Heathrow,  20)


    connect(J13, A30, travel_time(0.4, 30))
    connect(A30, Heathrow, travel_time(6.8, speed_A30))

    junction_map = {
        "J7": J7,
        "J12": J12,
        "J13": J13,
        "A30": A30,
        "Heathrow": Heathrow,
    }

    return (J7v, Heathrowv), (J7, Heathrow), junction_map


def BFS(start, goal):
    '''Finds the route with the fewest junctions using breadth-first search.'''
    visited = {start.value}
    queue = deque([(start, [start.value], 0)])

    while queue:
        current, path, hops = queue.popleft()

        if current.value == goal.value:
            return path, hops

        for neighbor in current.adjacent_nodes:
            if neighbor.value not in visited:
                visited.add(neighbor.value)
                queue.append((neighbor, path + [neighbor.value], hops + 1))

    return None, None


def DFS(start, goal, visited=None, path=None, hops=0):
    '''Finds a valid route by following one path at a time until it reaches the destination.'''
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start.value)
    path.append(start.value)

    if start.value == goal.value:
        return path, hops

    for neighbor in start.adjacent_nodes:
        if neighbor.value not in visited:
            result = DFS(neighbor, goal, visited, path.copy(), hops + 1)
            if result[0] is not None:
                return result

    return None, None


def dijkstra(start, end):
    '''Finds the fastest route with the lowest travel time so far.'''
    priority = [(0, start)]
    min_time = {start: 0}
    previous = {}

    while priority:
        current_time, current = heapq.heappop(priority)

        if current == end:
            break

        for neighbor, weight in current.passages.items():
            new_cost = current_time + weight

            if neighbor not in min_time or new_cost < min_time[neighbor]:
                min_time[neighbor] = new_cost
                previous[neighbor] = current
                heapq.heappush(priority, (new_cost, neighbor))

    path = []
    node = end
    while node in previous:
        path.append(node.name)
        node = previous[node]
    path.append(start.name)
    path.reverse()

    return path, min_time.get(end)


if __name__ == "__main__":
    print("Build Graphs")
    (start_v, end_v), (start_r, end_r), junction_map = graphs(result)
    print("Breath First Search")
    BFS_path, BFS_hops = BFS(start_v, end_v)
    print("Route:".join(BFS_path))
    print("Number of junctions:", BFS_hops)
    print("Estimated travel time:",
          round(route_time(BFS_path, junction_map), 2), "minutes")
    print("Depth First Search")
    DFS_path, DFS_hops = DFS(start_v, end_v)
    print("Route:".join(DFS_path))
    print("Number of junctions:", DFS_hops)
    print("Estimated travel time:",
          round(route_time(DFS_path, junction_map), 2), "minutes")
    print("Dijkstra")
    d_path, d_cost = dijkstra(start_r, end_r)
    print("Route".join(d_path))
    print("Estimated travel time:", round(d_cost, 2), "minutes")