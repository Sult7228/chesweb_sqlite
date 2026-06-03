import chess
import chess.pgn


def validate_and_apply_move(game, notation):
    board = chess.Board()
    for move in game.moves.all():
        board.push_san(move.notation)

    try:
        move = board.parse_san(notation)
        board.push(move)
        return True, board.fen()
    except Exception:
        return False, None