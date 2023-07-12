import check

BlackKingMatrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [0, -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [0, -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [0, -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [0, -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    [0, -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    [0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0],
    [0, 2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

BlackQueenMatrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
    [0, -1.0, 0, 0, 0, 0, 0, 0, -1.0],
    [0, -1.0, 0, 0.5, 0.5, 0.5, 0.5, 0, -1.0],
    [0, -0.5, 0, 0.5, 0.5, 0.5, 0.5, 0, -0.5],
    [0, 0, 0, 0.5, 0.5, 0.5, 0.5, 0, 0],
    [0, -1.0, 0, 0.5, 0.5, 0.5, 0.5, 0, -1.0],
    [0, -1.0, 0, 0.5, 0.5, 0.5, 0.5, 0, -1.0],
    [0, -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

BlackRookMatrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0.5, 1, 1, 1, 1, 1, 1, 0.5],
    [0, -0.5, 0, 0, 0, 0, 0, 0, -0.5],
    [0, -0.5, 0, 0, 0, 0, 0, 0, -0.5],
    [0, -0.5, 0, 0, 0, 0, 0, 0, -0.5],
    [0, -0.5, 0, 0, 0, 0, 0, 0, -0.5],
    [0, -0.5, 0, 0, 0, 0, 0, 0, -0.5],
    [0, 0, 0, 0, 0.5, 0.5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

BlackBishopMatrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
    [0, -1.0, 0, 0, 0, 0, 0, 0, -1.0],
    [0, -1.0, 0, 0.5, 1.0, 1.0, 0.5, 0, -1.0],
    [0, -1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0],
    [0, -1.0, 0, 1.0, 1.0, 1.0, 1.0, 0, -1.0],
    [0, -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0],
    [0, -1.0, 0.5, 0, 0, 0, 0, 0.5, -1.0],
    [0, -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

BlackKnightMatrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
    [0, -4.0, -2.0, 0, 0, 0, 0, -2.0, -4.0],
    [0, -3.0, 0, 1.0, 1.5, 1.5, 1.0, 0, -3.0],
    [0, -3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0],
    [0, -3.0, 0, 1.5, 2.0, 2.0, 1.5, 0, -3.0],
    [0, -3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0],
    [0, -4.0, -2.0, 0, 0.5, 0.5, 0, -2.0, -4.0],
    [0, -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

BlackPawnMatrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0],
    [0, 1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0],
    [0, 0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5],
    [0, 0, 0, 0, 2.0, 2.0, 0, 0, 0],
    [0, 0.5, -0.5, -1.0, 0, 0, -1.0, -0.5, 0.5],
    [0, 0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def evaluatePosition(Map):
    if check.isCheckmate(Map, "White"):
        return -9999
    elif check.isCheckmate(Map, "Black"):
        return 9999
    materialScore = evaluateMaterial(Map)
    positionalScore = evaluatePositional(Map)
    evaluationScore = materialScore + positionalScore/10
    return evaluationScore


def evaluateMaterial(Map):
    whiteMaterialScore = 0
    blackMaterialScore = 0

    # Point values for each piece type
    piece_values = {
        "Pawn": 1,
        "Knight": 3,
        "Bishop": 3,
        "Rook": 5,
        "Queen": 9
    }

    # Iterate over the Map and calculate the material score for each side
    for row in Map:
        for piece in row:
            if piece != 0 and piece[5:] in piece_values.keys():
                if "White" in piece:
                    whiteMaterialScore += piece_values[piece[5:]]
                else:
                    blackMaterialScore += piece_values[piece[5:]]

    materialScore = whiteMaterialScore - blackMaterialScore
    return materialScore


def evaluatePositional(Map):
    positionalScore = 0

    # White piece evaluation matrices
    black_matrices = {
        "King": BlackKingMatrix,
        "Queen": BlackQueenMatrix,
        "Rook": BlackRookMatrix,
        "Bishop": BlackBishopMatrix,
        "Knight": BlackKnightMatrix,
        "Pawn": BlackPawnMatrix
    }

    # Iterate over the Map and calculate the positional score
    for i in range(1, 9):
        for j in range(1, 9):
            piece = Map[i][j]
            if piece != 0:
                if "Black" in piece:
                    piece_type = piece[5:]  # Extract the piece type without "White"
                    positionalScore -= black_matrices[piece_type][i][j]
                else:  # Black pieces
                    # Get the corresponding black evaluation matrix and reverse it
                    piece_type = piece[5:]  # Extract the piece type without "Black"
                    white_matrices = list(reversed(black_matrices[piece_type]))
                    positionalScore += white_matrices[i][j]

    return positionalScore



