import random

def killAndReturn():
    # 8 x 8 chessboard filled with zero
    chessboard = [[0] * 8 for _ in range(8)]

    # Place the soldiers randomly on the board
    total_soldiers = random.randint(1, 7)  # Number of soldiers
    placed_soldiers = set()  # To keep track of placed soldiers

    while len(placed_soldiers) < total_soldiers:
        row = random.randint(0, 7)
        col = random.randint(0, 7)
        if (row, col) not in placed_soldiers:
            placed_soldiers.add((row, col))
            chessboard[row][col] = 1  # Mark the cell as occupied by a soldier

    # Place the specialized castle randomly on the board
    while True:
        castle_row = random.randint(0, 7)
        castle_col = random.randint(0, 7)
        if (castle_row, castle_col) not in placed_soldiers:
            chessboard[castle_row][castle_col] = 2  # Mark the cell as occupied by the castle
            break

    for row in chessboard:
        print(row)

    # Implement the movement logic for the castle
    def move_castle():
        current_row, current_col = castle_row, castle_col
        while current_row > 0:
            next_row = current_row - 1
            next_col = current_col
            if chessboard[next_row][next_col] == 1:
                # Castle kills the soldier and moves to the left
                chessboard[next_row][next_col] = 0
                current_row, current_col = next_row, max(0, current_col - 1)
            else:
                # Move the castle forward if possible
                current_row = next_row

    # Call the move_castle function
    move_castle()

    # Print the final state of the chessboard
    print("\nFinal State:")
    for row in chessboard:
        print(row)

# Run the function
killAndReturn()
