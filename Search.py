import pandas as pd
from Queue import QueueFIFO, QueueLIFO, PriorityQueue

# Leer archivos de Excel
costs_sheet = pd.read_excel("funcion_de_costo.xlsx") 
heuristic_sheet = pd.read_excel("heuristica.xlsx")

# Diccionarios de costos y heurísticas
cost_functions = {}

# Crear diccionario de costos
for i in range(len(costs_sheet)):
    if costs_sheet.iloc[i, 0] not in cost_functions:
        cost_functions[costs_sheet.iloc[i, 0]] = {}
    cost_functions[costs_sheet.iloc[i, 0]][costs_sheet.iloc[i, 1]] = costs_sheet.iloc[i, 2]

# Crear diccionario de heurísticas
heuristic_functions = {}
for i in range(len(heuristic_sheet)):
    heuristic_functions[heuristic_sheet.iloc[i, 0]] = heuristic_sheet.iloc[i, 1]


start_node = "Warm-up activities"
end_node = "Stretching"

# BFS algorithm

def bfs(start, end):
    visited = set()
    queue = QueueFIFO()  
    queue.insert((start, []))  
    while not queue.empty():
        print("Cola actual:", queue.queue)
        print("Nodos visitados:", visited)
        print("-----------------------------")
        node, path = queue.remove_first()  # Usamos los métodos de la cola FIFO
        print("Explorando nodo:", node)
        if node == end:
            return path + [node]  # Devolver el camino si se alcanza el nodo final
        visited.add(node)
        for neighbor, cost in cost_functions.get(node, {}).items():
            if neighbor not in visited:
                queue.insert((neighbor, path + [node]))  # Insertamos el vecino en la cola FIFO
                visited.add(neighbor)
    return None  # Devolver None si no se encuentra un camino

# A* algorithm

def a_star(start, end):
    visited = set()
    queue = PriorityQueue()  # Utilizamos la cola de prioridad en lugar de heapq
    queue.insert((0, start, []))  # Insertamos el elemento inicial
    while not queue.empty():
        print("Cola actual:", queue.queue)
        print("Nodos visitados:", visited)
        print("-----------------------------")
        cost, node, path = queue.remove_first()  # Usamos los métodos de la cola de prioridad
        print("Explorando nodo:", node)
        if node == end:
            return path + [node]  # Devolver el camino si se alcanza el nodo final
        visited.add(node)
        for neighbor, cost_to_neighbor in cost_functions.get(node, {}).items():
            if neighbor not in visited:
                total_cost = cost + cost_to_neighbor + heuristic_functions[neighbor]
                queue.insert((total_cost, neighbor, path + [node]))  # Insertamos el vecino en la cola de prioridad
                visited.add(neighbor)
    return None  # Devolver None si no se encuentra un camino

# DFS algorithm

def dfs(start, end):
    visited = set()
    queue = QueueLIFO()  # Utilizamos la cola LIFO en lugar de deque
    queue.insert((start, []))  # Insertamos el elemento inicial
    while not queue.empty():
        print("Cola actual:", queue.queue)
        print("Nodos visitados:", visited)
        print("-----------------------------")
        node, path = queue.remove_first()  # Usamos los métodos de la cola LIFO
        print("Explorando nodo:", node)
        if node == end:
            return path + [node]  # Devolver el camino si se alcanza el nodo final
        visited.add(node)
        for neighbor, cost in cost_functions.get(node, {}).items():
            if neighbor not in visited:
                queue.insert((neighbor, path + [node]))  # Insertamos el vecino en la cola LIFO
                visited.add(neighbor)
    return None  # Devolver None si no se encuentra un camino

# Uniform Cost Search algorithm, usando la cola de prioridad

def uniform_cost_search(start, end):
    visited = set()
    queue = PriorityQueue()  # Utilizamos la cola de prioridad en lugar de heapq
    queue.insert((0, start, []))  # Insertamos el elemento inicial
    while not queue.empty():
        print("Cola actual:", queue.queue)
        print("Nodos visitados:", visited)
        print("-----------------------------")
        cost, node, path = queue.remove_first()  # Usamos los métodos de la cola de prioridad
        print("Explorando nodo:", node)
        if node == end:
            return path + [node]  # Devolver el camino si se alcanza el nodo final
        visited.add(node)
        for neighbor, cost_to_neighbor in cost_functions.get(node, {}).items():
            if neighbor not in visited:
                total_cost = cost + cost_to_neighbor
                queue.insert((total_cost, neighbor, path + [node]))  # Insertamos el vecino en la cola de prioridad
                visited.add(neighbor)
    return None  # Devolver None si no se encuentra un camino

# Greedy Best First Search algorithm

def greedy_best_first(start, end):
    visited = set()
    queue = PriorityQueue()  
    queue.insert((0, start, []))  # Insertamos el elemento inicial
    while not queue.empty():
        print("Cola actual:", queue.queue)
        print("Nodos visitados:", visited)
        print("-----------------------------")
        cost, node, path = queue.remove_first()  # Usamos los métodos de la cola de prioridad
        print("Explorando nodo:", node)
        if node == end:
            return path + [node]  # Devolver el camino si se alcanza el nodo final
        visited.add(node)
        for neighbor, cost_to_neighbor in cost_functions.get(node, {}).items():
            if neighbor not in visited:
                queue.insert((heuristic_functions[neighbor], neighbor, path + [node]))  # Insertamos el vecino en la cola de prioridad
                visited.add(neighbor)
    return None  # Devolver None si no se encuentra un camino

#Depth delimited search algorithm

def depth_limited_search(start, end, limit):
    visited = set()
    queue = QueueLIFO()  # Utilizamos la cola LIFO en lugar de deque
    queue.insert((start, []))  # Insertamos el elemento inicial
    while not queue.empty():
        print("Cola actual:", queue.queue)
        print("Nodos visitados:", visited)
        print("-----------------------------")
        node, path = queue.remove_first()  # Usamos los métodos de la cola LIFO
        print("Explorando nodo:", node)
        if node == end:
            return path + [node]  # Devolver el camino si se alcanza el nodo final
        visited.add(node)
        if len(path) < limit:
            for neighbor, cost in cost_functions.get(node, {}).items():
                if neighbor not in visited:
                    queue.insert((neighbor, path + [node]))  # Insertamos el vecino en la cola LIFO
                    visited.add(neighbor)
    return None  # Devolver None si no se encuentra un camino

