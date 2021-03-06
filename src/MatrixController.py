import os

# read matrix from .txt file from specified input
def read_matrix(filename):
    matrix = []
    # get parent folder path
    cwd = os.getcwd()
    if (os.path.basename(os.path.normpath(cwd)) != "bnb-15puzzle"):
        pardir = os.path.abspath(os.path.join(cwd, os.pardir))
    else:
        pardir = cwd
    fileDir = os.path.join(pardir, "test", filename)
    print(fileDir)
    try:
        with open(fileDir, 'r') as f:
            for line in f:
                tempList = list(line.strip().split())
                tempLine = []
                for x in tempList:
                    try:
                        tempLine.append(int(x))
                    except ValueError:
                        tempLine.append(16)
                matrix.append(tempLine)
                # matrix.append([int(x) for x in tempList])
        return matrix
    except FileNotFoundError:
        print("File tidak ditemukan")
        return None

# print matrix properly
def print_matrix(matrix):
    if (matrix != None):
        print("╔════╤════╤════╤════╗")
        # ┌	┍	┎	┏─	━	│	┃
        for i in range(len(matrix)):
            print("║", end=" ")
            for j in range(len(matrix[i])):
                strToPrint = str(matrix[i][j]) + " " if matrix[i][j] < 10 else str(matrix[i][j])
                if strToPrint == "16": strToPrint = "  "
                strToPrint = strToPrint + " │" if j != len(matrix[i])-1 else strToPrint + " ║"
                print(strToPrint, end=" ")
            if i != len(matrix) - 1:
                print("\n╟────┼────┼────┼────╢")
        print("\n╚════╧════╧════╧════╝")
    else:
        print("Matrix kosong")

# find 16 position in matrix, return -1, -1 if not found
def find_16(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] == 16):
                return i, j
    return -1, -1

# copy matrix
def copy_matrix(matrix):
    tempMatrix = []
    for i in range(len(matrix)):
        tempMatrix.append([])
        for j in range(len(matrix[i])):
            tempMatrix[i].append(matrix[i][j])
    return tempMatrix

# move 16 to specified position
def move_16(matrix, direction):
    i, j = find_16(matrix)
    tempMatrix = copy_matrix(matrix)
    if direction == "Atas":
        if i > 0:
            tempMatrix[i][j], tempMatrix[i-1][j] = matrix[i-1][j], matrix[i][j]
    elif direction == "Bawah":
        if i < len(matrix)-1:
            tempMatrix[i][j], tempMatrix[i+1][j] = matrix[i+1][j], matrix[i][j]
    elif direction == "Kiri":
        if j > 0:
            tempMatrix[i][j], tempMatrix[i][j-1] = matrix[i][j-1], matrix[i][j]
    elif direction == "Kanan":
        if j < len(matrix[i])-1:
            tempMatrix[i][j], tempMatrix[i][j+1] = matrix[i][j+1], matrix[i][j]
    return tempMatrix

# transform matrix to string
def mat_to_str(matrix):
    strToReturn = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            strToReturn += str(matrix[i][j]) + " "
    return strToReturn.strip()