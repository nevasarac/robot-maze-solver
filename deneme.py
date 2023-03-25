import requests
import os
import time
from heapq import heappop, heappush
import tkinter as tk

url_1 = 'http://bilgisayar.kocaeli.edu.tr/prolab2/url1.txt'
url_2 = 'http://bilgisayar.kocaeli.edu.tr/prolab2/url2.txt'

def get_url(url):
    resp_body = None
    resp = requests.get(url)
    if resp and resp.status_code == 200:
        resp_body = resp.text
    return resp_body

def get_matrix_from_text(matrix_text: str):
    main_matrix = []
    rows = matrix_text.split('\n')
    for row in rows:
        tmp = []
        for char in row:
            tmp.append(char)
        main_matrix.append(tmp.copy())
    return main_matrix

def clear_screen():
    # print('\n'*80)
    os.system('cls' if os.name == 'nt' else 'clear')

def print_matrix(matrix: list):
    clear_screen()
    if matrix:
        len_of_row = len(matrix[0])
        # print("-"*(2*len_of_row-1))
        for row in matrix:
            print("".join(row))
            # print("-" * (2 * len_of_row - 1))



def print_matrix_2():
    # Printing the labyrinth and the shortest path
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i, j) in shortest_path:
                print("X", end="")
            # elif matrix[i][j] == 0:
            #      print(".", end="")
            #  else:
            #      print("1", end="")
            else:
                print(matrix[i][j], end="")
        print("")

# Create a new window to display the maze
def create_window(matrix):
    window = tk.Tk()
    window.title("Maze")
    width = len(matrix[0]) * 20
    height = len(matrix) * 20
    window.geometry('{}x{}'.format(width, height))
    return window

# Draw maze in the window
def draw_maze(canvas, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '0':
                canvas.create_rectangle(j*20, i*20, (j+1)*20, (i+1)*20, fill="white")
            elif matrix[i][j] == '1':
                canvas.create_rectangle(j*20, i*20, (j+1)*20, (i+1)*20, fill="black")
            elif matrix[i][j] == '2':
                canvas.create_rectangle(j*20, i*20, (j+1)*20, (i+1)*20, fill="red")
            elif matrix[i][j] == '3':
                canvas.create_rectangle(j*20, i*20, (j+1)*20, (i+1)*20, fill="green")

# Draw path in the maze
def draw_path(canvas, shortest_path):
    for i in range(len(shortest_path)-1):
        x1 = shortest_path[i][1] * 20 + 10
        y1 = shortest_path[i][0] * 20 + 10
        x2 = shortest_path[i+1][1] * 20 + 10
        y2 = shortest_path[i+1][0] * 20 + 10
        canvas.create_line(x1, y1, x2, y2, fill="blue", width=5)
if __name__ == '__main__':

    url_resp = get_url(url_2)
    matrix = get_matrix_from_text(url_resp)

    robot_location = (0,0)
    target_location = (len(matrix)-1,len(matrix[0])-1)

    def h(point, goal):
        return abs(point[0] - goal[0]) + abs(point[1] - goal[1])

    # A* algorithm
    open_list = []
    heappush(open_list, (0, robot_location))
    closed_set = set()
    g = {robot_location: 0}
    f = {robot_location: h(robot_location, target_location)}
    previous = {}
    while open_list:
        _, cell = heappop(open_list)
        if cell == target_location:
            path = []
            while cell in previous:
                path.append(cell)
                cell = previous[cell]
            path.append(robot_location)
            path.reverse()
            break
        closed_set.add(cell)
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_cell = (cell[0] + direction[0], cell[1] + direction[1])
            if next_cell[0] < 0 or next_cell[0] >= len(matrix) or next_cell[1] < 0 or next_cell[1] >= len(matrix[0]):
                continue

            if matrix[next_cell[0]][next_cell[1]] in ('1','2','3'):# 0 ise bu yoldan gitmiyor
                continue
            cost = g[cell] + 1
            if next_cell in closed_set and cost >= g.get(next_cell, 0):
                continue
            if cost < g.get(next_cell, 0) or next_cell not in [i[1] for i in open_list]:
                previous[next_cell] = cell
                g[next_cell] = cost
                f[next_cell] = cost + h(next_cell, target_location)
                heappush(open_list, (f[next_cell], next_cell))

    # Finding the shortest path
    if target_location in path:
        shortest_path = [robot_location] + path
    else:
        shortest_path = []

    #print_matrix_2()
    for sp in shortest_path:

        matrix[sp[0]][sp[1]]="X"
        print_matrix(matrix)
        time.sleep(1)

    create_window(matrix)
    draw_maze(matrix)
    draw_path(shortest_path)