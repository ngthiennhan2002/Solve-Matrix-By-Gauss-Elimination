import time
from fractions import Fraction

# Function to read matrix from file
def readMatrix(filename):
    f = open("data.txt", "r")
    matrix = []
    for x in f:
        temp_array = x.split()
        array = []
        for j in temp_array:
            array.append(int(j))
        matrix.append(array)
    row = len(matrix[0]) - 1
    column = len(matrix[0])
    return matrix, row, column


# Function to print the matrix
def printMatrix(matrix, row, column, msg):
    print(msg)
    for i in range(row):
        for j in range(column):
            print(matrix[i][j], end=' ')
        print()
   
   
# Function to swap two rows
def swapTwoRows(firstRow, secondRow):
    temp = firstRow
    firstRow = secondRow
    secondRow = temp
    return firstRow, secondRow


# Function to rearrange the matrix
# (Row has 0 at the left-most position will be pushed to bottom)
def rearrangeMatrix(matrix, row, column, pos):
    for i in range(pos, row):
        for j in range(i+1, row):
            if matrix[i][pos] != 0:
                break
            elif matrix[i][pos] == 0 and matrix[j][pos] != 0:
                matrix[i], matrix[j] = swapTwoRows(matrix[i], matrix[j])


# Function to simplìy the row (divided by its left-most value)
def simplify(row, pos):
    left_most_value = row[pos]
    for i in range(len(row)):
        row[i] = Fraction(row[i], left_most_value)
    return row
     
# Function to do Gauss elimination
def GaussElimination(matrix, row, column):
    try:
        for t in range(row):
            if t == row - 1:
                if matrix[t][t] != 0 and matrix[t][t] != 1:
                    matrix[t] = simplify(matrix[t], t)
                    return matrix, row, column
                elif matrix[t][t] == 0 or matrix[t][t] == 1:
                    return matrix, row, column
            while matrix[t][t] == 0:
                rearrangeMatrix(matrix, row, column, t)
            matrix[t] = simplify(matrix[t], t)
            for i in range(t + 1, row):
                ratio = -(matrix[i][t] * matrix[t][t])
                for j in range(column):
                    matrix[i][j] = matrix[i][j] + ratio * matrix[t][j]
    except:
        print("Cannot do Gauss Elimination")
    return matrix, row, column


# Function to check special cases
# Special cases: No solution, Infinite solutions
def isInSpecialCases(matrix, row, column):
    for i in range(row):
        count = 0
        for j in range(column - 1):
            if matrix[i][j] == 0:
                count += 1
        if count == column - 1:
            if matrix[i][column - 1] == 0:
                return "System has infinite solutions"
            else:
                return "System has no solution"
    return False


# Function to do Back Substitution
def backSubstitution(matrix, row, column):
    try:
        n = row
        x_data = [0] * n
        x_data[n-1] = matrix[n-1][n] # Gán kết quả x dưới cùng
        # range(start, stop, step)
        for i in range(n-2, -1, -1):
            x_data[i] = matrix[i][n]
            for j in range(i+1,n):
                x_data[i] = x_data[i] - matrix[i][j] * x_data[j]
            x_data[i] = x_data[i] / matrix[i][i]
        return x_data
    except:
        print("Cannot do Back Substitution!")


# Function to print result
def printSolution(matrix, row, column):
    print("\n--> CONCLUSION: ")
    special_case_conclusion = isInSpecialCases(matrix, row, column)
    if special_case_conclusion != False:
        print(special_case_conclusion)
    else:
        x_result = backSubstitution(matrix, row, column)
        for i in range(row):
            print("x", end='')
            print(i + 1, end='')
            print(" =", x_result[i])
        


# Main function
def main():
    try:
        filename = "data.txt"
        matrix, row, column = readMatrix(filename)
        msg = "ORIGINAL MATRIX:"
        printMatrix(matrix, row, column, msg)
        matrix, row, column = GaussElimination(matrix, row, column)
        msg = "\n--> SOLVED MATRIX:"
        printMatrix(matrix, row, column, msg)
        printSolution(matrix, row, column)
        print("\nRESULT: RUN CODE SUCCESSFULLY!")
    except:
        print("\nWARNING: FAILED TO RUN CODE!")

main()
time.sleep(1000)
