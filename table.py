import pygame
import pieces

white = (255, 255, 255)
black = (153, 76, 0)


# Draw Squares
def DrawWhiteSquare(screen, dx, dy):
    pygame.draw.rect(screen, white, (dx, dy, 60, 60))


def DrawBlackSquare(screen, dx, dy):
    pygame.draw.rect(screen, black, (dx, dy, 60, 60))


def GetCoordinates(line, column):
    dx = 150 + 60 * (column - 1)
    dy = 60 + 60 * (line - 1)
    return dx, dy


# Draw table
def DrawTable(screen):
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                DrawWhiteSquare(screen, i * 60 + 150, j * 60 + 60)
            else:
                DrawBlackSquare(screen, i * 60 + 150, j * 60 + 60)


# Get the square of 2 coordinates
def toSquare(dx, dy):
    x = (dy - 60) // 60 + 1  # Row index
    y = (dx - 150) // 60 + 1  # Column index
    return x, y


# Draw piece
def DrawPiece(screen, pieceImg, dx, dy):
    screen.blit(pieceImg, (dx, dy))


# Draw the initial state
def DrawInitialState(screen, Map):
    # Pawns
    for i in range(1, 9):
        DrawPiece(screen, pieces.WhitePawn, *GetCoordinates(2, i))
        DrawPiece(screen, pieces.BlackPawn, *GetCoordinates(7, i))
        Map[2][i] = "WhitePawn"
        Map[7][i] = "BlackPawn"

    # Kings
    DrawPiece(screen, pieces.WhiteKing, *GetCoordinates(1, 4))
    DrawPiece(screen, pieces.BlackKing, *GetCoordinates(8, 4))
    Map[1][4] = "WhiteKing"
    Map[8][4] = "BlackKing"

    # Queens
    DrawPiece(screen, pieces.WhiteQueen, *GetCoordinates(1, 5))
    DrawPiece(screen, pieces.BlackQueen, *GetCoordinates(8, 5))
    Map[1][5] = "WhiteQueen"
    Map[8][5] = "BlackQueen"

    # Rooks
    DrawPiece(screen, pieces.WhiteRook, *GetCoordinates(1, 1))
    DrawPiece(screen, pieces.WhiteRook, *GetCoordinates(1, 8))
    DrawPiece(screen, pieces.BlackRook, *GetCoordinates(8, 1))
    DrawPiece(screen, pieces.BlackRook, *GetCoordinates(8, 8))
    Map[1][1] = Map[1][8] = "WhiteRook"
    Map[8][1] = Map[8][8] = "BlackRook"

    # Knights
    DrawPiece(screen, pieces.WhiteKnight, *GetCoordinates(1, 2))
    DrawPiece(screen, pieces.WhiteKnight, *GetCoordinates(1, 7))
    DrawPiece(screen, pieces.BlackKnight, *GetCoordinates(8, 2))
    DrawPiece(screen, pieces.BlackKnight, *GetCoordinates(8, 7))
    Map[1][2] = Map[1][7] = "WhiteKnight"
    Map[8][2] = Map[8][7] = "BlackKnight"

    # Bishops
    DrawPiece(screen, pieces.WhiteBishop, *GetCoordinates(1, 3))
    DrawPiece(screen, pieces.WhiteBishop, *GetCoordinates(1, 6))
    DrawPiece(screen, pieces.BlackBishop, *GetCoordinates(8, 3))
    DrawPiece(screen, pieces.BlackBishop, *GetCoordinates(8, 6))
    Map[1][3] = Map[1][6] = "WhiteBishop"
    Map[8][3] = Map[8][6] = "BlackBishop"


# Print the map
def PrintMap(screen, Map):
    for i in range(1, 9):
        for j in range(1, 9):
            if (i + j) % 2 == 0:
                DrawWhiteSquare(screen, *GetCoordinates(i, j))
            else:
                DrawBlackSquare(screen, *GetCoordinates(i, j))
            piece = Map[i][j]
            if piece:
                DrawPiece(screen, pieces.pieceImages[piece], *GetCoordinates(i, j))


# Show turn
def show_turn(screen, turn, dx, dy):
    font = pygame.font.Font('freesansbold.ttf', 32)
    player = font.render(turn, True, white)
    screen.blit(player, (dx, dy))


def showCurrentTurn(screen, moveCounter):
    if moveCounter % 2 == 0:
        show_turn(screen, "White to move", 275, 20)
    else:
        show_turn(screen, "Black to move", 275, 560)
