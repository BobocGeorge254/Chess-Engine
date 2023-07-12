import pygame

import check
import table
import moves

pygame.init()
screen = pygame.display.set_mode((800, 600))
white = (255, 255, 255)
black = (153, 76, 0)
clock = pygame.time.Clock()
running = True
MoveCounter = 0

# Title and icon
pygame.display.set_caption("Chess.com")
icon = pygame.image.load("Photos/chess.png")
pygame.display.set_icon(icon)


# Draw Squares
def DrawSquare(dx, dy, color):
    pygame.draw.rect(screen, color, (dx, dy, 60, 60))


# Draw table
def DrawTable():
    for i in range(8):
        for j in range(8):
            color = white if (i + j) % 2 == 0 else black
            DrawSquare(i * 60 + 150, j * 60 + 60, color)


def getPiece(dx, dy):
    return Map[dx][dy]


def makeMove(startx, starty, stopx, stopy, Map, flag=0):
    global MoveCounter
    # Get the coordinates of the start and stop squares
    if flag == 0:
        startSquare = table.toSquare(startx, starty)
        stopSquare = table.toSquare(stopx, stopy)
    else:
        startSquare = (startx, starty)
        stopSquare = (stopx, stopy)

    # Get the piece in the start square
    piece = getPiece(*startSquare)

    PawnPromotion = False
    if "Pawn" in piece:
        if stopSquare[0] == 1:
            Map[stopSquare[0]][stopSquare[1]] = "BlackQueen"
            Map[startSquare[0]][startSquare[1]] = 0
            PawnPromotion = True
        elif stopSquare[0] == 8:
            Map[stopSquare[0]][stopSquare[1]] = "WhiteQueen"
            Map[startSquare[0]][startSquare[1]] = 0
            PawnPromotion = True
    if PawnPromotion is False:
        # Check if it's a castling move
        if piece == "WhiteKing" or piece == "BlackKing":
            # Kingside castling
            if startSquare[1] - stopSquare[1] == 2:
                if piece == "WhiteKing":
                    # Move the king
                    Map[stopSquare[0]][stopSquare[1]] = "WhiteKing"
                    Map[startSquare[0]][startSquare[1]] = 0
                    # Move the rook
                    Map[stopSquare[0]][stopSquare[1] + 1] = "WhiteRook"
                    Map[startSquare[0]][stopSquare[1] - 1] = 0
                else:
                    # Move the king
                    Map[stopSquare[0]][stopSquare[1]] = "BlackKing"
                    Map[startSquare[0]][startSquare[1]] = 0
                    # Move the rook
                    Map[stopSquare[0]][stopSquare[1] + 1] = "BlackRook"
                    Map[startSquare[0]][stopSquare[1] - 1] = 0
            elif stopSquare[1] - startSquare[1] == 2:
                if piece == "WhiteKing":
                    # Move the king
                    Map[stopSquare[0]][stopSquare[1]] = "WhiteKing"
                    Map[startSquare[0]][startSquare[1]] = 0
                    # Move the rook
                    Map[stopSquare[0]][stopSquare[1] - 1] = "WhiteRook"
                    Map[startSquare[0]][stopSquare[1] + 2] = 0
                else:
                    # Move the king
                    Map[stopSquare[0]][stopSquare[1]] = "BlackKing"
                    Map[startSquare[0]][startSquare[1]] = 0
                    # Move the rook
                    Map[stopSquare[0]][stopSquare[1] - 1] = "BlackRook"
                    Map[startSquare[0]][stopSquare[1] + 2] = 0
            else:
                Map[stopSquare[0]][stopSquare[1]] = piece
                Map[startSquare[0]][startSquare[1]] = 0
        # Regular move
        else:
            Map[stopSquare[0]][stopSquare[1]] = piece
            Map[startSquare[0]][startSquare[1]] = 0


def isCheckmate(Map, turn):
    tempMap = [[piece for piece in row] for row in Map]  # Create a temporary map
    if turn == "White":
        if check.isWhiteInCheck(tempMap):
            for i in range(1, 9):
                for j in range(1, 9):
                    piece = tempMap[i][j]
                    if piece != 0 and piece.startswith("White"):
                        if "King" not in piece:
                            legalMoves = moves.legalMoves(tempMap, i, j, piece, "White")
                        else:
                            legalMoves = moves.getKingMoves(tempMap, "White")
                            legalMoves = [legalMoves, [0]]
                        for move in legalMoves[0]:
                            # Try making each legal move on the temporary map
                            tempMapCopy = [[piece for piece in row] for row in tempMap]
                            makeMove(i, j, *move, tempMapCopy, 1)
                            if not check.isWhiteInCheck(tempMapCopy):
                                return False  # At least one legal move avoids check
            return True  # No legal moves found to avoid check
    elif turn == "Black":
        if check.isBlackInCheck(tempMap):
            for i in range(1, 9):
                for j in range(1, 9):
                    piece = tempMap[i][j]
                    if piece != 0 and piece.startswith("Black"):
                        if "King" not in piece:
                            legalMoves = moves.legalMoves(tempMap, i, j, piece, "Black")
                        else:
                            legalMoves = moves.getKingMoves(tempMap, "Black")
                            legalMoves = [legalMoves, [0]]
                        for move in legalMoves[0]:
                            # Try making each legal move on the temporary map
                            tempMapCopy = [[piece for piece in row] for row in tempMap]
                            makeMove(i, j, *move, tempMapCopy, 1)
                            if not check.isBlackInCheck(tempMapCopy):
                                return False  # At least one legal move avoids check
            return True  # No legal moves found to avoid check
    return False  # Invalid turn




# Game loop
Map = [[0 for _ in range(9)] for _ in range(9)]
clicked = False


while running:
    moveMade = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (startx, starty) = pygame.mouse.get_pos()
            clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            (stopx, stopy) = pygame.mouse.get_pos()
            turn = "White" if MoveCounter % 2 == 0 else "Black"
            destinationSquare = table.toSquare(stopx, stopy)
            startingSquare = table.toSquare(startx, starty)
            if (
                    destinationSquare in moves.legalMoves(Map, *startingSquare, getPiece(*startingSquare), turn)[0]) \
                    or ("King" in getPiece(*startingSquare) and destinationSquare in moves.getKingMoves(Map, turn)
            ):
                tempMap = [[piece for piece in row] for row in Map]
                makeMove(startx, starty, stopx, stopy, tempMap)
                if (
                        ("White" in turn and not check.isWhiteInCheck(tempMap))
                        or ("Black" in turn and not check.isBlackInCheck(tempMap))
                ):
                    makeMove(startx, starty, stopx, stopy, Map)
                    MoveCounter += 1  # Increment the move counter
                    moveMade = True
                    if isCheckmate(Map, "White") or isCheckmate(Map, "Black"):
                        print("Checkmate")

    screen.fill((16, 16, 16))
    DrawTable()

    if clicked is False:
        table.DrawInitialState(screen, Map)
    else:
        table.PrintMap(screen, Map)

    table.showCurrentTurn(screen, MoveCounter)
    pygame.display.update()
    if moveMade:
        continue

pygame.quit()
