import pandas as pd
import time
from Ejercicio2 import QueueFIFO, QueueLIFO, PriorityQueue

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
    queue = QueueFIFO()  # Utilizamos la cola FIFO en lugar de deque
    queue.insert((start, []))  # Insertamos el elemento inicial
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


'''

start_time = time.time()
path = bfs(start_node, end_node)
end_time = time.time()
print('------------BFS ALGORITHM------------')
if path:
    print("El camino de", start_node, "a", end_node, "es:", path)
    print("Longitud del camino:", len(path) - 1)  # Restar 1 para obtener el número de aristas
else:
    print("No hay camino de", start_node, "a", end_node)

print("Tiempo de ejecución:", end_time - start_time, "segundos")
    
'''
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


'''
start_time = time.time()
path = a_star(start_node, end_node)
end_time = time.time()
print('------------A* ALGORITHM------------')
if path:
    print("El camino de", start_node, "a", end_node, "es:", path)
    print("Longitud del camino:", len(path) - 1)  # Restar 1 para obtener el número de aristas
else:
    print("No hay camino de", start_node, "a", end_node)

print("Tiempo de ejecución:", end_time - start_time, "segundos")
'''


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



'''
start_time = time.time()
path = dfs(start_node, end_node)
end_time = time.time()
print('------------DFS ALGORITHM------------')
if path:
    print("El camino de", start_node, "a", end_node, "es:", path)
    print("Longitud del camino:", len(path) - 1)  # Restar 1 para obtener el número de aristas
else:
    print("No hay camino de", start_node, "a", end_node)

print("Tiempo de ejecución:", end_time - start_time, "segundos")
'''


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



'''
start_time = time.time()
path = uniform_cost_search(start_node, end_node)
end_time = time.time()

print('------------UCS ALGORITHM------------')
if path:
    print("El camino de", start_node, "a", end_node, "es:", path)
    print("Longitud del camino:", len(path) - 1)  # Restar 1 para obtener el número de aristas
else:
    print("No hay camino de", start_node, "a", end_node)

print("Tiempo de ejecución:", end_time - start_time, "segundos")
'''

# Greedy Best First Search algorithm, usando la cola de prioridad

def greedy_best_first(start, end):
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
                queue.insert((heuristic_functions[neighbor], neighbor, path + [node]))  # Insertamos el vecino en la cola de prioridad
                visited.add(neighbor)
    return None  # Devolver None si no se encuentra un camino


'''
start_time = time.time()
path = greedy_best_first(start_node, end_node)
end_time = time.time()

print('------------GBFS ALGORITHM------------')
if path:
    print("El camino de", start_node, "a", end_node, "es:", path)
    print("Longitud del camino:", len(path) - 1)  # Restar 1 para obtener el número de aristas
else:
    print("No hay camino de", start_node, "a", end_node)
    
print("Tiempo de ejecución:", end_time - start_time, "segundos")
'''
