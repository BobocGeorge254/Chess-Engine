def getPiece(dx, dy, Map):
    return Map[dx][dy]


def Inside(dx, dy):
    return 1 <= dx <= 8 and 1 <= dy <= 8


def isPiecePinned(dx, dy, Map):
    piece = getPiece(dx, dy, Map)

    if piece == 0:
        return False

    # Find the king's position
    king = "WhiteKing" if piece.startswith("White") else "BlackKing"
    kingPosition = None
    for i in range(1, 9):
        for j in range(1, 9):
            if getPiece(i, j, Map) == king:
                kingPosition = (i, j)
                break

    # Check if the piece is on the same row, column, or diagonal as the king
    if dx == kingPosition[0] or dy == kingPosition[1] or abs(dx - kingPosition[0]) == abs(dy - kingPosition[1]):
        legal_moves = []  # List to store legal moves for pinned piece

        # Check if there is an opposing rook or queen along the same row or column
        if dx == kingPosition[0]:
            direction = 1 if dy > kingPosition[1] else -1

            j = dy - direction
            while Inside(dx, j):
                if getPiece(dx, j, Map) != 0:
                    if (piece.startswith("White") and getPiece(dx, j, Map) != "WhiteKing") or (
                            piece.startswith("Black") and getPiece(dx, j, Map) != "BlackKing"):
                        return False
                    else:
                        break
                legal_moves.append((dx, j))  # Add legal move
                j -= direction

            j = dy + direction
            while Inside(dx, j):
                if getPiece(dx, j, Map) != 0:
                    if (piece.startswith("White") and getPiece(dx, j, Map) in ["BlackRook", "BlackQueen"]) or (
                            piece.startswith("Black") and getPiece(dx, j, Map) in ["WhiteRook", "WhiteQueen"]):
                        legal_moves.append((dx, j))
                        return legal_moves  # Return legal moves
                    else:
                        break
                legal_moves.append((dx, j))  # Add legal move
                j += direction

        elif dy == kingPosition[1]:
            direction = 1 if dx > kingPosition[0] else -1

            i = dx - direction
            while Inside(i, dy):
                if getPiece(i, dy, Map) != 0:
                    if (piece.startswith("White") and getPiece(i, dy, Map) != "WhiteKing") or (
                            piece.startswith("Black") and getPiece(i, dy, Map) != "BlackKing"):
                        return False
                    else:
                        break
                legal_moves.append((i, dy))  # Add legal move
                i -= direction

            i = dx + direction
            while Inside(i, dy):
                if getPiece(i, dy, Map) != 0:
                    if (piece.startswith("White") and getPiece(i, dy, Map) in ["BlackRook", "BlackQueen"]) or (
                            piece.startswith("Black") and getPiece(i, dy, Map) in ["WhiteRook", "WhiteQueen"]):
                        legal_moves.append((i, dy))
                        return legal_moves  # Return legal moves
                    else:
                        break
                legal_moves.append((i, dy))  # Add legal move
                i += direction
        else:
            dxDirection = 1 if dx > kingPosition[0] else -1
            dyDirection = 1 if dy > kingPosition[1] else -1

            i = dx - dxDirection
            j = dy - dyDirection
            while Inside(i, j):
                if getPiece(i, j, Map) != 0:
                    if (piece.startswith("White") and getPiece(i, j, Map) != "WhiteKing") or (
                            piece.startswith("Black") and getPiece(i, j, Map) != "BlackKing"):
                        return False
                    else:
                        break
                legal_moves.append((i, j))  # Add legal move
                i -= dxDirection
                j -= dyDirection

            i = dx + dxDirection
            j = dy + dyDirection
            while Inside(i, j):
                if getPiece(i, j, Map) != 0:
                    if (piece.startswith("White") and getPiece(i, j, Map) in ["BlackBishop", "BlackQueen"]) or (
                            piece.startswith("Black") and getPiece(i, j, Map) in ["WhiteBishop", "WhiteQueen"]):
                        legal_moves.append((i, j))
                        return legal_moves  # Return legal moves
                    else:
                        break
                legal_moves.append((i, j))  # Add legal move
                i += dxDirection
                j += dyDirection

        return False

    return False
