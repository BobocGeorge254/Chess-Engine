import copy

import pin


def Inside(dx, dy):
    return 1 <= dx <= 8 and 1 <= dy <= 8


def getPiece(dx, dy, Map):
    return Map[dx][dy]


def findPiece(piece, Map):
    for i in range(1, 9):
        for j in range(1, 9):
            if getPiece(i, j, Map) == piece:
                return i, j
    return None


def legalMoves(Map, startx, starty, currentPiece, turn):
    #currentPiece = getPiece(startx, starty, Map)
    List = []

    if currentPiece == 0:
        return []

    ListPin = pin.isPiecePinned(startx, starty, Map)
    # Rook
    if "Rook" in currentPiece:
        copyStartx = startx
        copyStarty = starty

        if Inside(startx + 1, starty) and Map[startx + 1][starty] == 0:
            while Inside(startx + 1, starty) and Map[startx + 1][starty] == 0:
                List.append((startx + 1, starty))
                startx = startx + 1
        if turn == "White" and Inside(startx + 1, starty) and Map[startx + 1][starty].startswith("Black"):
            List.append((startx + 1, starty))
        if turn == "Black" and Inside(startx + 1, starty) and Map[startx + 1][starty].startswith("White"):
            List.append((startx + 1, starty))

        startx = copyStartx
        starty = copyStarty
        if Inside(startx - 1, starty) and Map[startx - 1][starty] == 0:
            while Inside(startx - 1, starty) and Map[startx - 1][starty] == 0:
                List.append((startx - 1, starty))
                startx = startx - 1
        if turn == "White" and Inside(startx - 1, starty) and Map[startx - 1][starty].startswith("Black"):
            List.append((startx - 1, starty))
        if turn == "Black" and Inside(startx - 1, starty) and Map[startx - 1][starty].startswith("White"):
            List.append((startx - 1, starty))

        startx = copyStartx
        starty = copyStarty
        if Inside(startx, starty + 1) and Map[startx][starty + 1] == 0:
            while Inside(startx, starty + 1) and Map[startx][starty + 1] == 0:
                List.append((startx, starty + 1))
                starty = starty + 1
        if turn == "White" and Inside(startx, starty + 1) and Map[startx][starty + 1].startswith("Black"):
            List.append((startx, starty + 1))
        if turn == "Black" and Inside(startx, starty + 1) and Map[startx][starty + 1].startswith("White"):
            List.append((startx, starty + 1))

        startx = copyStartx
        starty = copyStarty
        if Inside(startx, starty - 1) and Map[startx][starty - 1] == 0:
            while Inside(startx, starty - 1) and Map[startx][starty - 1] == 0:
                List.append((startx, starty - 1))
                starty = starty - 1
        if turn == "White" and Inside(startx, starty - 1) and Map[startx][starty - 1].startswith("Black"):
            List.append((startx, starty - 1))
        if turn == "Black" and Inside(startx, starty - 1) and Map[startx][starty - 1].startswith("White"):
            List.append((startx, starty - 1))

        # Bishop
    if "Bishop" in currentPiece:
        copyStartx = startx
        copyStarty = starty

        if Inside(startx + 1, starty + 1) and Map[startx + 1][starty + 1] == 0:
            while Inside(startx + 1, starty + 1) and Map[startx + 1][starty + 1] == 0:
                List.append((startx + 1, starty + 1))
                startx = startx + 1
                starty = starty + 1
        if turn == "White" and Inside(startx + 1, starty + 1) and Map[startx + 1][starty + 1].startswith("Black"):
            List.append((startx + 1, starty + 1))
        if turn == "Black" and Inside(startx + 1, starty + 1) and Map[startx + 1][starty + 1].startswith("White"):
            List.append((startx + 1, starty + 1))

        startx = copyStartx
        starty = copyStarty
        if Inside(startx + 1, starty - 1) and Map[startx + 1][starty - 1] == 0:
            while Inside(startx + 1, starty - 1) and Map[startx + 1][starty - 1] == 0:
                List.append((startx + 1, starty - 1))
                startx = startx + 1
                starty = starty - 1
        if turn == "White" and Inside(startx + 1, starty - 1) and Map[startx + 1][starty - 1].startswith("Black"):
            List.append((startx + 1, starty - 1))
        if turn == "Black" and Inside(startx + 1, starty - 1) and Map[startx + 1][starty - 1].startswith("White"):
            List.append((startx + 1, starty - 1))

        startx = copyStartx
        starty = copyStarty
        if Inside(startx - 1, starty + 1) and Map[startx - 1][starty + 1] == 0:
            while Inside(startx - 1, starty + 1) and Map[startx - 1][starty + 1] == 0:
                List.append((startx - 1, starty + 1))
                startx = startx - 1
                starty = starty + 1
        if turn == "White" and Inside(startx - 1, starty + 1) and Map[startx - 1][starty + 1].startswith("Black"):
            List.append((startx - 1, starty + 1))
        if turn == "Black" and Inside(startx - 1, starty + 1) and Map[startx - 1][starty + 1].startswith("White"):
            List.append((startx - 1, starty + 1))

        startx = copyStartx
        starty = copyStarty
        if Inside(startx - 1, starty - 1) and Map[startx - 1][starty - 1] == 0:
            while Inside(startx - 1, starty - 1) and Map[startx - 1][starty - 1] == 0:
                List.append((startx - 1, starty - 1))
                startx = startx - 1
                starty = starty - 1
        if turn == "White" and Inside(startx - 1, starty - 1) and Map[startx - 1][starty - 1].startswith("Black"):
            List.append((startx - 1, starty - 1))
        if turn == "Black" and Inside(startx - 1, starty - 1) and Map[startx - 1][starty - 1].startswith("White"):
            List.append((startx - 1, starty - 1))

        # Queen treated as both a Bishop and a Rook
    if "Queen" in currentPiece:
        copyStartx = startx
        copyStarty = starty

        if Inside(startx + 1, starty) and Map[startx + 1][starty] == 0:
            while Inside(startx + 1, starty) and Map[startx + 1][starty] == 0:
                List.append((startx + 1, starty))
                startx = startx + 1
        if turn == "White" and Inside(startx + 1, starty) and Map[startx + 1][starty].startswith("Black"):
            List.append((startx + 1, starty))
        if turn == "Black" and Inside(startx + 1, starty) and Map[startx + 1][starty].startswith("White"):
            List.append((startx + 1, starty))

        startx = copyStartx
        starty = copyStarty
        if Inside(startx - 1, starty) and Map[startx - 1][starty] == 0:
            while Inside(startx - 1, starty) and Map[startx - 1][starty] == 0:
                List.append((startx - 1, starty))
                startx = startx - 1
        if turn == "White" and Inside(startx - 1, starty) and Map[startx - 1][starty].startswith("Black"):
            List.append((startx - 1, starty))
        if turn == "Black" and Inside(startx - 1, starty) and Map[startx - 1][starty].startswith("White"):
            List.append((startx - 1, starty))

        startx = copyStartx
        starty = copyStarty
        if Inside(startx, starty + 1) and Map[startx][starty + 1] == 0:
            while Inside(startx, starty + 1) and Map[startx][starty + 1] == 0:
                List.append((startx, starty + 1))
                starty = starty + 1
        if turn == "White" and Inside(startx, starty + 1) and Map[startx][starty + 1].startswith("Black"):
            List.append((startx, starty + 1))
        if turn == "Black" and Inside(startx, starty + 1) and Map[startx][starty + 1].startswith("White"):
            List.append((startx, starty + 1))

        startx = copyStartx
        starty = copyStarty
        if Inside(startx, starty - 1) and Map[startx][starty - 1] == 0:
            while Inside(startx, starty - 1) and Map[startx][starty - 1] == 0:
                List.append((startx, starty - 1))
                starty = starty - 1
        if turn == "White" and Inside(startx, starty - 1) and Map[startx][starty - 1].startswith("Black"):
            List.append((startx, starty - 1))
        if turn == "Black" and Inside(startx, starty - 1) and Map[startx][starty - 1].startswith("White"):
            List.append((startx, starty - 1))

        startx = copyStartx
        starty = copyStarty
        if Inside(startx + 1, starty + 1) and Map[startx + 1][starty + 1] == 0:
            while Inside(startx + 1, starty + 1) and Map[startx + 1][starty + 1] == 0:
                List.append((startx + 1, starty + 1))
                startx = startx + 1
                starty = starty + 1
        if turn == "White" and Inside(startx + 1, starty + 1) and Map[startx + 1][starty + 1].startswith("Black"):
            List.append((startx + 1, starty + 1))
        if turn == "Black" and Inside(startx + 1, starty + 1) and Map[startx + 1][starty + 1].startswith("White"):
            List.append((startx + 1, starty + 1))

        startx = copyStartx
        starty = copyStarty
        if Inside(startx + 1, starty - 1) and Map[startx + 1][starty - 1] == 0:
            while Inside(startx + 1, starty - 1) and Map[startx + 1][starty - 1] == 0:
                List.append((startx + 1, starty - 1))
                startx = startx + 1
                starty = starty - 1
        if turn == "White" and Inside(startx + 1, starty - 1) and Map[startx + 1][starty - 1].startswith("Black"):
            List.append((startx + 1, starty - 1))
        if turn == "Black" and Inside(startx + 1, starty - 1) and Map[startx + 1][starty - 1].startswith("White"):
            List.append((startx + 1, starty - 1))

        startx = copyStartx
        starty = copyStarty
        if Inside(startx - 1, starty + 1) and Map[startx - 1][starty + 1] == 0:
            while Inside(startx - 1, starty + 1) and Map[startx - 1][starty + 1] == 0:
                List.append((startx - 1, starty + 1))
                startx = startx - 1
                starty = starty + 1
        if turn == "White" and Inside(startx - 1, starty + 1) and Map[startx - 1][starty + 1].startswith("Black"):
            List.append((startx - 1, starty + 1))
        if turn == "Black" and Inside(startx - 1, starty + 1) and Map[startx - 1][starty + 1].startswith("White"):
            List.append((startx - 1, starty + 1))

        startx = copyStartx
        starty = copyStarty
        if Inside(startx - 1, starty - 1) and Map[startx - 1][starty - 1] == 0:
            while Inside(startx - 1, starty - 1) and Map[startx - 1][starty - 1] == 0:
                List.append((startx - 1, starty - 1))
                startx = startx - 1
                starty = starty - 1
        if turn == "White" and Inside(startx - 1, starty - 1) and Map[startx - 1][starty - 1].startswith("Black"):
            List.append((startx - 1, starty - 1))
        if turn == "Black" and Inside(startx - 1, starty - 1) and Map[startx - 1][starty - 1].startswith("White"):
            List.append((startx - 1, starty - 1))
    if "Knight" in currentPiece:
        copyStartx = startx
        copyStarty = starty
        Knight = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]
        for Move in Knight:
            startx = copyStartx
            starty = copyStarty
            if Inside(startx + Move[0], starty + Move[1]) and Map[startx + Move[0]][starty + Move[1]] == 0:
                List.append((startx + Move[0], starty + Move[1]))
            elif turn == "White" and Inside(startx + Move[0], starty + Move[1]) and \
                    Map[startx + Move[0]][starty + Move[1]].startswith("Black"):
                List.append((startx + Move[0], starty + Move[1]))
            elif turn == "Black" and Inside(startx + Move[0], starty + Move[1]) and \
                    Map[startx + Move[0]][starty + Move[1]].startswith("White"):
                List.append((startx + Move[0], starty + Move[1]))
    copyList = copy.deepcopy(List)
    AttackingPawnMoves = []
    if "Pawn" in currentPiece:
        copyStartx = startx
        copyStarty = starty

        if turn == "White":
            if Inside(startx + 1, starty + 1):
                AttackingPawnMoves.append((startx + 1, starty + 1))
            if Inside(startx + 1, starty - 1):
                AttackingPawnMoves.append((startx + 1, starty - 1))
        if turn == "Black":
            if Inside(startx - 1, starty + 1):
                AttackingPawnMoves.append((startx - 1, starty + 1))
            if Inside(startx - 1, starty - 1):
                AttackingPawnMoves.append((startx - 1, starty - 1))
        copyList.extend(AttackingPawnMoves)

        # First Move
        if turn == "White" and startx == 2:
            if Map[startx + 1][starty] == 0:
                List.append((startx + 1, starty))
                if Map[startx + 2][starty] == 0:
                    List.append((startx + 2, starty))
            if Inside(startx + 1, starty + 1) and Map[startx + 1][starty + 1] != 0 and Map[startx + 1][starty + 1].startswith("Black"):
                List.append((startx + 1, starty + 1))
            if Inside(startx + 1, starty - 1) and Map[startx + 1][starty - 1] != 0 and Map[startx + 1][starty - 1].startswith("Black"):
                List.append((startx + 1, starty - 1))
                
        elif turn == "Black" and startx == 7:
            if Map[startx - 1][starty] == 0:
                List.append((startx - 1, starty))
                if Map[startx - 2][starty] == 0:
                    List.append((startx - 2, starty))
            if Inside(startx - 1, starty + 1) and Map[startx - 1][starty + 1] != 0 and Map[startx - 1][starty + 1].startswith("White"):
                List.append((startx + 1, starty - 1))
            if Inside(startx - 1, starty - 1) and Map[startx - 1][starty - 1] != 0 and Map[startx - 1][starty - 1].startswith("White"):
                List.append((startx - 1, starty - 1))

        # Every other move
        else:
            if turn == "White":
                if Inside(startx + 1, starty) and Map[startx + 1][starty] == 0:
                    List.append((startx + 1, starty))
                if Inside(startx + 1, starty + 1) and Map[startx + 1][starty + 1] != 0 and Map[startx + 1][starty + 1].startswith("Black"):
                    List.append((startx + 1, starty + 1))
                if Inside(startx + 1, starty - 1) and Map[startx + 1][starty - 1] != 0 and Map[startx + 1][starty - 1].startswith("Black"):
                    List.append((startx + 1, starty - 1))

            if turn == "Black":
                if Inside(startx - 1, starty) and Map[startx - 1][starty] == 0:
                    List.append((startx - 1, starty))
                if Inside(startx - 1, starty + 1) and Map[startx - 1][starty + 1] != 0 and Map[startx - 1][starty + 1].startswith("White"):
                    List.append((startx - 1, starty + 1))
                if Inside(startx - 1, starty - 1) and Map[startx - 1][starty - 1] != 0 and Map[startx - 1][starty - 1].startswith("White"):
                    List.append((startx - 1, starty - 1))

    if not ListPin:
        return List, copyList
    return [tuples for tuples in List if tuples in ListPin], [tuples for tuples in copyList if tuples in ListPin]


def getAllLegalMoves(Map, turn):
    allLegalMoves = []

    for row in range(9):
        for col in range(9):
            currentPiece = getPiece(row, col, Map)

            # Check if the current piece belongs to the given turn
            if currentPiece != 0 and currentPiece.startswith(turn):
                legalMovesForPiece = legalMoves(Map, row, col, currentPiece, turn)[0]
                allLegalMoves.extend(legalMovesForPiece)

    return allLegalMoves


def getAllAttackingMoves(Map, turn):
    allAttackingMoves = []

    for row in range(9):
        for col in range(9):
            currentPiece = getPiece(row, col, Map)

            # Check if the current piece belongs to the given turn
            if currentPiece != 0 and currentPiece.startswith(turn):
                legalMovesForPiece = legalMoves(Map, row, col, currentPiece, turn)[1]
                allAttackingMoves.extend(legalMovesForPiece)

    return allAttackingMoves


def getKingMoves(Map, turn):
    kingMoves = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    kingPosition = findPiece(turn + "King", Map)
    opposingKingPosition = findPiece("WhiteKing" if turn == "Black" else "BlackKing", Map)

    opponentMoves = getAllAttackingMoves(Map, "White" if turn == "Black" else "Black")
    possibleOppenentKingMoves = []

    for dx, dy in directions:
        newx = opposingKingPosition[0] + dx
        newy = opposingKingPosition[1] + dy
        if Inside(newx, newy):
            possibleOppenentKingMoves.append((newx, newy))
    opponentMoves.extend(possibleOppenentKingMoves)

    for dx, dy in directions:
        newx = kingPosition[0] + dx
        newy = kingPosition[1] + dy
        if Inside(newx, newy):
            if (newx, newy) not in opponentMoves:
                if Map[newx][newy] == 0 or not Map[newx][newy].startswith(turn):
                    kingMoves.append((newx, newy))

    if turn == "White":
        kingside_rook_position = (1, 1)
        queenside_rook_position = (1, 8)
    else:
        kingside_rook_position = (8, 1)
        queenside_rook_position = (8, 8)

    if kingPosition not in opponentMoves:
        # Check kingside castling
        if (
                Map[kingPosition[0]][kingPosition[1] - 1] == 0
                and Map[kingPosition[0]][kingPosition[1] - 2] == 0
                and Map[kingside_rook_position[0]][kingside_rook_position[1]] == turn + "Rook"
        ):
            kingMoves.append((kingPosition[0], kingPosition[1] - 2))

        # Check queenside castling
        if (
                Map[kingPosition[0]][kingPosition[1] + 1] == 0
                and Map[kingPosition[0]][kingPosition[1] + 2] == 0
                and Map[kingPosition[0]][kingPosition[1] + 3] == 0
                and Map[queenside_rook_position[0]][queenside_rook_position[1]] == turn + "Rook"
        ):
            kingMoves.append((kingPosition[0], kingPosition[1] + 2))

    return kingMoves





