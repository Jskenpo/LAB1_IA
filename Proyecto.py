from Preprocessing import *
from Search import *

# Llamar a la función de búsqueda deseada
print("Laberinto:")
maze = read_maze_from_file('test_maze.txt')

start, end = find_start_end_coordinates(maze)
print("Coordenadas de inicio:", start)
print("Coordenadas de fin:", end)


# Ejemplo de uso de BFS
print("\nEjemplo de búsqueda usando BFS:")
path_bfs = bfs(start, end, maze )
#contar en cuantos pasos se resuelve el laberinto
pasos = len(path_bfs)
if path_bfs:
    print("Camino encontrado:", path_bfs)
    print("Pasos para resolver el laberinto: ", pasos)
else:
    print("No se encontró ningún camino usando BFS.")


# Ejemplo de uso de A*
print("\nEjemplo de búsqueda usando A*:")
heuristic_functions = create_heuristic_functions(maze, end, euclidean_distance)
path_a_star = a_star(start, end, maze, heuristic_functions)
pasos = len(path_a_star)
if path_a_star:
    print("Camino encontrado:", path_a_star)
    print("Pasos para resolver el laberinto: ", pasos)
else:
    print("No se encontró ningún camino usando A*.")


# Ejemplo de uso de DFS
print("\nEjemplo de búsqueda usando DFS:")

path_dfs = dfs(start, end, maze)
pasos = len(path_dfs)
if path_dfs:
    print("Camino encontrado:", path_dfs)
    print("Pasos para resolver el laberinto: ", pasos)
else:
    print("No se encontró ningún camino usando DFS.")

# Ejemplo de uso de Greedy First Search
print("\nEjemplo de búsqueda usando Greedy First Search:")

path_greedy_first_search = greedy_first_search(start, end, maze, heuristic_functions)
pasos = len(path_greedy_first_search)
if path_greedy_first_search:
    print("Camino encontrado:", path_greedy_first_search)
    print("Pasos para resolver el laberinto: ", pasos)
else:
    print("No se encontró ningún camino usando Greedy First Search.")

# Ejemplo de uso de Depth Limited Search
print("\nEjemplo de búsqueda usando Depth Limited Search:")
path_depth_limited_search = depth_limited_search(start, end, 10, maze)

if path_depth_limited_search:
    print("Camino encontrado:", path_depth_limited_search)
    pasos = len(path_depth_limited_search)
    print("Pasos para resolver el laberinto: ", pasos)
else:
    print("No se encontró ningún camino usando Depth Limited Search.")








