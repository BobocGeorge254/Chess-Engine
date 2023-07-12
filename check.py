import moves
import table


def getPiece(dx, dy, Map):
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
    piece = getPiece(*startSquare, Map)

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


def isWhiteInCheck(Map):
    opponentMoves = moves.getAllAttackingMoves(Map, "Black")
    whiteKingPosition = (0, 0)
    for i in range(9):
        for j in range(9):
            if Map[i][j] == "WhiteKing":
                whiteKingPosition = i, j
                break
        if whiteKingPosition != (0, 0):
            break
    if whiteKingPosition in opponentMoves:
        return True
    return False


def isBlackInCheck(Map):
    opponentMoves = moves.getAllAttackingMoves(Map, "White")
    blackKingPosition = (0, 0)
    for i in range(9):
        for j in range(9):
            if Map[i][j] == "BlackKing":
                blackKingPosition = i, j
                break
        if blackKingPosition != (0, 0):
            break
    if blackKingPosition in opponentMoves:
        return True
    return False


def isCheckmate(Map, turn):
    tempMap = [[piece for piece in row] for row in Map]  # Create a temporary map
    if turn == "White":
        if isWhiteInCheck(tempMap):
            for i in range(1, 9):
                for j in range(1, 9):
                    piece = tempMap[i][j]
                    if piece != 0 and piece.startswith("White"):
                        if "King" not in piece:
                            legalMoves = moves.legalMoves(tempMap, i, j, piece, "White")
                        else:
                            legalMoves = moves.getKingMoves(tempMap, "White", whiteKingMoved=False, blackKingMoved=False)
                            legalMoves = [legalMoves, [0]]
                        for move in legalMoves[0]:
                            # Try making each legal move on the temporary map
                            tempMapCopy = [[piece for piece in row] for row in tempMap]
                            makeMove(i, j, *move, tempMapCopy, 1)
                            if not isWhiteInCheck(tempMapCopy):
                                return False  # At least one legal move avoids check
            return True  # No legal moves found to avoid check
    elif turn == "Black":
        if isBlackInCheck(tempMap):
            for i in range(1, 9):
                for j in range(1, 9):
                    piece = tempMap[i][j]
                    if piece != 0 and piece.startswith("Black"):
                        if "King" not in piece:
                            legalMoves = moves.legalMoves(tempMap, i, j, piece, "Black")
                        else:
                            legalMoves = moves.getKingMoves(tempMap, "Black", whiteKingMoved=False, blackKingMoved=False)
                            legalMoves = [legalMoves, [0]]
                        for move in legalMoves[0]:
                            # Try making each legal move on the temporary map
                            tempMapCopy = [[piece for piece in row] for row in tempMap]
                            makeMove(i, j, *move, tempMapCopy, 1)
                            if not isBlackInCheck(tempMapCopy):
                                return False  # At least one legal move avoids check
            return True  # No legal moves found to avoid check
    return False  # Invalid turn
