# Empty squares can be presented with 0, otherwise numbers are entered in a 9x9 matrix. 
# Sudoku checker checks rows, columns and 3x3 blocks. No number is allowed twice within those.
def sudoku_grid_correct(sudoku: list):
    check = [0] * 9
    #Check rows
    for row in sudoku:
        for element in row:
            if element !=0:
                index = element - 1
                check[index] = check[index] + 1
        for number in check:
            if number > 1:
                return False
        check = [0] * 9
    
    #Check columns
    check = [0] * 9
    k = 0
    while k <9:
        column = [row[k] for row in sudoku]
        k = k + 1

        for i in range(0, 9):
            if column[i] != 0:
                index = column[i] -1
                check[index] = check[index] + 1
        for number in check:
            if number > 1:
                return False
        check = [0] * 9
    
    #Check grids
    for row_no in [0, 3, 6]:
        for column_no in [0, 3, 6]:
            block = []
            for i in range(row_no, row_no + 3):
                row_slice = sudoku[i][column_no:column_no + 3]
                block.append(row_slice)

            check = [0] * 9
            for row in block:
                for element in row:
                    if element != 0:
                        index = element - 1
                        check[index] = check[index] + 1
    
            for number in check:
                if number > 1:
                    return False
    return True

# Tests
if __name__ == "__main__":
    sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))

