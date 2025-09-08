import chess.pgn
import sys

if len(sys.argv) != 3:
    print("Usage: python b.py <input_pgn> <output_pgn>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file) as pgn, open(output_file, "w") as out:
    while True:
        game = chess.pgn.read_game(pgn)
        if game is None:
            break
        result = game.headers.get("Result")
        if result in ["0-1", "1/2-1/2"]:
            out.write(str(game) + "\n\n")

print(f"Filtered games saved to {output_file}")
