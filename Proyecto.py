from Preprocessing import *
from Search import *
import time 

# Llamar a la función de búsqueda deseada
print("Laberinto:")
maze = read_maze_from_file('test_maze.txt')

start, end = find_start_end_coordinates(maze)
print("Coordenadas de inicio:", start)
print("Coordenadas de fin:", end)

salida = True

while salida:
    
    print('----------------MENU DE OPCIONES----------------')
    print('Seleccione el algoritmo de búsqueda que desea usar: ')
    print('1. BFS')
    print('2. A*')
    print('3. DFS')
    print('4. Greedy First Search')
    print('5. Depth Limited Search')
    print('6. Salir')

    opcion = int(input('Ingrese la opción que desea: '))

    if opcion == 1:

        # Ejemplo de uso de BFS
        print("\nEjemplo de búsqueda usando BFS:")

        start_time = time.time()

        path_bfs = bfs(start, end, maze )
        #contar en cuantos pasos se resuelve el laberinto
        
        excecution_time = round(time.time() - start_time, 6)
        
        if path_bfs:
            pasos = len(path_bfs)
            print("Camino encontrado:", path_bfs)
            print("Pasos para resolver el laberinto: ", pasos)
            print("--- %s seconds ---" % excecution_time)
        else:
            print("No se encontró ningún camino usando BFS.")

    elif opcion == 2:

        # Ejemplo de uso de A*
        print("\nEjemplo de búsqueda usando A*:")
        heuristic_functions = create_heuristic_functions(maze, end, euclidean_distance)

        start_time = time.time()

        path_a_star = a_star(start, end, maze, heuristic_functions)
        excecution_time = round(time.time() - start_time, 6)
        if path_a_star:
            pasos = len(path_a_star)
            print("Camino encontrado:", path_a_star)
            print("Pasos para resolver el laberinto: ", pasos)
            print("--- %s seconds ---" % excecution_time)
        else:
            print("No se encontró ningún camino usando A*.")

    elif opcion == 3:
        # Ejemplo de uso de DFS
        print("\nEjemplo de búsqueda usando DFS:")
        start_time = time.time()
        path_dfs = dfs(start, end, maze)
        
        excecution_time = round(time.time() - start_time, 6)
        if path_dfs:
            pasos = len(path_dfs)
            print("Camino encontrado:", path_dfs)
            print("Pasos para resolver el laberinto: ", pasos)
            print("--- %s seconds ---" % excecution_time)
        else:
            print("No se encontró ningún camino usando DFS.")

    elif opcion == 4:
        # Ejemplo de uso de Greedy First Search
        print("\nEjemplo de búsqueda usando Greedy First Search:")
        start_time = time.time()
        path_greedy_first_search = greedy_first_search(start, end, maze, heuristic_functions)
        
        excecution_time = round(time.time() - start_time, 6)
        if path_greedy_first_search:
            pasos = len(path_greedy_first_search)
            print("Camino encontrado:", path_greedy_first_search)
            print("Pasos para resolver el laberinto: ", pasos)
            print("--- %s seconds ---" % excecution_time)
        else:
            print("No se encontró ningún camino usando Greedy First Search.")

    elif opcion == 5:
        # Ejemplo de uso de Depth Limited Search
        print("\nEjemplo de búsqueda usando Depth Limited Search:")
        start_time = time.time()
        path_depth_limited_search = depth_limited_search(start, end, 10, maze)
        excecution_time = round(time.time() - start_time, 6)
        if path_depth_limited_search:
            print("Camino encontrado:", path_depth_limited_search)
            pasos = len(path_depth_limited_search)
            print("Pasos para resolver el laberinto: ", pasos)
            print("--- %s seconds ---" % excecution_time)
            
        else:
            print("No se encontró ningún camino usando Depth Limited Search.")

    else:
        print('Saliendo...')
        salida = False








