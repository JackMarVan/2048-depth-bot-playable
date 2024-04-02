import random

board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board_free = []

valid_moves = ['n', 's', 'e', 'w', 'q']
auto_valid_moves = ['n', 's', 'e', 'w']

global points
points = 0

user_input = ''

# Prints a formatted version of the board's state
def clean_print():
    for x in range(4):
        for y in range(4):
            print(f"{board[x * 4 + y * 1] : <5}", end = " ")
            #print(board[x * 4 + y * 1], end = " ")
        print()
        print()
    print()

# Performs a user specified move by sliding the board,
# merging it, then sliding again
def next_move():
    valid_turn_check = 0
    if shift() == 1:
        valid_turn_check = 1
    if merge() == 1:
        valid_turn_check = 1
    if shift() == 1:
        valid_turn_check = 1
    return valid_turn_check

# Places a 2 tile in a random empty space, sometimes a 4 (10%)
def place_tile():
    if evaluate_board_validity() == 1:
        return 1
    new_tile = 0
    if random.randint(1, 10) == 1:
        new_tile = 4
    else:
        new_tile = 2
    free_indexes = len(board_free) - 1
    tile_spot = board_free[random.randint(0, free_indexes)]
    board[tile_spot] = new_tile

# Iterates through the board to confirm possible spots for a new tile
def evaluate_board_validity():
    free_spots = 0
    global board_free
    board_free = []
    
    for x in range(len(board)):
        if board[x] == 0:
            board_free.append(x)
            free_spots += 1
    
    if free_spots == 0:
        return 1
    return 0

# Merges adjacent tiles in the board according to a user specified direction
def merge():
    global points
    valid_turn_check = 0
    if user_input == 'n':
        for x in range(3):
            for y in range(4):
                if board[x * 4 + y * 1] != 0:
                    if board[x * 4 + y * 1] == board[x * 4 + y * 1 + 4]:
                        board[x * 4 + y * 1] = board[x * 4 + y * 1] * 2
                        board[x * 4 + y * 1 + 4] = 0
                        points += board[x * 4 + y * 1]
                        valid_turn_check = 1
    if user_input == 's':
        for x in range(3):
            for y in range(4):
                if board[15 - (x * 4 + y * 1)] != 0:
                    if board[15 - (x * 4 + y * 1)] == board[15 - (x * 4 + y * 1 + 4)]:
                        board[15 - (x * 4 + y * 1)] = board[15 - (x * 4 + y * 1)] * 2
                        board[15 - (x * 4 + y * 1 + 4)] = 0
                        points += board[15 - (x * 4 + y * 1)]
                        valid_turn_check = 1
    if user_input == 'e':
        for x in range(4):
            for y in range(3):
                if board[x * 4 + (3 - y * 1)] != 0:
                    if board[x * 4 + (3 - y * 1)] == board[x * 4 + (2 - y * 1)]:
                        board[x * 4 + (3 - y * 1)] = board[x * 4 + (3 - y * 1)] * 2
                        board[x * 4 + (2 - y * 1)] = 0
                        points += board[x * 4 + (3 - y * 1)]
                        valid_turn_check = 1
    if user_input == 'w':
        for x in range(4):
            for y in range(3):
                if board[x * 4 + y * 1] != 0:
                    if board[x * 4 + y * 1] == board[x * 4 + y * 1 + 1]:
                        board[x * 4 + y * 1] = board[x * 4 + y * 1] * 2
                        board[x * 4 + y * 1 + 1] = 0
                        points += board[x * 4 + y * 1]
                        valid_turn_check = 1
    return valid_turn_check

# Shifts the board according to a user specified direction
def shift():
    valid_turn_check = 0
    if user_input == 'n':
        for x in range(3):
            for y in range(4):
                compare_index = x * 4 + y * 1 + 4
                if board[x * 4 + y * 1] == 0:
                    while(compare_index <= 15):
                        if board[compare_index] != 0:
                            board[x * 4 + y * 1] = board[compare_index]
                            board[compare_index] = 0
                            valid_turn_check = 1
                            break
                        compare_index += 4
    if user_input == 's':
        for x in range(3):
            for y in range(4):
                compare_index = 15 - (x * 4 + y * 1 + 4)
                if board[15 - (x * 4 + y * 1)] == 0:
                    while(compare_index >= 0):
                        if board[compare_index] != 0:
                            board[15 - (x * 4 + y * 1)] = board[compare_index]
                            board[compare_index] = 0
                            valid_turn_check = 1
                            break
                        compare_index -= 4
    if user_input == 'e':
        for x in range(4):
            for y in range(3):
                compare_index = x * 4 + (2 - y * 1)
                if board[x * 4 + (3 - y * 1)] == 0:
                    while(compare_index >= x * 4):
                        if board[compare_index] != 0:
                            board[x * 4 + (3 - y * 1)] = board[compare_index]
                            board[compare_index] = 0
                            valid_turn_check = 1
                            break
                        compare_index -= 1
    if user_input == 'w':
        for x in range(4):
            for y in range(3):
                compare_index = x * 4 + y * 1 + 1
                if board[x * 4 + y * 1] == 0:
                    while(compare_index <= x * 4 + 3):
                        if board[compare_index] != 0:
                            board[x * 4 + y * 1] = board[compare_index]
                            board[compare_index] = 0
                            valid_turn_check = 1
                            break
                        compare_index += 1
    return valid_turn_check

# Iterates through the board to confirm no merges are possible,
# indicating a game over
def check_game_over():
    for x in range(4):
        for y in range(4):
            if (x * 4 + y * 1) % 4 == 0:
                if board[x * 4 + y * 1] == board[x * 4 + y * 1 + 1]:
                    return 1
            elif (x * 4 + y * 1) % 4 == 3:
                if board[x * 4 + y * 1] == board[x * 4 + y * 1 - 1]:
                    return 1
            else:
                if board[x * 4 + y * 1] == board[x * 4 + y * 1 + 1]:
                    return 1
                if board[x * 4 + y * 1] == board[x * 4 + y * 1 - 1]:
                    return 1

            if (x * 4 + y * 1) < 4:
                if board[x * 4 + y * 1] == board[x * 4 + y * 1 + 4]:
                    return 1
            elif (x * 4 + y * 1) > 11:
                if board[x * 4 + y * 1] == board[x * 4 + y * 1 - 4]:
                    return 1
            else:
                if board[x * 4 + y * 1] == board[x * 4 + y * 1 + 4]:
                    return 1
                if board[x * 4 + y * 1] == board[x * 4 + y * 1 - 4]:
                    return 1
    return 0

# Clears the board for a new game
def reset_board():
    global board_free
    board_free = []
    global board
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Merges any adjacent tiles according to the chosen direction
def bot_merge(direction, new_board):
    valid_turn = 0
    points = 0
    if direction == 'n':
        for x in range(3):
            for y in range(4):
                if new_board[x * 4 + y * 1] != 0:
                    if new_board[x * 4 + y * 1] == new_board[x * 4 + y * 1 + 4]:
                        new_board[x * 4 + y * 1] = new_board[x * 4 + y * 1] * 2
                        new_board[x * 4 + y * 1 + 4] = 0
                        points += new_board[x * 4 + y * 1]
                        valid_turn = 1
    if direction == 's':
        for x in range(3):
            for y in range(4):
                if new_board[15 - (x * 4 + y * 1)] != 0:
                    if new_board[15 - (x * 4 + y * 1)] == new_board[15 - (x * 4 + y * 1 + 4)]:
                        new_board[15 - (x * 4 + y * 1)] = new_board[15 - (x * 4 + y * 1)] * 2
                        new_board[15 - (x * 4 + y * 1 + 4)] = 0
                        points += new_board[15 - (x * 4 + y * 1)]
                        valid_turn = 1
    if direction == 'e':
        for x in range(4):
            for y in range(3):
                if new_board[x * 4 + (3 - y * 1)] != 0:
                    if new_board[x * 4 + (3 - y * 1)] == new_board[x * 4 + (2 - y * 1)]:
                        new_board[x * 4 + (3 - y * 1)] = new_board[x * 4 + (3 - y * 1)] * 2
                        new_board[x * 4 + (2 - y * 1)] = 0
                        points += new_board[x * 4 + (3 - y * 1)]
                        valid_turn = 1
    if direction == 'w':
        for x in range(4):
            for y in range(3):
                if new_board[x * 4 + y * 1] != 0:
                    if new_board[x * 4 + y * 1] == new_board[x * 4 + y * 1 + 1]:
                        new_board[x * 4 + y * 1] = new_board[x * 4 + y * 1] * 2
                        new_board[x * 4 + y * 1 + 1] = 0
                        points += new_board[x * 4 + y * 1]
                        valid_turn = 1
    return [valid_turn, new_board, points]

# Shifts a copy of the board according to the chosen direction
def bot_shift(direction, new_board):
    valid_turn = 0
    if direction == 'n':
        for x in range(3):
            for y in range(4):
                compare_index = x * 4 + y * 1 + 4
                if new_board[x * 4 + y * 1] == 0:
                    while(compare_index <= 15):
                        if new_board[compare_index] != 0:
                            new_board[x * 4 + y * 1] = new_board[compare_index]
                            new_board[compare_index] = 0
                            valid_turn = 1
                            break
                        compare_index += 4
    if direction == 's':
        for x in range(3):
            for y in range(4):
                compare_index = 15 - (x * 4 + y * 1 + 4)
                if new_board[15 - (x * 4 + y * 1)] == 0:
                    while(compare_index >= 0):
                        if new_board[compare_index] != 0:
                            new_board[15 - (x * 4 + y * 1)] = new_board[compare_index]
                            new_board[compare_index] = 0
                            valid_turn = 1
                            break
                        compare_index -= 4
    if direction == 'e':
        for x in range(4):
            for y in range(3):
                compare_index = x * 4 + (2 - y * 1)
                if new_board[x * 4 + (3 - y * 1)] == 0:
                    while(compare_index >= x * 4):
                        if new_board[compare_index] != 0:
                            new_board[x * 4 + (3 - y * 1)] = new_board[compare_index]
                            new_board[compare_index] = 0
                            valid_turn = 1
                            break
                        compare_index -= 1
    if direction == 'w':
        for x in range(4):
            for y in range(3):
                compare_index = x * 4 + y * 1 + 1
                if new_board[x * 4 + y * 1] == 0:
                    while(compare_index <= x * 4 + 3):
                        if new_board[compare_index] != 0:
                            new_board[x * 4 + y * 1] = new_board[compare_index]
                            new_board[compare_index] = 0
                            valid_turn = 1
                            break
                        compare_index += 1
    return [valid_turn, new_board]

# Processes potential new moves
def bot_next_move_process(direction, new_board):
    first_shift = bot_shift(direction, new_board)
    merge = bot_merge(direction, first_shift[1])
    second_shift = bot_shift(direction, merge[1])

    if first_shift[0] == 1 or merge[0] == 1 or second_shift[0] == 1:
        return [1, second_shift[1], merge[2]]
    else:
        return [0, new_board, 0]

# Chooses the best move from the four cardinal directions
def bot_next_move(depth, new_board, points):
    valid_moves = []

    north_move = bot_next_move_process('n', new_board.copy())
    south_move = bot_next_move_process('s', new_board.copy())
    east_move = bot_next_move_process('e', new_board.copy())
    west_move = bot_next_move_process('w', new_board.copy())
    #n_next_north_move = bot_next_move(depth - 1, north_move[1].copy())
    
    if depth > 1:
        next_north_move = bot_next_move(depth - 1, north_move[1].copy(), north_move[2] + points)
        next_south_move = bot_next_move(depth - 1, south_move[1].copy(), south_move[2] + points)
        next_east_move = bot_next_move(depth - 1, east_move[1].copy(), east_move[2] + points)
        next_west_move = bot_next_move(depth - 1, west_move[1].copy(), west_move[2] + points)

        north_move = next_north_move
        south_move = next_south_move
        east_move = next_east_move
        west_move = next_west_move
    
    if north_move[0] == 1:
        valid_moves.append(north_move)
    if south_move[0] == 1:
        valid_moves.append(south_move)
    if east_move[0] == 1:
        valid_moves.append(east_move)
    if west_move[0] == 1:
        valid_moves.append(west_move)

    if len(valid_moves) > 0:
        best_move = valid_moves[0]
        for x in range(len(valid_moves)):
            #print(valid_moves[x])
            if valid_moves[x][2] > best_move[2]:
                best_move = valid_moves[x]
        return best_move
    else:
        #try different values if bugs
        return [0, new_board, points]
        

# Plays the specified amount of games prioritizing moves
# which grant the most points
def autoplay_bot(games_total, depth):
    global board
    global points
    global user_input
    total_points = 0
    max_points = 0
    best_board = board
    games = 0

    while (games < games_total):
        points = 0
        reset_board()
        place_tile()
        while (user_input != 'q'):
            next_move = bot_next_move(depth, board, 0)
            if next_move[0] == 1:
                points += next_move[2]
                board = next_move[1]
                place_tile()
            elif user_input != '':
                print("No valid moves")
                pass

            #Un-comment this for a turn log
            #clean_print()
            
            #check here for game over
            if 0 not in board:
                if check_game_over() == 0:
                    #print("Game over")
                    #print("Points:")
                    #print(points)
                    break

            #user_input = input("Enter input:")
            user_input = auto_valid_moves[random.randint(0, 3)]

        total_points += points
        if points > max_points:
            max_points = points
            best_board = board
        games += 1

    print("Average bot score was:")
    print(total_points / games_total)
    print("Best bot score was:")
    print(max_points)
    print("Best bot board was:")
    for x in range(4):
        for y in range(4):
            print(f"{best_board[x * 4 + y * 1] : <5}", end = " ")
        print()
        print()
    print()

## Un-comment the code below to play manually. Remember to specify one game
## In the main body for autoplay_random()
    
# Plays the specified amount of games with random inputs
def autoplay_random(games_total):
    global points
    global user_input
    max_points = 0
    total_points = 0
    best_board = []
    games = 0

    while (games < games_total):
        points = 0
        reset_board()
        place_tile()
        while (user_input != 'q'):
            if next_move() == 1:
                place_tile()
            elif user_input != '':
                print("Invalid move")
                pass

            #Un-comment this line for a turn log
            clean_print()
            
            #check here for game over
            if 0 not in board:
                if check_game_over() == 0:
                    print("Game over")
                    print("Points:")
                    print(points)
                    break

            #Switch the comment state of the two lines below to play manually
            user_input = input("Enter input:")
            #user_input = auto_valid_moves[random.randint(0, 3)]
            
            while (user_input not in valid_moves):
                user_input = input("Input not valid. Choose 'n', 's', 'e', 'w', or 'q' to quit:")

        total_points += points
        if points > max_points:
            max_points = points
            best_board = board
        games += 1

    #print("Average random score was:")
    #print(total_points / games_total)
    #print("Best random score was:")
    #print(max_points)
    #print("Best random board was:")
    #for x in range(4):
    #    for y in range(4):
    #        print(f"{best_board[x * 4 + y * 1] : <5}", end = " ")
    #    print()
    #    print()
    #print()

# The main body begins here
#games_total = input("Enter the amount of games to simulate:")
#depth = input("Enter depth (4+ will take a long time):")
#intro_string = "For games (this may take a couple seconds):"
#print(f"For {games_total} games (this may take a couple seconds):")
#print()
#autoplay_bot(int(games_total), int(depth))
autoplay_random(1)
close = input("Enter to close")
    
