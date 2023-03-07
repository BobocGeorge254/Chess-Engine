def Inside(dx,dy) :
    return dx >= 1 and dx <= 8 and dy >= 1 and dy <= 8

def LegalMoves(Map,startx, starty,currentPiece,turn):
    List = []

    #Rook
    if "Rook" in currentPiece :
        copyStartx = startx
        copyStarty = starty

        if Inside(startx + 1, starty) and Map[startx + 1][starty] == 0 :
            while Inside(startx + 1, starty) and Map[startx + 1][starty] == 0 :
                List.append((startx + 1,starty))
                startx = startx + 1
        if turn == 'White' and Inside(startx + 1, starty) and Map[startx + 1][starty][0] == 'B' :
            List.append((startx + 1, starty))
        if turn == 'Black' and Inside(startx + 1, starty) and Map[startx + 1][starty][0] == 'W' :
            List.append((startx + 1, starty))

        startx = copyStartx
        starty = copyStarty
        if Inside(startx - 1, starty) and Map[startx - 1][starty] == 0 :
            while (Inside(startx - 1, starty) and Map[startx - 1][starty] == 0) :
                List.append((startx - 1,starty))
                startx = startx - 1
        if turn == 'White' and Inside(startx - 1, starty) and Map[startx - 1][starty][0] == 'B' :
            List.append((startx - 1, starty))
        if turn == 'Black' and Inside(startx - 1, starty) and Map[startx - 1][starty][0] == 'W' :
            List.append((startx - 1, starty))


        startx = copyStartx
        starty = copyStarty
        if Inside(startx, starty + 1) and Map[startx][starty + 1] == 0 :
            while (Inside(startx, starty + 1) and Map[startx][starty + 1] == 0) :
                List.append((startx,starty + 1))
                starty = starty + 1
        if turn == 'White' and Inside(startx, starty + 1) and Map[startx][starty + 1][0] == 'B':
            List.append((startx, starty + 1))
        if turn == 'Black' and Inside(startx, starty + 1) and Map[startx][starty + 1][0] == 'W':
            List.append((startx, starty + 1))

        startx = copyStartx
        starty = copyStarty
        if Inside(startx, starty - 1) and Map[startx][starty - 1] == 0 :
            while (Inside(startx, starty - 1) and Map[startx][starty - 1] == 0) :
                List.append((startx,starty - 1))
                starty = starty - 1
        if turn == 'White' and Inside(startx, starty - 1) and Map[startx][starty - 1][0] == 'B':
            List.append((startx, starty - 1))
        if turn == 'Black' and Inside(startx, starty - 1) and Map[startx][starty - 1][0] == 'W':
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
        if turn == 'White' and Inside(startx + 1, starty + 1) and Map[startx + 1][starty + 1][0] == 'B':
            List.append((startx + 1, starty + 1))
        if turn == 'Black' and Inside(startx + 1, starty + 1) and Map[startx + 1][starty + 1][0] == 'W':
            List.append((startx + 1, starty + 1))

        startx = copyStartx
        starty = copyStarty
        if Inside(startx + 1, starty - 1) and Map[startx + 1][starty - 1] == 0:
            while Inside(startx + 1, starty - 1) and Map[startx + 1][starty - 1] == 0:
                List.append((startx + 1, starty - 1))
                startx = startx + 1
                starty = starty - 1
        if turn == 'White' and Inside(startx + 1, starty - 1) and Map[startx + 1][starty - 1][0] == 'B':
            List.append((startx + 1, starty - 1))
        if turn == 'Black' and Inside(startx + 1, starty - 1) and Map[startx + 1][starty - 1][0] == 'W':
            List.append((startx + 1, starty - 1))

        startx = copyStartx
        starty = copyStarty
        if Inside(startx - 1, starty + 1) and Map[startx - 1][starty + 1] == 0:
            while Inside(startx - 1, starty + 1) and Map[startx - 1][starty + 1] == 0:
                List.append((startx - 1, starty + 1))
                startx = startx - 1
                starty = starty + 1
        if turn == 'White' and Inside(startx - 1, starty + 1) and Map[startx - 1][starty + 1][0] == 'B':
            List.append((startx - 1, starty + 1))
        if turn == 'Black' and Inside(startx - 1, starty + 1) and Map[startx - 1][starty + 1][0] == 'W':
            List.append((startx - 1, starty + 1))

        startx = copyStartx
        starty = copyStarty
        if Inside(startx - 1, starty - 1) and Map[startx - 1][starty - 1] == 0:
            while Inside(startx - 1, starty - 1) and Map[startx - 1][starty - 1] == 0:
                List.append((startx - 1, starty - 1))
                startx = startx - 1
                starty = starty - 1
        if turn == 'White' and Inside(startx - 1, starty - 1) and Map[startx - 1][starty - 1][0] == 'B':
            List.append((startx - 1, starty - 1))
        if turn == 'Black' and Inside(startx - 1, starty - 1) and Map[startx - 1][starty - 1][0] == 'W':
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
            elif turn == 'White' and Inside(startx + Move[0], starty + Move[1]) and Map[startx + Move[0]][starty + Move[1]][0] == 'B':
                List.append((startx + Move[0], starty + Move[1]))
            elif turn == 'Black' and Inside(startx + Move[0], starty + Move[1]) and Map[startx + Move[0]][starty + Move[1]][0] == 'W':
                List.append((startx + Move[0], starty + Move[1]))

        return List

    #Queen treated as both a Bishop and a Rook
    if "Queen" in currentPiece :
        return LegalMoves(Map,startx,starty,currentPiece[0:5] + "Bishop",turn) + LegalMoves(Map,startx,starty,currentPiece[0:5] + "Rook",turn)

    if "Pawn" in currentPiece :
        copyStartx = startx
        copyStarty = starty

        #First Move
        if turn == 'White' and starty == 2 :
            if Map[startx][starty + 1] == 0:
                List.append( (startx, starty + 1) )
            if Map[startx][starty + 2] == 0:
                List.append( (startx, starty + 2) )
            if Inside(startx + 1, starty + 1) and Map[startx + 1][starty + 1] != 0 and Map[startx + 1][starty + 1][0] == 'B':
                List.append((startx + 1, starty + 1))
            if Inside(startx - 1, starty + 1) and Map[startx - 1][starty + 1] != 0 and Map[startx - 1][starty + 1][0] == 'B':
                List.append((startx - 1, starty + 1))
        elif turn == 'Black' and starty == 7 :
            if Map[startx][starty - 1] == 0:
                List.append( (startx, starty - 1) )
            if Map[startx][starty - 2] == 0:
                List.append( (startx, starty - 2) )
            if Inside(startx + 1, starty - 1) and Map[startx + 1][starty - 1] != 0 and Map[startx + 1][starty - 1][0] == 'W':
                List.append((startx + 1, starty - 1))
            if Inside(startx - 1, starty - 1) and Map[startx - 1][starty - 1] != 0 and Map[startx - 1][starty - 1][0] == 'W':
                List.append((startx - 1, starty - 1))

        #Every other move
        else :
            if turn == 'White' :
                if Inside(startx, starty + 1) and Map[startx][starty + 1] == 0 :
                    List.append( (startx, starty + 1) )
                if Inside(startx + 1, starty + 1) and Map[startx + 1][starty + 1] != 0 and Map[startx + 1][starty + 1][0] == 'B' :
                    List.append( (startx + 1, starty + 1))
                if Inside(startx - 1, starty + 1) and Map[startx - 1][starty + 1] != 0 and Map[startx - 1][starty + 1][0] == 'B' :
                    List.append( (startx - 1, starty + 1))

            if turn == 'Black' :
                if Inside(startx, starty - 1) and Map[startx][starty - 1] == 0 :
                    List.append( (startx, starty - 1) )
                if Inside(startx + 1, starty - 1) and Map[startx + 1][starty - 1] != 0 and Map[startx + 1][starty - 1][0] == 'W' :
                    List.append( (startx + 1, starty - 1))
                if Inside(startx - 1, starty - 1) and Map[startx - 1][starty - 1] != 0 and Map[startx - 1][starty - 1][0] == 'W' :
                    List.append( (startx - 1, starty - 1))

        #Pawn promotion took care in Move function

    return List


def GetAllLegalMoves(Map,side) :
    List = []
    for i in range(1,9) :
        for j in range(1,9) :
            if Map[i][j] != 0 and Map[i][j][0] == side[0] == 'W' :
                if Map[i][j] == "WhitePawn" :
                    List = List + LegalMoves(Map,i,j,"WhitePawn","White")
                if Map[i][j] == "WhiteKnight" :
                    List = List + LegalMoves(Map,i,j,"WhiteKnight","White")
                if Map[i][j] == "WhiteBishop" :
                    List = List + LegalMoves(Map,i,j,"WhiteBishop","White")
                if Map[i][j] == "WhiteRook" :
                    List = List + LegalMoves(Map,i,j,"WhiteRook","White")
                if Map[i][j] == "WhiteQueen" :
                    List = List + LegalMoves(Map,i,j,"WhiteQueen","White")
            if Map[i][j] != 0 and Map[i][j][0] == side[0] == 'B':
                if Map[i][j] == "BlackPawn" :
                    List = List + LegalMoves(Map,i,j,"BlackPawn","Black")
                if Map[i][j] == "BlackKnight" :
                    List = List + LegalMoves(Map,i,j,"BlackKnight","Black")
                if Map[i][j] == "BlackBishop" :
                    List = List + LegalMoves(Map,i,j,"BlackBishop","Black")
                if Map[i][j] == "BlackRook" :
                    List = List + LegalMoves(Map,i,j,"BlackRook","Black")
                if Map[i][j] == "BlackQueen" :
                    List = List + LegalMoves(Map,i,j,"BlackQueen","Black")

    return List