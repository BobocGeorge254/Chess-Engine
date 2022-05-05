import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
white = (255,255,255)
black = (153,76,0)
clock = pygame.time.Clock()

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
def Move(startx,starty,stopx,stopy,stringPiece):
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


#Get the piece in a specific square
def getPiece(dx,dy) :
    return Map[dx][dy]


#Actual function to load the board
def PrintMap():
    for i in range(1,9):
        for j in range(1,9):
            if (i + j) % 2 == 0 :
                DrawWhiteSquare(*GetCoordinates(i,j))
            else:
                DrawBlackSquare(*GetCoordinates(i,j))
            if Map[i][j] == 'WhiteRook' :
                DrawPiece(WhiteRook,*GetCoordinates(i,j))
            elif Map[i][j] == 'BlackRook' :
                DrawPiece(BlackRook,*GetCoordinates(i,j))
            elif Map[i][j] == 'WhiteKnight' :
                DrawPiece(WhiteKnight,*GetCoordinates(i,j))
            elif Map[i][j] == 'BlackKnight' :
                DrawPiece(BlackKnight,*GetCoordinates(i,j))
            elif Map[i][j] == 'WhiteBishop' :
                DrawPiece(WhiteBishop,*GetCoordinates(i,j))
            elif Map[i][j] == 'BlackBishop' :
                DrawPiece(BlackBishop,*GetCoordinates(i,j))
            elif Map[i][j] == 'WhiteQueen' :
                DrawPiece(WhiteQueen,*GetCoordinates(i,j))
            elif Map[i][j] == 'BlackQueen' :
                DrawPiece(BlackQueen,*GetCoordinates(i,j))
            elif Map[i][j] == 'WhiteKing' :
                DrawPiece(WhiteKing,*GetCoordinates(i,j))
            elif Map[i][j] == 'BlackKing' :
                DrawPiece(BlackKing,*GetCoordinates(i,j))
            elif Map[i][j] == 'WhitePawn' :
                DrawPiece(WhitePawn,*GetCoordinates(i,j))
            elif Map[i][j] == 'BlackPawn' :
                DrawPiece(BlackPawn,*GetCoordinates(i,j))

def FlipMap():
    for i in range(1,9):
        for j in range(1,9):
            if (i + j) % 2 == 1 :
                DrawWhiteSquare(*GetCoordinates(i,j))
            else:
                DrawBlackSquare(*GetCoordinates(i,j))
            if Map[i][j] == 'WhiteRook' :
                DrawPiece(WhiteRook,*GetCoordinates(i,9 - j))
            elif Map[i][j] == 'BlackRook' :
                DrawPiece(BlackRook,*GetCoordinates(i,9 - j))
            elif Map[i][j] == 'WhiteKnight' :
                DrawPiece(WhiteKnight,*GetCoordinates(i,9 - j))
            elif Map[i][j] == 'BlackKnight' :
                DrawPiece(BlackKnight,*GetCoordinates(i,9-j))
            elif Map[i][j] == 'WhiteBishop' :
                DrawPiece(WhiteBishop,*GetCoordinates(i,9-j))
            elif Map[i][j] == 'BlackBishop' :
                DrawPiece(BlackBishop,*GetCoordinates(i,9-j))
            elif Map[i][j] == 'WhiteQueen' :
                DrawPiece(WhiteQueen,*GetCoordinates(i,9-j))
            elif Map[i][j] == 'BlackQueen' :
                DrawPiece(BlackQueen,*GetCoordinates(i,9-j))
            elif Map[i][j] == 'WhiteKing' :
                DrawPiece(WhiteKing,*GetCoordinates(i,9-j))
            elif Map[i][j] == 'BlackKing' :
                DrawPiece(BlackKing,*GetCoordinates(i,9-j))
            elif Map[i][j] == 'WhitePawn' :
                DrawPiece(WhitePawn,*GetCoordinates(i,9-j))
            elif Map[i][j] == 'BlackPawn' :
                DrawPiece(BlackPawn,*GetCoordinates(i,9-j))

#Draw a dot to suggest moves
def DrawDot(dx,dy):
    pygame.draw.circle(screen, (32,32,32), (GetCoordinates(dx,dy)[0] + 30,GetCoordinates(dx,dy)[1] + 30),10)

#For the text
font = pygame.font.Font('freesansbold.ttf',32)
def show_turn(turn,dx,dy):
    player = font.render(turn, True, white)
    screen.blit(player,(dx,dy))


def ShowAvailableMoves(piece, dx, dy):
    ListOfMoves = []
    if piece.find("Pawn") :
        DrawDot(dx,dy+1)
        ListOfMoves.append((dx,dy+1))
    return ListOfMoves


current_white_time = current_black_time = currentTime = 0
def DisplayTimeWhite():
    current_white_time = pygame.time.get_ticks()
    score_surf = font.render(f'{100-int(current_white_time/1000)} : 00',False,(255,255,255))
    score_rect = score_surf.get_rect(center = (70,100))
    screen.blit(score_surf,score_rect)

def DisplayTimeBlack():
    current_black_time = pygame.time.get_ticks()
    score_surf = font.render(f'{100-int(current_black_time/1000)} : 00',False,(255,255,255))
    score_rect = score_surf.get_rect(center = (70,500))
    screen.blit(score_surf,score_rect)

#Game loop
startx = starty = stopx = stopy = 150
y = WhitePawn
x = "WhitePawn"
running = True
clicked = False
MoveCounter = 0
buttonPressTime = 0
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN :
            (startx,starty) = pygame.mouse.get_pos()
            currentPiece = getPiece(*toSquare(startx, starty))
            #print(ShowAvailableMoves(currentPiece, *toSquare(startx, starty)))
            clicked = True
        elif event.type == pygame.MOUSEBUTTONUP :
            (stopx,stopy) = pygame.mouse.get_pos()
            if toSquare(startx, starty) != toSquare(stopx, stopy) :
                Move(*toSquare(startx, starty), *toSquare(stopx, stopy), currentPiece)
                MoveCounter = MoveCounter + 1
                buttonPressTime = pygame.time.get_ticks()
    screen.fill((16, 16, 16))
    DrawTable()
    if clicked is False :
        DrawInitialState()
    else :
        PrintMap()
    if MoveCounter & 1 == 0 :
        show_turn("White to move", 275,20)
        DisplayTimeWhite()
        #FlipMap()
    else :
        show_turn("Black to move", 275,560)
        DisplayTimeBlack()
    clock.tick(60)
    pygame.display.update()

pygame.quit()
