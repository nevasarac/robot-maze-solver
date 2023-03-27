from tkinter import ttk
import random
import requests
import os
import time
from heapq import heappop, heappush
import tkinter as tk
from datetime import datetime

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

# Draw maze in the window
def draw_maze(canvas, matrix):
    canvas.delete("all")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '0':
                canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill="white")
            elif matrix[i][j] == '1':
                canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill="black")
            elif matrix[i][j] == '2':
                canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill="red")
            elif matrix[i][j] == '3':
                canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill="green")
            elif matrix[i][j] == 'R':
                canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill="blue")
            elif matrix[i][j] == 'T':
                canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill="yellow")
    x1, y1, x2, y2 = canvas.bbox('all')
    canvas.config(width=x2, height=y2)


# Draw path in the maze
def draw_path(canvas, shortest_path):
    for i in range(len(shortest_path) - 1):
        x1 = shortest_path[i][1] * 20 + 10
        y1 = shortest_path[i][0] * 20 + 10
        x2 = shortest_path[i + 1][1] * 20 + 10
        y2 = shortest_path[i + 1][0] * 20 + 10
        canvas.create_line(x1, y1, x2, y2, fill="blue", width=5)


def change_url():
    global current_url
    current_url = (current_url + 1) % len(urls)
    url_lbl.config(text="Url:" + urls[current_url])
    # url_button.config(text=urls[current_url])


def run_solver():
    t1 = datetime.now()
    global shortest_path
    global delta
    url_resp = get_url(urls[current_url])
    matrix = get_matrix_from_text(url_resp)
    is_found = False
    while(not is_found):
        ri = random.randint(0,len(matrix)-1)
        rj = random.randint(0,len(matrix[0])-1)
        if matrix[ri][rj] == '0':
            robot_location = (ri,rj)
            is_found = True
    is_found = False
    while (not is_found):
        ri = random.randint(0, len(matrix)-1)
        rj = random.randint(0, len(matrix[0])-1)
        if matrix[ri][rj] == '0':
            target_location = (ri, rj)
            is_found = True
    matrix[robot_location[0]][robot_location[1]] = 'R'
    matrix[target_location[0]][target_location[1]] = 'T'

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

            if matrix[next_cell[0]][next_cell[1]] in ('1', '2', '3'):  # 0 ise bu yoldan gitmiyor
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

    # print_matrix_2()
    # for sp in shortest_path:
    #
    #     matrix[sp[0]][sp[1]]="X"
    #     game_str = ""
    #     for row in matrix:
    #         game_str+="".join(row)+"\n"
    #     #print_matrix(matrix)
    #     game_lbl.config(text=game_str)
    draw_maze(maze_canvas, matrix)
    result_info_lbl.config(text="")

    # convert time string to datetime

    t2 = datetime.now()

    # get difference
    delta = t2 - t1

def show_solve():
    global shortest_path
    global delta
    draw_path(maze_canvas, shortest_path)
    result_info_lbl.config(text="Robotun geçtiği kare sayısı : "+str(len(shortest_path))+" Geçen süre : "+str(delta.total_seconds()))


if __name__ == '__main__':
    urls = ["http://bilgisayar.kocaeli.edu.tr/prolab2/url1.txt", "http://bilgisayar.kocaeli.edu.tr/prolab2/url2.txt"]
    current_url = 0

    root = tk.Tk()
    root.title('PROJE')
    # root.geometry('850x850+500+100')
    url_lbl = tk.Label(root, text="Url:" + urls[current_url])
    # lbl.grid(column=0, row=0)
    # url_lbl.pack()
    url_lbl.grid(row=0, columnspan=2, padx=2, pady=15)
    maze_canvas = tk.Canvas(root)
    url_button = tk.Button(root, text="Url değiştir", command=change_url)
    # url_button.pack()
    url_button.grid(row=2, columnspan=2, padx=2, pady=15)

    run_button = tk.Button(root, text="Çalıştır", command=run_solver)
    # run_button.pack()
    run_button.grid(row=3, column=0, padx=2, pady=15)
    solve_button = tk.Button(root, text="En kısa yolu göster", command=show_solve)
    solve_button.grid(row=3, column=1, padx=2, pady=15)

    # maze_canvas.pack()
    maze_canvas.grid(row=4, columnspan=2, padx=2, pady=15)

    # first_space_lbl = tk.Label(root)
    # first_space_lbl.grid(row=1)
    result_info_lbl = tk.Label(root)
    result_info_lbl.grid(row=5, columnspan=2, padx=2, pady=15)

    root.mainloop()
