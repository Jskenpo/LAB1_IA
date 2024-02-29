from Search import *
import random
import math


import matplotlib.pyplot as plt

def plot_maze_with_path(maze, path):
    maze_copy = [row[:] for row in maze]  # Copia del laberinto para evitar modificar el original
    for x, y in path:
        maze_copy[x][y] = 'X'  # Marcar el camino con 'X'

    plt.figure(figsize=(len(maze[0]) / 2, len(maze) / 2))
    plt.imshow(maze_copy, cmap='binary', interpolation='nearest')

    # Agregar etiquetas
    for y in range(len(maze_copy)):
        for x in range(len(maze_copy[0])):
            plt.text(y, x, maze_copy[x][y], ha='center', va='center', color='red' if maze_copy[x][y] == 'X' else 'black')

    plt.xticks([])  # Ocultar etiquetas del eje x
    plt.yticks([])  # Ocultar etiquetas del eje y
    plt.grid(visible=True, color='gray', linestyle='--', linewidth=0.5)
    plt.show()


# Función para calcular la distancia euclidiana entre dos puntos
def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Función para calcular la distancia de Manhattan entre dos puntos
def manhattan_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x2 - x1) + abs(y2 - y1)

def generate_maze(rows, cols):
    maze = []
    for _ in range(rows):
        row = [random.choice([0, 1]) for _ in range(cols)]  # 0 representa un camino libre, 1 representa una pared
        maze.append(row)
    # Establecer la entrada y la salida en los bordes superior e inferior de la matriz
    maze[0][random.randint(0, cols - 1)] = 2  # Entrada marcada como 2
    maze[rows - 1][random.randint(0, cols - 1)] = 3  # Salida marcada como 3
    return maze

def print_maze(maze):
    for row in maze:
        print(' '.join(map(str, row)))

def find_start_end_coordinates(maze):
    start = None
    end = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 2:
                start = (i, j)
            elif maze[i][j] == 3:
                end = (i, j)
            if start is not None and end is not None:
                return start, end
    return start, end

def create_heuristic_functions(maze, end, distance_function):
    heuristic_functions = {}
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 0:  # Solo calcular la heurística para los espacios libres
                heuristic_functions[(i, j)] = distance_function((i, j), end)
    return heuristic_functions

def read_maze_from_file(file_path):
    maze = []
    with open(file_path, 'r') as file:
        for line in file:
            maze.append([int(char) for char in line.strip()])
    return maze



