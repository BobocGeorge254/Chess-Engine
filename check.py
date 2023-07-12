import moves


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


