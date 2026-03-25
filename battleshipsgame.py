import random
while True:
    name = str(input("Welcome to Battleships! Enter your name: "))             #initalise name
    boardsize = 10
    
    while True:
        shipLength = int(input("Enter the length of your ship (1-3): "))        #ship length
        if shipLength < 1 or shipLength > 3:
            print("Invalid length. Please Enter again.")
            continue
        else:
            break
    while True:    
        shipX = int(input("Enter the x coordinates of your ship (1-9): "))           #coordinates of ship
        shipY = int(input("Enter the y coordinates of your ship (1-9): "))
        if shipX < 1 or shipX > 9 or shipY < 1 or shipY > 9:
            print("Invalid coordinates. Please Enter again.")
            continue
        else:
            break
    while True:
        shipOri = str(input("Enter the orientation of your ship (horizontal or vertical): ")) #orientation of the ship and whether it can fit on board
        if shipOri == "vertical":
            if shipY + shipLength > 10:
                print("Invalid placement, ship will be out of bounds. Try again")
                continue
            else:
                break
        elif shipOri == "horizontal":
            if shipX + shipLength > 10:
                print("Invalid placement, ship will be out of bounds. Try again")
                continue
            else:
                break
        elif shipOri != "horizontal" or shipOri != "vertical":
            print("Invalid input. Please Enter again.")
            continue
    board = []
    for i in range(0, boardsize):                          # intialising the board
        boardrow = []
        for j in range(0, boardsize):
            boardrow.append(0)
        board.append(boardrow)

    print(f"Your now have a ship of length {shipLength} placed at ({shipX}, {shipY}) on the board.") 
    
    def placeship(startX, length, startY, Ori):
        if Ori == "horizontal":
            for i in range(startX, startX + length):
                if board[startY][i] == 0:
                    board[startY][i] = 'S'
                else:
                    board[i][startX] = 'X'
        elif Ori == "vertical":
            for i in range(startY, startY + length):
                if board[i][startX] == 0:
                    board[i][startX] = 'S'
                else:
                    board[i][startX] = 'X'

    def printboard(board):
        for i in range(0, boardsize):
            for j in range(0, boardsize):
                print(board[i][j], end = ' ')
            print('')    

    placeship(shipX, shipLength, shipY, shipOri)  
    printboard(board)

    while True:
        # Start randship input loop
        while True:
            randshipLength = int(input("Enter the length of another ship to attack (1-3): "))
            if randshipLength < 1 or randshipLength > 3:
                print("Invalid length. Please Enter again.")
                continue
            else:
                break
        while True:
            randshipX = int(input("Enter the x coordinates of this ship (1-9): "))
            randshipY = int(input("Enter the y coordinates of this ship (1-9): "))
            if randshipX < 1 or randshipX > 9 or randshipY < 1 or randshipY > 9:
                print("Invalid coordinates. Please Enter again.")
                continue
            elif randshipX == shipX and randshipY == shipY:
                print("Invalid coordinates, will overlap with your first ship.")
                continue
            else:
                break
        while True:
            randshipOri = str(input("Enter the orientation of this ship (horizontal or vertical): "))
            if randshipOri == "vertical":
                if randshipY + randshipLength > 10:
                    print("Invalid placement, ship will be out of bounds. Try again")
                    continue
                else:
                    break
            elif randshipOri == "horizontal":
                if randshipX + randshipLength > 10:
                    print("Invalid placement, ship will be out of bounds. Try again")
                    continue
                else:
                    break
            elif randshipOri != "horizontal" or randshipOri != "vertical":
                print("Invalid input. Please Enter again.")
                continue
            else:
                break

        # Place the randship temporarily
        temp_board = [row[:] for row in board]  # Copy board
        def placeship_temp(startX, length, startY, Ori, temp_board):
            clash = False
            if Ori == "horizontal": 
                for i in range(startX, startX + length):
                    if temp_board[startY][i] == 'S':
                        clash = True
                        break
                if not clash:
                    for i in range(startX, startX + length):
                        temp_board[startY][i] = 'S'
            elif Ori == "vertical":
                for i in range(startY, startY + length):
                    if temp_board[i][startX] == 'S':
                        clash = True
                        break
                if not clash:
                    for i in range(startY, startY + length):
                        temp_board[i][startX] = 'S'
            return clash, temp_board

        clash, new_board = placeship_temp(randshipX, randshipLength, randshipY, randshipOri, temp_board)
        if clash:
            print("Your ships are overlapping. Try again.")
            continue  # redo the entire randship input
        else:
            board = new_board         # replace original board with new board
            printboard(board)
            break
         
    # attack phase        


    break

        

        





    
    
        



         

    
           
    
