import evaluation
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
    if isinstance(piece, str) and "Pawn" in piece:
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

    return Map


def minimaxWhite(Map, depth, alpha, beta, maximizingPlayer):
    if depth == 0:
        return evaluation.evaluatePosition(Map)
    if maximizingPlayer:
        legalMoves = moves.getAllLegalMovesWhite(Map)
        maxEval = float('-inf')
        for move in legalMoves:
            tempMap = makeMove(*move, Map, 1)  # Make the move on a temporary map
            depthEvaluation = minimaxWhite(tempMap, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, depthEvaluation)
            alpha = max(alpha, depthEvaluation)
            if beta <= alpha:
                break
        return maxEval
    else:
        legalMoves = moves.getAllLegalMovesBlack(Map)
        minEval = float('inf')
        for move in legalMoves:
            tempMap = makeMove(*move, Map, 1)  # Make the move on a temporary map
            depthEvaluation = minimaxWhite(tempMap, depth - 1, alpha, beta, True)
            minEval = min(minEval, depthEvaluation)
            beta = min(beta, depthEvaluation)
            if beta <= alpha:
                break
        return minEval


def bestMove(Map, depth):
    legalMoves = moves.getAllLegalMovesWhite(Map)
    bestScore = float('-inf')
    bestMove = None
    alpha = float('-inf')
    beta = float('inf')

    for move in legalMoves:
        tempMap = [[piece for piece in row] for row in Map]  # Create a copy of the map
        makeMove(*move, tempMap, 1)  # Make the move on the temporary map
        score = minimaxWhite(tempMap, depth - 1, alpha, beta, False)

        if score > bestScore:
            bestScore = score
            bestMove = move

    return bestMove, bestScore
