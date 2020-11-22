grid = [" " for x in range(10)]

def printGrid(grid):
    print(" " + grid[1] + " | " + grid[2] + " | " + grid[3])
    print("-----------")
    print(" " + grid[4] + " | " + grid[5] + " | " + grid[6])
    print("-----------")
    print(" " + grid[7] + " | " + grid[8] + " | " + grid[9])  
    
def checkFull(grid):
    if grid.count(" ") > 1:
        return False
    else: return True
    
def checkWinner(grid, xo):
    return ((grid[1] == xo and grid[2] == xo and grid[3] == xo) or 
            (grid[4] == xo and grid[5] == xo and grid[6] == xo) or 
            (grid[7] == xo and grid[8] == xo and grid[9] == xo) or
            (grid[1] == xo and grid[4] == xo and grid[7] == xo) or  
            (grid[2] == xo and grid[5] == xo and grid[8] == xo) or 
            (grid[3] == xo and grid[6] == xo and grid[9] == xo) or 
            (grid[1] == xo and grid[5] == xo and grid[9] == xo) or  
            (grid[3] == xo and grid[5] == xo and grid[7] == xo))

def insertXO(xo, position):
    grid[position] = xo
    
def freePosition(position):
    return grid[position] == " "

def playerTurn():
    isRunning = True
    while isRunning:
        choice = input("Please select position for X (1-9): ")
        try:
            choice = int(choice)
            if choice > 0 and choice <10:
                if freePosition(choice):
                    isRunning = False
                    insertXO("x", choice)
                else: print("Sorry this square has already been chosen")
            else: print("Please enter number between 1-9 (inclusive)")
        except:
            print("Please enter a number. ")
            
def chooseRandom(fromHere):
    import random
    length = len(fromHere)
    r = random.randrange(0, length)
    return fromHere[r]
            
def AITurn():
    options = [i for i, entry in enumerate(grid) if entry == " " and i != 0]
    choice = 0
    for symbol in ["o", "x"]:
        for j in options:
            gridClone = grid[:]
            gridClone[j] = symbol
            if checkWinner(gridClone, symbol):
                choice = j
                return choice
    availableCorner = []
    for i in options:
        if i in [1,3,7,9]:
            availableCorner.append(i)
    if len(availableCorner) > 0:
        choice = chooseRandom(availableCorner)
        return choice
    if 5 in options:
        choice = 5
        return choice
    availableEdge = []
    for i in options:
        if i in [2,4,6,8]:
            availableEdge.append(i)
    if len(availableEdge) > 0:
        choice = chooseRandom(availableEdge)
    return choice

def main():
    print("~NOUGHTS & CROSSES~")
    printGrid(grid)
    while not(checkFull(grid)):
        if not(checkWinner(grid, "o")):
            playerTurn()
            printGrid(grid)
        else:
            print("AI has won- You lose! ")
            break
        if not(checkWinner(grid, "x")):
            position = AITurn()
            if position == 0:
                print("It's a draw.")
            else: 
                insertXO("o", position)
                print("\nAI placed an 'O' in square", position, ":")
                printGrid(grid)
        else:
            print("You win!")
            break
    if checkFull(grid): print("You and the AI draw!")
    
main()