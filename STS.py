#!/usr/bin/env python3

# 2d array board
board = [[0 for j in range(7)] for i in range(9)]

# Value dict to convert color string to value
s_dict = {
    "r": 25,
    "g": 5,
    "p": 10,
    "b": 0
}

# Starting position is always the same
START = tuple([4, 3])


def main():
    # Read in the board
    f = open("board.txt", "r")
    for i in range(9):
        row = f.readline()[0:7]
        for j in range(7):
            board[i][j] = row[j]

    opt_path = dfs(15, [START], 0)
    simplified = ""
    print(opt_path)
    for step in range(1, len(opt_path[1])):
        if opt_path[1][step][0] > opt_path[1][step-1][0]:
            simplified += "D"
        elif opt_path[1][step][0] < opt_path[1][step-1][0]:
            simplified += "U"
        elif opt_path[1][step][1] < opt_path[1][step-1][1]:
            simplified += "L"
        else:
            simplified += "R"
    print(simplified)


def dfs(left, path, score):
    # Current position (row/col)
    cur = path[len(path)-1]

    # If the current position is out of bounds return None
    if cur[0] not in range(0, 9) or cur[1] not in range(0, 7):
        return None

    # Add the value of this position to the score total
    score += s_dict[board[cur[0]][cur[1]]]
    if left == 0:
        return [score, path]

    # Create list of all possible next positions
    next = [tuple([cur[0]+1, cur[1]]), tuple([cur[0]-1, cur[1]]),
            tuple([cur[0], cur[1]+1]), tuple([cur[0], cur[1]-1])]
    results = []
    for coord in next:
        if coord not in path:
            result = dfs(left-1, path + [coord], score)
            if result is not None:
                results.append(result)

    if len(results) == 0:
        return None
    return max(results, key=lambda x: x[0])


if __name__ == "__main__":
    main()
