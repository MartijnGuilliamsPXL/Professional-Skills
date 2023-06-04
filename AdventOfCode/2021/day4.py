with open("./day4.txt") as file:
    data = file.read().split("\n")

while("" in data):
    data.remove("")

drawnNumbers = data[0].split(',')
boardsAmount = len(data) - 1
boards = []
for i in range(int(boardsAmount/5)):
    board = []
    for j in range(5):
        board.append(data[i*5+1+j].split())
    boards.append(board)

win = False
for drawnNumber in drawnNumbers:
    if win:
        break
    #search drawnnumber in array and replace it with X
    for i,board in enumerate(boards):
        for j,row in enumerate(board):
            for k,n in enumerate(row):
                if n == drawnNumber:
                    boards[i][j][k] = "X"
    

    for board in boards:
        checkRow = False
        checkCol = False
        for row in board:
            checkRow = True
            for n in row:
                if n != "X":
                    checkRow = False
                    break
            if checkRow:
                break

        for col in range(len(board[0])):
            checkCol = True
            for row in range(len(board)):
                if board[row][col] != "X":
                    checkCol = False
                    break
            if checkCol:
                break
        
        if checkRow or checkCol:
            win = True
            score = 0
            for row in board:
                for n in row:
                    if n != "X":
                        score += int(n)
            score = score * int(drawnNumber)
            print(score)
            break;


#Part 2
        
drawnNumbers = data[0].split(',')
boardsAmount = len(data) - 1
boards = []
for i in range(int(boardsAmount/5)):
    board = []
    for j in range(5):
        board.append(data[i*5+1+j].split())
    boards.append(board)

win = False
solved_boards = 0

for drawnNumber in drawnNumbers:
    if win:
        break
    for i,board in enumerate(boards):
        for j,row in enumerate(board):
            for k,n in enumerate(row):
                if n == drawnNumber:
                    boards[i][j][k] = "X"
    
    for i,board in enumerate(boards):
        checkRow = False
        checkCol = False
        for row in board:
            checkRow = True
            for n in row:
                if n != "X":
                    checkRow = False
                    break
            if checkRow:
                break

        for col in range(len(board[0])):
            checkCol = True
            for row in range(len(board)):
                if board[row][col] != "X":
                    checkCol = False
                    break
            if checkCol:
                break
        
        if checkRow or checkCol:
            solved_boards += 1
            if solved_boards != boardsAmount/5:
                for j,row in enumerate(board):
                    for k,n in enumerate(row):
                        boards[i][j][k] = "O"
            else:
                win = True
                score = 0
                for row in board:
                    for n in row:
                        if n != "X":
                            score += int(n)
                score = score * int(drawnNumber)
                print(score)