import requests
import os
import time

URL_1 = 'http://bilgisayar.kocaeli.edu.tr/prolab2/url1.txt'
URL_2 = 'http://bilgisayar.kocaeli.edu.tr/prolab2/url2.txt'
ROBOT_LOCATION = (0, 0)
TARGET_LOCATION = (8, 8)


def get_body_from_url(url):
    resp_body = None
    resp = requests.get(url)
    if resp and resp.status_code == 200:
        resp_body = resp.text
    return resp_body


def get_matrix_from_text(matrix_text: str):
    main_matrix = []
    rows = matrix_text.split('\n')
    for row in rows:
        tmp_row = []
        for char in row:
            tmp_row.append(char)
        main_matrix.append(tmp_row.copy())
    return main_matrix

def clear_terminal():
    # print('\n'*80)
    os.system('cls' if os.name == 'nt' else 'clear')

def print_matrix(matrix: list):
    clear_terminal()
    if matrix:
        len_of_row = matrix[0].__len__()
        # print("-"*(2*len_of_row-1))
        for row in matrix:
            print("|".join(row))
            # print("-" * (2 * len_of_row - 1))


if __name__ == '__main__':

    matrix = None
    url_resp_body = get_body_from_url(URL_1)
    if url_resp_body:
        matrix = get_matrix_from_text(url_resp_body)
    matrix[TARGET_LOCATION[0]][TARGET_LOCATION[1]] = 'T'
    matrix[ROBOT_LOCATION[0]][ROBOT_LOCATION[1]] = 'R'
    robot_last_location = [ROBOT_LOCATION[0], ROBOT_LOCATION[1]]
    print_matrix(matrix)
    walked_path = []
    i = 0
    while i < 10:
        walked_path.append(robot_last_location)
        if matrix[robot_last_location[0] + 1][robot_last_location[1]] == '0':
            matrix[robot_last_location[0]][robot_last_location[1]] = '*'
            robot_last_location[0] += 1
            matrix[robot_last_location[0]][robot_last_location[1]] = 'R'
        elif matrix[robot_last_location[0]][robot_last_location[1]+1] == '0':
            matrix[robot_last_location[0]][robot_last_location[1]] = '*'
            robot_last_location[1] += 1
            matrix[robot_last_location[0]][robot_last_location[1]] = 'R'
        i += 1
        print_matrix(matrix)
        time.sleep(2)
