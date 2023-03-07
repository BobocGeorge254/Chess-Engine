def Inside(dx,dy) :
    return dx >= 1 and dx <= 8 and dy >= 1 and dy <= 8

def xWhiteKing(Map) :
    for i in range(1,9) :
        for j in range(1,9) :
            if Map[i][j] == "WhiteKing" :
                return i

def yWhiteKing(Map) :
    for i in range(1,9) :
        for j in range(1,9) :
            if Map[i][j] == "WhiteKing" :
                return j

def xBlackKing(Map) :
    for i in range(1,9) :
        for j in range(1,9) :
            if Map[i][j] == "BlackKing" :
                return i

def yBlackKing(Map) :
    for i in range(1,9) :
        for j in range(1,9) :
            if Map[i][j] == "BlackKing" :
                return j

def Pinned(Map, startx, stopx) :
    pinnedPieces = []
    ct = 0
    i = xWhiteKing(Map) + 1
    j = yWhiteKing(Map) + 1
    while Inside(i,j) :
        if Map[i][j] != 0 :
            if "White" in Map[i][j] :
                ct = ct + 1
                pinX = i
                pinY = j
            elif "Black" in Map[i][j] and ct == 1 :
                if Map[i][j] == "BlackBishop" or Map[i][j] == "BlackQueen" :
                    pinnedPieces.append((pinX,pinY))
        i = i + 1
        j = j + 1

    ct = 0
    i = xWhiteKing(Map) + 1
    j = yWhiteKing(Map) - 1
    while Inside(i,j) :
        if Map[i][j] != 0 :
            if "White" in Map[i][j] :
                ct = ct + 1
                pinX = i
                pinY = j
            elif "Black" in Map[i][j] and ct == 1 :
                if Map[i][j] == "BlackBishop" or Map[i][j] == "BlackQueen" :
                    pinnedPieces.append((pinX,pinY))
        i = i + 1
        j = j - 1

    ct = 0
    i = xWhiteKing(Map) - 1
    j = yWhiteKing(Map) + 1
    while Inside(i,j) :
        if Map[i][j] != 0 :
            if "White" in Map[i][j] :
                ct = ct + 1
                pinX = i
                pinY = j
            elif "Black" in Map[i][j] and ct == 1 :
                if Map[i][j] == "BlackBishop" or Map[i][j] == "BlackQueen" :
                    pinnedPieces.append((pinX,pinY))
        i = i - 1
        j = j + 1

    ct = 0
    i = xWhiteKing(Map) - 1
    j = yWhiteKing(Map) - 1
    while Inside(i,j) :
        if Map[i][j] != 0 :
            if "White" in Map[i][j] :
                ct = ct + 1
                pinX = i
                pinY = j
            elif "Black" in Map[i][j] and ct == 1 :
                if Map[i][j] == "BlackBishop" or Map[i][j] == "BlackQueen" :
                    pinnedPieces.append((pinX,pinY))
        i = i - 1
        j = j - 1

    ct = 0
    i = xWhiteKing(Map)
    j = yWhiteKing(Map) - 1
    while Inside(i, j):
        if Map[i][j] != 0:
            if "White" in Map[i][j]:
                ct = ct + 1
                pinX = i
                pinY = j
            elif "Black" in Map[i][j] and ct == 1:
                if Map[i][j] == "BlackRook" or Map[i][j] == "BlackQueen":
                    pinnedPieces.append((pinX, pinY))
        j = j - 1

    ct = 0
    i = xWhiteKing(Map)
    j = yWhiteKing(Map) + 1
    while Inside(i, j):
        if Map[i][j] != 0:
            if "White" in Map[i][j]:
                ct = ct + 1
                pinX = i
                pinY = j
            elif "Black" in Map[i][j] and ct == 1:
                if Map[i][j] == "BlackRook" or Map[i][j] == "BlackQueen":
                    pinnedPieces.append((pinX, pinY))
        j = j + 1

    ct = 0
    i = xWhiteKing(Map) - 1
    j = yWhiteKing(Map)
    while Inside(i, j):
        if Map[i][j] != 0:
            if "White" in Map[i][j]:
                ct = ct + 1
                pinX = i
                pinY = j
            elif "Black" in Map[i][j] and ct == 1:
                if Map[i][j] == "BlackRook" or Map[i][j] == "BlackQueen":
                    pinnedPieces.append((pinX, pinY))
        i = i - 1

    ct = 0
    i = xWhiteKing(Map) + 1
    j = yWhiteKing(Map)
    while Inside(i, j):
        if Map[i][j] != 0:
            if "White" in Map[i][j]:
                ct = ct + 1
                pinX = i
                pinY = j
            elif "Black" in Map[i][j] and ct == 1:
                if Map[i][j] == "BlackRook" or Map[i][j] == "BlackQueen":
                    pinnedPieces.append((pinX, pinY))
        i = i + 1




    ct = 0
    i = xBlackKing(Map) + 1
    j = yBlackKing(Map) + 1
    while Inside(i, j):
        if Map[i][j] != 0:
            if "Black" in Map[i][j]:
                ct = ct + 1
                pinX = i
                pinY = j
            elif "White" in Map[i][j] and ct == 1:
                if Map[i][j] == "WhiteBishop" or Map[i][j] == "WhiteQueen":
                    pinnedPieces.append((pinX, pinY))
        i = i + 1
        j = j + 1

    ct = 0
    i = xBlackKing(Map) + 1
    j = yBlackKing(Map) - 1
    while Inside(i, j):
        if Map[i][j] != 0:
            if "Black" in Map[i][j]:
                ct = ct + 1
                pinX = i
                pinY = j
            elif "White" in Map[i][j] and ct == 1:
                if Map[i][j] == "WhiteBishop" or Map[i][j] == "WhiteQueen":
                    pinnedPieces.append((pinX, pinY))
        i = i + 1
        j = j - 1

    ct = 0
    i = xBlackKing(Map) - 1
    j = yBlackKing(Map) + 1
    while Inside(i, j):
        if Map[i][j] != 0:
            if "Black" in Map[i][j]:
                ct = ct + 1
                pinX = i
                pinY = j
            elif "White" in Map[i][j] and ct == 1:
                if Map[i][j] == "WhiteBishop" or Map[i][j] == "WhiteQueen":
                    pinnedPieces.append((pinX, pinY))
        i = i - 1
        j = j + 1

    ct = 0
    i = xBlackKing(Map) - 1
    j = yBlackKing(Map) - 1
    while Inside(i, j):
        if Map[i][j] != 0:
            if "Black" in Map[i][j]:
                ct = ct + 1
                pinX = i
                pinY = j
            elif "White" in Map[i][j] and ct == 1:
                if Map[i][j] == "WhiteBishop" or Map[i][j] == "WhiteQueen":
                    pinnedPieces.append((pinX, pinY))
        i = i - 1
        j = j - 1

    ct = 0
    i = xBlackKing(Map) - 1
    j = yBlackKing(Map)
    while Inside(i, j):
        if Map[i][j] != 0:
            if "Black" in Map[i][j]:
                ct = ct + 1
                pinX = i
                pinY = j
            elif "White" in Map[i][j] and ct == 1:
                if Map[i][j] == "WhiteRook" or Map[i][j] == "WhiteQueen":
                    pinnedPieces.append((pinX, pinY))
        i = i - 1

    ct = 0
    i = xBlackKing(Map) + 1
    j = yBlackKing(Map)
    while Inside(i, j):
        if Map[i][j] != 0:
            if "Black" in Map[i][j]:
                ct = ct + 1
                pinX = i
                pinY = j
            elif "White" in Map[i][j] and ct == 1:
                if Map[i][j] == "WhiteRook" or Map[i][j] == "WhiteQueen":
                    pinnedPieces.append((pinX, pinY))
        i = i + 1

    ct = 0
    i = xBlackKing(Map)
    j = yBlackKing(Map) - 1
    while Inside(i, j):
        if Map[i][j] != 0:
            if "Black" in Map[i][j]:
                ct = ct + 1
                pinX = i
                pinY = j
            elif "White" in Map[i][j] and ct == 1:
                if Map[i][j] == "WhiteRook" or Map[i][j] == "WhiteQueen":
                    pinnedPieces.append((pinX, pinY))
        j = j - 1

    ct = 0
    i = xBlackKing(Map)
    j = yBlackKing(Map) + 1
    while Inside(i, j):
        if Map[i][j] != 0:
            if "Black" in Map[i][j]:
                ct = ct + 1
                pinX = i
                pinY = j
            elif "White" in Map[i][j] and ct == 1:
                if Map[i][j] == "WhiteRook" or Map[i][j] == "WhiteQueen":
                    pinnedPieces.append((pinX, pinY))
        j = j + 1

    pin = (startx, stopx) in pinnedPieces
    return pin