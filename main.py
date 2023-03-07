import copy
import pygame
import DetLegalMove

pygame.init()
screen = pygame.display.set_mode((800,600))
white = (255,255,255)
black = (153,76,0)
clock = pygame.time.Clock()
xWhiteKing = xBlackKing = 4
yWhiteKing = 1
yBlackKing = 8
WhiteInCheck = BlackInCheck = False
WhiteOutOfCheck = BlackOutOfCheck = True
startx = starty = stopx = stopy = 150
running = True
clicked = False
MoveCounter = 0
buttonPressTime = 0

#Title and icon
pygame.display.set_caption("Chess.com")
icon = pygame.image.load("chess.png")
pygame.display.set_icon(icon)
BlackKingMoved = WhiteKingMoved = False

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
    if "King" in stringPiece :
        if "White" in stringPiece :
            xWhiteKing = stopx
            yWhiteKing = stopy
            WhiteKingMoved = True
        else :
            xBlackKing = stopx
            yBlackKing = stopy
            BlackKingMoved = True
    if (Color[startx - 1][starty - 1] == "White") :
        DrawWhiteSquare(*GetCoordinates(startx,starty))
    else :
        DrawBlackSquare(*GetCoordinates(startx, starty))
    Map[startx][starty] = 0
    PawnPromotion = False
    if "Pawn" in stringPiece :
        if stopy == 1 :
            Map[stopx][stopy] = "BlackQueen"
            PawnPromotion = True
        elif stopy == 8 :
            Map[stopx][stopy] = "WhiteQueen"
            PawnPromotion = True
    if PawnPromotion is False :
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


'''
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
'''


def Inside(dx,dy) :
    return dx >= 1 and dx <= 8 and dy >= 1 and dy <= 8

def LegalMoves(startx, starty,currentPiece):
    List = []

    #Rook
    if "Rook" in currentPiece :
        copyStartx = startx
        copyStarty = starty

        if Inside(startx + 1, starty) and Map[startx + 1][starty] == 0 :
            while Inside(startx + 1, starty) and Map[startx + 1][starty] == 0 :
                List.append((startx + 1,starty))
                startx = startx + 1
        if MoveCounter % 2 == 0 and Inside(startx + 1, starty) and Map[startx + 1][starty][0] == 'B' :
            List.append((startx + 1, starty))
        if MoveCounter % 2 == 1 and Inside(startx + 1, starty) and Map[startx + 1][starty][0] == 'W' :
            List.append((startx + 1, starty))

        startx = copyStartx
        starty = copyStarty
        if Inside(startx - 1, starty) and Map[startx - 1][starty] == 0 :
            while (Inside(startx - 1, starty) and Map[startx - 1][starty] == 0) :
                List.append((startx - 1,starty))
                startx = startx - 1
        if MoveCounter % 2 == 0 and Inside(startx - 1, starty) and Map[startx - 1][starty][0] == 'B' :
            List.append((startx - 1, starty))
        if MoveCounter % 2 == 1 and Inside(startx - 1, starty) and Map[startx - 1][starty][0] == 'W' :
            List.append((startx - 1, starty))


        startx = copyStartx
        starty = copyStarty
        if Inside(startx, starty + 1) and Map[startx][starty + 1] == 0 :
            while (Inside(startx, starty + 1) and Map[startx][starty + 1] == 0) :
                List.append((startx,starty + 1))
                starty = starty + 1
        if MoveCounter % 2 == 0 and Inside(startx, starty + 1) and Map[startx][starty + 1][0] == 'B':
            List.append((startx, starty + 1))
        if MoveCounter % 2 == 1 and Inside(startx, starty + 1) and Map[startx][starty + 1][0] == 'W':
            List.append((startx, starty + 1))

        startx = copyStartx
        starty = copyStarty
        if Inside(startx, starty - 1) and Map[startx][starty - 1] == 0 :
            while (Inside(startx, starty - 1) and Map[startx][starty - 1] == 0) :
                List.append((startx,starty - 1))
                starty = starty - 1
        if MoveCounter % 2 == 0 and Inside(startx, starty - 1) and Map[startx][starty - 1][0] == 'B':
            List.append((startx, starty - 1))
        if MoveCounter % 2 == 1 and Inside(startx, starty - 1) and Map[startx][starty - 1][0] == 'W':
            List.append((startx, starty - 1))

        return List

    #Bishop
    if "Bishop" in currentPiece:
        copyStartx = startx
        copyStarty = starty

        if Inside(startx + 1, starty + 1) and Map[startx + 1][starty + 1] == 0:
            while Inside(startx + 1, starty + 1) and Map[startx + 1][starty + 1] == 0:
                List.append((startx + 1, starty + 1))
                startx = startx + 1
                starty = starty + 1
        if MoveCounter % 2 == 0 and Inside(startx + 1, starty + 1) and Map[startx + 1][starty + 1][0] == 'B':
            List.append((startx + 1, starty + 1))
        if MoveCounter % 2 == 1 and Inside(startx + 1, starty + 1) and Map[startx + 1][starty + 1][0] == 'W':
            List.append((startx + 1, starty + 1))

        startx = copyStartx
        starty = copyStarty
        if Inside(startx + 1, starty - 1) and Map[startx + 1][starty - 1] == 0:
            while Inside(startx + 1, starty - 1) and Map[startx + 1][starty - 1] == 0:
                List.append((startx + 1, starty - 1))
                startx = startx + 1
                starty = starty - 1
        if MoveCounter % 2 == 0 and Inside(startx + 1, starty - 1) and Map[startx + 1][starty - 1][0] == 'B':
            List.append((startx + 1, starty - 1))
        if MoveCounter % 2 == 1 and Inside(startx + 1, starty - 1) and Map[startx + 1][starty - 1][0] == 'W':
            List.append((startx + 1, starty - 1))

        startx = copyStartx
        starty = copyStarty
        if Inside(startx - 1, starty + 1) and Map[startx - 1][starty + 1] == 0:
            while Inside(startx - 1, starty + 1) and Map[startx - 1][starty + 1] == 0:
                List.append((startx - 1, starty + 1))
                startx = startx - 1
                starty = starty + 1
        if MoveCounter % 2 == 0 and Inside(startx - 1, starty + 1) and Map[startx - 1][starty + 1][0] == 'B':
            List.append((startx - 1, starty + 1))
        if MoveCounter % 2 == 1 and Inside(startx - 1, starty + 1) and Map[startx - 1][starty + 1][0] == 'W':
            List.append((startx - 1, starty + 1))

        startx = copyStartx
        starty = copyStarty
        if Inside(startx - 1, starty - 1) and Map[startx - 1][starty - 1] == 0:
            while Inside(startx - 1, starty - 1) and Map[startx - 1][starty - 1] == 0:
                List.append((startx - 1, starty - 1))
                startx = startx - 1
                starty = starty - 1
        if MoveCounter % 2 == 0 and Inside(startx - 1, starty - 1) and Map[startx - 1][starty - 1][0] == 'B':
            List.append((startx - 1, starty - 1))
        if MoveCounter % 2 == 1 and Inside(startx - 1, starty - 1) and Map[startx - 1][starty - 1][0] == 'W':
            List.append((startx - 1, starty - 1))

        return List

    if "Knight" in currentPiece :
        copyStartx = startx
        copyStarty = starty
        Knight = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]
        for Move in Knight :
            startx = copyStartx
            starty = copyStarty
            if Inside(startx + Move[0], starty + Move[1]) and Map[startx + Move[0]][starty + Move[1]] == 0:
                List.append((startx + Move[0], starty + Move[1]))
            elif MoveCounter % 2 == 0 and Inside(startx + Move[0], starty + Move[1]) and Map[startx + Move[0]][starty + Move[1]][0] == 'B':
                List.append((startx + Move[0], starty + Move[1]))
            elif MoveCounter % 2 == 1 and Inside(startx + Move[0], starty + Move[1]) and Map[startx + Move[0]][starty + Move[1]][0] == 'W':
                List.append((startx + Move[0], starty + Move[1]))

        return List

    #Queen treated as both a Bishop and a Rook
    if "Queen" in currentPiece :
        return LegalMoves(startx,starty,currentPiece[0:5] + "Bishop") + LegalMoves(startx,starty,currentPiece[0:5] + "Rook")

    if "Pawn" in currentPiece :
        copyStartx = startx
        copyStarty = starty

        #First Move
        if MoveCounter % 2 == 0 and starty == 2 :
            if Map[startx][starty + 1] == 0:
                List.append( (startx, starty + 1) )
            if Map[startx][starty + 2] == 0:
                List.append( (startx, starty + 2) )
        elif MoveCounter % 2 == 1 and starty == 7 :
            if Map[startx][starty - 1] == 0:
                List.append( (startx, starty - 1) )
            if Map[startx][starty - 2] == 0:
                List.append( (startx, starty - 2) )

        #Every other move
        else :
            if MoveCounter % 2 == 0 :
                if Inside(startx, starty + 1) and Map[startx][starty + 1] == 0 :
                    List.append( (startx, starty + 1) )
                if Inside(startx + 1, starty + 1) and Map[startx + 1][starty + 1] != 0 and Map[startx + 1][starty + 1][0] == 'B' :
                    List.append( (startx + 1, starty + 1))
                if Inside(startx - 1, starty + 1) and Map[startx - 1][starty + 1] != 0 and Map[startx - 1][starty + 1][0] == 'B' :
                    List.append( (startx - 1, starty + 1))

            if MoveCounter % 2 == 1 :
                if Inside(startx, starty - 1) and Map[startx][starty - 1] == 0 :
                    List.append( (startx, starty - 1) )
                if Inside(startx + 1, starty - 1) and Map[startx + 1][starty - 1] != 0 and Map[startx + 1][starty - 1][0] == 'W' :
                    List.append( (startx + 1, starty - 1))
                if Inside(startx - 1, starty - 1) and Map[startx - 1][starty - 1] != 0 and Map[startx - 1][starty - 1][0] == 'W' :
                    List.append( (startx - 1, starty - 1))

        #Pawn promotion took care in Move function

    return List




#Boolean returing if a move is okay or not
def LegalMove(startx, starty, stopx, stopy, currentPiece, MoveCounter) :
    #Test if the square is free
    if MoveCounter % 2 == 1 :
        if Map[stopx][stopy] != 0 :
            if Map[stopx][stopy][0] == 'B' :
                return False
    if MoveCounter % 2 == 0 :
        if Map[stopx][stopy] != 0 :
            if Map[stopx][stopy][0] == "W":
                return False


    #Test if the moved was played by the correct player
    if MoveCounter % 2 == 1 :
        if currentPiece[0] == 'W' :
            return False
    else :
        if currentPiece[0] == 'B' :
            return False

    #Handle The King
    if "King" in currentPiece :
        if stopy == 1 and stopx == 2 and Map[4][1] == 'WhiteKing' and Map[1][1] == 'WhiteRook' :
            if Map[2][1] == 0 and Map[3][1] == 0 and WhiteKingMoved == False :
                Map[1][1] = Map[4][1] = 0
                Map[2][1] = 'WhiteKing'
                Map[3][1] = 'WhiteRook'
                return 'Castle'
        if stopy == 1 and stopx == 6 and Map[4][1] == 'WhiteKing' and Map[8][1] == 'WhiteRook' :
            if Map[5][1] == 0 and Map[6][1] == 0 and Map[7][1] == 0 and WhiteKingMoved == False :
                Map[8][1] = Map[4][1] = 0
                Map[6][1] = 'WhiteKing'
                Map[5][1] = 'WhiteRook'
                return 'Castle'
        if stopy == 8 and stopx == 2 and Map[4][8] == 'BlackKing' and Map[1][8] == 'BlackRook' :
            if Map[2][8] == 0 and Map[3][8] == 0 and BlackKingMoved == False :
                Map[1][8] = Map[4][8] = 0
                Map[2][8] = 'BlackKing'
                Map[3][8] = 'BlackRook'
                return 'Castle'
        if stopy == 8 and stopx == 6 and Map[4][8] == 'BlackKing' and Map[8][8] == 'BlackRook' :
            if Map[5][8] == 0 and Map[6][8] == 0 and Map[7][8] == 0 and BlackKingMoved == False :
                Map[8][8] = Map[4][8] = 0
                Map[6][8] = 'BlackKing'
                Map[5][8] = 'BlackRook'
                return 'Castle'
        if abs(startx - stopx) > 1 or abs(starty - stopy) > 1:
            return False

    #Handle The Rooks
    if "Rook" in currentPiece :
        ListOfMoves = LegalMoves(startx,starty,currentPiece)
        if ((stopx, stopy) not in ListOfMoves) :
            return False

    #Handle The Bishops
    if "Bishop" in currentPiece :
        ListOfMoves = LegalMoves(startx,starty,currentPiece)
        if ((stopx, stopy) not in ListOfMoves) :
            return False

    #Handle The Queen
    if "Queen" in currentPiece :
        ListOfMoves = LegalMoves(startx,starty,currentPiece)
        if ((stopx, stopy) not in ListOfMoves) :
            return False

    #Handle The Knight
    if "Knight" in currentPiece :
        ListOfMoves = LegalMoves(startx, starty, currentPiece)
        if ((stopx, stopy) not in ListOfMoves) :
            return False

    #Handle The Pawns
    if "Pawn" in currentPiece :
        ListOfMoves = LegalMoves(startx, starty, currentPiece)
        if ((stopx, stopy) not in ListOfMoves) :
            return False

    return True

def WhiteInCheck(stopx,stopy,currentPiece) :
    if ((xWhiteKing, yWhiteKing) in LegalMoves(*toSquare(stopx, stopy), currentPiece)):
        return True
    return False

def BlackInCheck(stopx,stopy,currentPiece) :
    if ((xBlackKing, yBlackKing) in LegalMoves(*toSquare(stopx, stopy), currentPiece)):
        return True
    return False


#Game loop
y = WhitePawn
x = "WhitePawn"
CheckState = []
whiteInCheck = False
blackInCheck = False


while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN :
            (startx,starty) = pygame.mouse.get_pos()
            currentPiece = getPiece(*toSquare(startx, starty))
            clicked = True
        elif event.type == pygame.MOUSEBUTTONUP :
            (stopx,stopy) = pygame.mouse.get_pos()
            if toSquare(startx, starty) != toSquare(stopx, stopy) \
                    and LegalMove(*toSquare(startx, starty), *toSquare(stopx, stopy), currentPiece, MoveCounter) is True \
                        and whiteInCheck is False and blackInCheck is False :

                Move(*toSquare(startx, starty), *toSquare(stopx, stopy), currentPiece)
                if (xWhiteKing, yWhiteKing) in DetLegalMove.GetAllLegalMoves(Map,"Black")  :
                    whiteInCheck = True
                if (xBlackKing, yBlackKing) in DetLegalMove.GetAllLegalMoves(Map, "White") :
                    blackInCheck = True
                MoveCounter = MoveCounter + 1
                buttonPressTime = pygame.time.get_ticks()
                #print(DetLegalMove.GetAllLegalMoves(Map, "Black"))
            if toSquare(startx, starty) != toSquare(stopx, stopy) and LegalMove(*toSquare(startx, starty), *toSquare(stopx, stopy), currentPiece, MoveCounter) is True \
                    and WhiteInCheck == True :
                while ((xWhiteKing, yWhiteKing) in DetLegalMove.GetAllLegalMoves(Map,"Black")) :
                    print("White Checked")
                    (stopx, stopy) = pygame.mouse.get_pos()
                    MapSave = copy.deepcopy(Map)
                    Move(*toSquare(startx,starty),*toSquare(stopx,stopy),currentPiece)
                    if ((xWhiteKing, yWhiteKing) not in DetLegalMove.GetAllLegalMoves(Map,"Black")) :
                        WhiteOutOfCheck = True
                        WhiteInCheck = False
                        break
                    Map = copy.deepcopy(MapSave)
                MoveCounter = MoveCounter + 1
            if toSquare(startx,starty) != toSquare(stopx,stopy) and LegalMove(*toSquare(startx, starty), *toSquare(stopx, stopy), currentPiece, MoveCounter) == 'Castle' :
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
        #FlipMap()
    else :
        show_turn("Black to move", 275,560)
    pygame.display.update()

pygame.quit()
