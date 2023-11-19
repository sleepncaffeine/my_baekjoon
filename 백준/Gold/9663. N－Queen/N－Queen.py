def safe(lvl, board):
    for i in range(lvl):
        if board[i] == board[lvl] or abs(board[lvl] - board[i]) == lvl - i:
            return False
    return True


def nqueen(x, n, board):
    if x == n:
        return 1
    count = 0
    for i in range(n):
        board[x] = i
        if safe(x, board):
            count += nqueen(x + 1, n, board)
    return count


n = int(input())
board = [0] * n
print(nqueen(0, n, board))
