def find_empty(puzzle):
	for row in range(len(puzzle)):
		for col in range(len(puzzle)):
			if puzzle[row][col] == -1:
				return row, col
	return None, None


def valid(puzzle, guess, row, col):
	row_val = puzzle[row]
	if guess in row_val:
		return False

	col_val = [puzzle[i][col] for i in range(len(puzzle))]
	if guess in col_val:
		return False

	row_start = (row//3)*3
	col_start = (col//3)*3

	for r in range(row_start, row_start+3):
		for c in range(col_start, col_start+3):
			if puzzle[r][c] == guess:
				return False
	return True


def solve(puzzle):
	row, col = find_empty(puzzle)

	if row == None:
		return True
	
	for guess in range(1,len(puzzle)+1):
		if valid(puzzle, guess, row, col):
			puzzle[row][col] = guess

			if solve(puzzle):
				return True


		puzzle[row][col] = -1
	return False


example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]

print(solve(example_board))
print(example_board)

