import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
white = (255,255,255)
black = (153,76,0)

#Title and icon
pygame.display.set_caption("Chess.com")
icon = pygame.image.load("chess.png")
pygame.display.set_icon(icon)

#Draw Squares
def DrawWhiteSquare(dx,dy):
    x = pygame.draw.rect(screen, white, (dx,dy,60,60))
    #pygame.display.update()

def DrawBlackSquare(dx,dy):
    pygame.draw.rect(screen, black, (dx,dy,60,60))
    #pygame.display.update()

#Draw table
Map = [[0 for i in range(9)] for j in range(9)]
Color = [[0 for i in range(9)] for j in range(9)]
def DrawTable() :
    for i in range(8) :
        for j in range(8) :
            if (i + j) % 2 == 0 :
                Color[i][j] = "White"
                DrawWhiteSquare(i * 60 + 150, j * 60 + 60)
            else :
                Color[i][j] = "Black"
                DrawBlackSquare(i * 60 + 150, j * 60 + 60)

#Get drawing coordinates for a square
def GetCoordinates(line, column) :
    dx = 150 + 60 * (line - 1)
    dy = 60 + 60 * (column - 1)
    return (dx,dy)

#Draw piece
def DrawPiece(pieceImg, dx, dy):
    screen.blit(pieceImg,(dx,dy))

#Define pieces
WhitePawn = pygame.image.load("WhitePawn.png")
BlackPawn = pygame.image.load("BlackPawn.png")

WhiteKnight = pygame.image.load("WhiteKnight.png")
BlackKnight = pygame.image.load("BlackKnight.png")

WhiteBishop = pygame.image.load("WhiteBishop.png")
BlackBishop = pygame.image.load("BlackBishop.png")

WhiteRook = pygame.image.load("WhiteRook.png")
BlackRook = pygame.image.load("BlackRook.png")

WhiteQueen = pygame.image.load("WhiteQueen.png")
BlackQueen = pygame.image.load("BlackQueen.png")

WhiteKing = pygame.image.load("WhiteKing.png")
BlackKing = pygame.image.load("BlackKing.png")

#Draw the initial state
def DrawInitialState():
    #Pawns
    for i in range(1,9):
        DrawPiece(WhitePawn, *GetCoordinates(i, 2))
        DrawPiece(BlackPawn, *GetCoordinates(i, 7))
        Map[i][2] = "WhitePawn"
        Map[i][7] = "BlackPawn"

    #Kings
    DrawPiece(WhiteKing, *GetCoordinates(4, 1))
    DrawPiece(BlackKing, *GetCoordinates(4, 8))
    Map[4][1] = "WhiteKing"
    Map[4][8] = "BlackKing"

    #Queens
    DrawPiece(WhiteQueen, *GetCoordinates(5, 1))
    DrawPiece(BlackQueen, *GetCoordinates(5, 8))
    Map[5][1] = "WhiteQueen"
    Map[5][8] = "BlackQueen"

    #Rooks
    DrawPiece(WhiteRook, *GetCoordinates(1, 1))
    DrawPiece(WhiteRook, *GetCoordinates(8, 1))
    DrawPiece(BlackRook, *GetCoordinates(1, 8))
    DrawPiece(BlackRook, *GetCoordinates(8, 8))
    Map[1][1] = Map[8][1] = "WhiteRook"
    Map[1][8] = Map[8][8] = "BlackRook"

    #Knighs
    DrawPiece(WhiteKnight, *GetCoordinates(2, 1))
    DrawPiece(WhiteKnight, *GetCoordinates(7, 1))
    DrawPiece(BlackKnight, *GetCoordinates(2, 8))
    DrawPiece(BlackKnight, *GetCoordinates(7, 8))
    Map[2][1] = Map[7][1] = "WhiteKnight"
    Map[2][8] = Map[7][8] = "BlackKnight"

    #Bishops
    DrawPiece(WhiteBishop, *GetCoordinates(3, 1))
    DrawPiece(WhiteBishop, *GetCoordinates(6, 1))
    DrawPiece(BlackBishop, *GetCoordinates(3, 8))
    DrawPiece(BlackBishop, *GetCoordinates(6, 8))
    Map[3][1] = Map[6][1] = "WhiteBishop"
    Map[3][8] = Map[6][8] = "BlackBishop"

#Make a move
def Move(piece,startx,starty,stopx,stopy,stringPiece):
    DrawPiece(piece,*GetCoordinates(stopx,stopy))
    if (Color[startx - 1][starty - 1] == "White") :
        DrawWhiteSquare(*GetCoordinates(startx,starty))
    else :
        DrawBlackSquare(*GetCoordinates(startx, starty))
    Map[startx][starty] = 0
    Map[stopx][stopy] = stringPiece

#Get the square of 2 coordinates
def toSquare(dx,dy) :
    x = ( dx - 150 ) / 60 + 1
    y = ( dy - 60 ) / 60 + 1
    return (int(x),int(y))

def getPiece(dx,dy) :
    return Map[dx][dy]

def toSurface(x) :
    if x == "WhitePawn" :
        return WhitePawn
    elif x == "BlackPawn" :
        return BlackPawn
    elif x == "WhiteKing" :
        return WhiteKing
    elif x == "BlackKing" :
        return BlackKing
    elif x == "WhiteQueen":
        return WhiteQueen
    elif x == "BlackQueen":
        return BlackQueen
    elif x == "WhiteRook":
        return WhiteRook
    elif x == "BlackRook":
        return BlackRook
    elif x == "WhiteKnight":
        return WhiteKnight
    elif x == "BlackKnight":
        return BlackKnight
    elif x == "WhiteBishop" :
        return WhiteBishop
    else :
        return BlackBishop

#Game loop
startx = starty = stopx = stopy = 0
y = WhitePawn
x = "WhitePawn"
running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN :
            (startx,starty) = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP :
            (stopx,stopy) = pygame.mouse.get_pos()
            x = getPiece(*toSquare(startx,starty))
            y = toSurface(x)
    screen.fill((16, 16, 16))
    DrawTable()
    DrawInitialState()
    #Move(WhitePawn,4,2,4,4)
    #print(startx,stopx)
    Move(y, *toSquare(startx, starty), *toSquare(stopx, stopy), x)
    pygame.display.update()

pygame.quit()
