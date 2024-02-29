import pandas as pd
from Queue import QueueFIFO, QueueLIFO, PriorityQueue

# BFS algorithm
def bfs(start, end, maze):
    visited = set()
    queue = QueueFIFO()  
    queue.insert((start, []))  
    while not queue.empty():
        node, path = queue.remove_first()
        if node == end:
            return path + [node]  
        visited.add(node)
        # Buscar celdas adyacentes válidas en el laberinto
        neighbors = get_valid_neighbors(node, maze)
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.insert((neighbor, path + [node]))
                visited.add(neighbor)
    return None

# A* algorithm
def a_star(start, end, maze, heuristic_functions):
    visited = set()
    queue = PriorityQueue() 
    queue.insert((0, start, []))  
    while not queue.empty():
        cost, node, path = queue.remove_first()  
        if node == end:
            return path + [node] 
        visited.add(node)
        neighbors = get_valid_neighbors(node, maze)
        for neighbor in neighbors:
            if neighbor not in visited:
                total_cost = cost + 1 + heuristic_functions.get(neighbor, 0)  # Consideramos un costo uniforme de 1 para todos los movimientos
                queue.insert((total_cost, neighbor, path + [node]))  
                visited.add(neighbor)
    return None

# DFS algorithm
def dfs(start, end, maze):
    visited = set()
    queue = QueueLIFO() 
    queue.insert((start, [])) 
    while not queue.empty():
        node, path = queue.remove_first()  
        if node == end:
            return path + [node]  
        visited.add(node)
        neighbors = get_valid_neighbors(node, maze)
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.insert((neighbor, path + [node]))  
                visited.add(neighbor)
    return None  

#greeedy first search algorithm
def greedy_first_search(start, end, maze, heuristic_functions):
    visited = set()
    queue = PriorityQueue() 
    queue.insert((0, start, []))  
    while not queue.empty():
        cost, node, path = queue.remove_first()  
        if node == end:
            return path + [node]  
        visited.add(node)
        neighbors = get_valid_neighbors(node, maze)
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.insert((heuristic_functions.get(neighbor, 0), neighbor, path + [node]))  
                visited.add(neighbor)
    return None

# Depth Limited Search algorithm
def depth_limited_search(start, end, limit, maze):
    visited = set()
    queue = QueueLIFO()  
    queue.insert((start, []))  
    while not queue.empty():
        node, path = queue.remove_first()  
        if node == end:
            return path + [node]  
        visited.add(node)
        if len(path) < limit:
            neighbors = get_valid_neighbors(node, maze)
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.insert((neighbor, path + [node]))  
                    visited.add(neighbor)
    return None

def get_valid_neighbors(node, maze):
    x, y = node
    neighbors = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Movimientos posibles: abajo, arriba, derecha, izquierda
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != 1:
            neighbors.append((nx, ny))
    return neighbors
