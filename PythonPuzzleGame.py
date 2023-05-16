#Juego en una consola
import random
import time

width = 10
height = 10

playerX = int(width * 0.5)
playerY = int(height * 0.5)

#Esto es una Multidimensional array, ni puta idea de como esta declarada pero esta ahy.
gridValue = [[0] * width for _ in range(height)]

#Generate Floor Hole
gridValue[1][1] = 4

GameOver = False

def GenerateGrid():
    x = 0
    y = 0
    while(x < width):
        while(y < height):
          
            if(x == 0 or y == 0 or x == width -1 or y == height -1):    #Wall
                symbol = "#"
                gridValue[x][y] = 1 
                
            elif(x == playerX and y == playerY):    #Player
                symbol = "@"
                gridValue[x][y] = 2 
                
            elif(GetGridValue(x, y) == 3):  #Box
                symbol = "O"
                gridValue[x][y] = 3 
                
            elif(GetGridValue(x, y) == 4):  #Floor Hole / Box Target
                symbol = "X"
                gridValue[x][y] = 4 
                
            else:
                gridValue[x][y] = 0 #Air
                symbol = "·"
            
            print(symbol, end=" ")
            y += 1
        print()
        x += 1
        y = 0

def EndGame():
    global GameOver
    GameOver = True
    
    #Game over Animation
    """
    #Dosent work
    x = 0
    y = 0
    while(x < width):
        while(y < height):
            symbol = "#"
            gridValue[x][y] = 1 
            print(symbol, end=" ")
            y += 1
            
            GenerateGrid()
        print()
        x += 1
        y = 0
    """
    print("\nGAME OVER!")

def GenerateBox():
    #Generate Box
    randX = 0
    randY = 0
    
    #The box will be generated in an empty position
    while GetGridValue(randX,randY) != 0:
        randX = random.randint(3, width - 3)
        randY = random.randint(3, height - 3)
        
    gridValue[randX][randY] = 3

def GetGridValue(posX,posY):
    if(posX < 0 or posX >= width or posY < 0 or posY >= height):
        return 0
    return gridValue[posX][posY]

def IsCollidingWithWall(posX,posY):
    if(posX < 0 or posX >= width or posY < 0 or posY >= height):
        return True
    #print(str(gridValue[posX][posY]) + " Coordinates: " + str(posX) + "/" + str(posY) )
    if(gridValue[posX][posY] != 0):
        return True
    else:
        return False

def MoveBox(initialPosX,initialPosY,targetPosX,targetPosY):
    #Is box NOT moving to wall
    if(IsCollidingWithWall(targetPosX, targetPosY) == False):
        gridValue[targetPosX][targetPosY] = 3
        gridValue[initialPosX][initialPosY] = 0
    #Box moved to hole
    elif(GetGridValue(targetPosX, targetPosY) == 4):
        gridValue[targetPosX][targetPosY] = 0
        gridValue[initialPosX][initialPosY] = 0
        GenerateGrid()
        EndGame()

#Initial generation
GenerateGrid()

#generate the box
GenerateBox()

#Game Loop
while GameOver == False:
    #Draw map
    GenerateGrid()
    
    #Player input | desiredX/Y es la direccion en la que se va a mover
    desiredX = 0
    desiredY = 0
    
    playerInput = input().lower()
        
    if(playerInput == "w"):
        desiredX -= 1
    elif(playerInput == "s"):
        desiredX += 1
    elif(playerInput == "d"):
        desiredY += 1
    else:
        desiredY -= 1
    
    #Check collisions
    desiredXPos = playerX + desiredX
    desiredYPos = playerY + desiredY
    
    if(IsCollidingWithWall(desiredXPos, desiredYPos) == False):
        playerX += desiredX
        playerY += desiredY
    
    #Check interactions
    if(GetGridValue(desiredXPos, desiredYPos) == 3):
        MoveBox(desiredXPos,desiredYPos,desiredXPos + desiredX, desiredYPos + desiredY)
