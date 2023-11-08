# Checkers!
# Dec 2, 2021
# Colby Campbell

import pygame

user_input = input("Enter your board save or press enter to continue: ")

pygame.init()

# screen
tile_size = 64
screen_size = tile_size * 8
pygame.display.set_caption("Checkers!")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
background_colour = (111, 77, 65)  # The background colour is the colour used for the non-white checkerboard spaces
brown = (215, 190, 170)
green = (32, 127, 25)

# checkers
bc = pygame.image.load("black_checker.png")
bkc = pygame.image.load("black_k_checker.png")
wc = pygame.image.load("white_checker.png")
wkc = pygame.image.load(r"white_k_checker.png")
starting_board = "11111111111100000000333333333333" 
previous_mouse_pos = [-1, -1]
turn = 0
first_move = True


class Checker:

    def __init__(self, x, y, colour, king, selected):
        self.x = x
        self.y = y
        self.colour = colour
        self.king = king
        self.selected = selected


def create_checkerboard(checker_board):
    checker_board = checker_board[:32]  # Limiting the string to 32 digits
    return_checkerboard = []
    for count, num in enumerate(checker_board):
        y = count // 4
        x = (count * 2 + (y % 2)) - (y * 8)
        if num == "1":
            return_checkerboard.append(Checker(x, y, 0, False, False))
        elif num == "2":
            return_checkerboard.append(Checker(x, y, 0, True, False))
        elif num == "3":
            return_checkerboard.append(Checker(x, y, 1, False, False))
        elif num == "4":
            return_checkerboard.append(Checker(x, y, 1, True, False))
    return return_checkerboard


# Used for sorting the board list in order based on their x and y positions
def sort(value):
    return (value.y * 10) + value.x


# May break at a later time, keep save_checkerboard2 just in case. The sort is needed for it to work so if it doesn't
# work you will have to use the other function instead.
def save_checkerboard(checker_board):
    checker_board.sort(key=sort)
    return_string = ""
    count = 0
    for piece in checker_board:
        while piece.x != (count * 2 + (count // 4 % 2)) - (count // 4 * 8) or piece.y != count // 4:
            return_string += "0"
            count += 1
        if piece.colour == 0:
            if piece.king:
                return_string += "2"
            else:
                return_string += "1"
        else:
            if piece.king:
                return_string += "4"
            else:
                return_string += "3"
        count += 1
    return return_string


# This one works just as well as the other, but may be less efficient?
def save_checkerboard2(checker_board):
    return_string = ""
    for count in range(0, 32):
        pos_match = False
        for piece in checker_board:
            if piece.x == (count * 2 + (count // 4 % 2)) - (count // 4 * 8) and piece.y == count // 4:
                if piece.colour == 0:
                    if piece.value == 0:
                        return_string += "1"
                    else:
                        return_string += "2"
                else:
                    if piece.value == 0:
                        return_string += "3"
                    else:
                        return_string += "4"
                pos_match = True
                break
        if not pos_match:
            return_string += "0"
    return return_string


def draw_checkerboard(colour1, colour2):
    screen.fill(colour1)
    for x in range(8):
        for y in range(8):
            if y % 2 == 0:
                if x % 2 == 1:
                    pygame.draw.rect(screen, colour2, (x * tile_size, y * tile_size, tile_size, tile_size))
            else:
                if x % 2 == 0:
                    pygame.draw.rect(screen, colour2, (x * tile_size, y * tile_size, tile_size, tile_size))


def draw_checkers(checker_board):
    for piece in checker_board:
        if piece.colour == 0:  # Black is 0
            if piece.king:
                screen.blit(bkc, (piece.x * tile_size, piece.y * tile_size))
            else:
                screen.blit(bc, (piece.x * tile_size, piece.y * tile_size))
        else:
            if piece.king:
                screen.blit(wkc, (piece.x * tile_size, piece.y * tile_size))
            else:
                screen.blit(wc, (piece.x * tile_size, piece.y * tile_size))


def select_checker(checker_board, piece_turn, mouse_pos):
    x_pos = mouse_pos[0] // 64
    y_pos = mouse_pos[1] // 64
    found_checker = False
    for piece in checker_board:
        if piece.x == x_pos and piece.y == y_pos and piece.colour == piece_turn:
            for clear_piece in checker_board:  # Clears the old piece selection when a new one is found
                clear_piece.selected = False
            piece.selected = True
            found_checker = True
    if not found_checker:
        return x_pos, y_pos


# The most spaghetti code of all time, but it works? (I think it works anyway...)
def find_highlighted(checker_board, starting_point, colour, king, mouse_pos):
    highlight = []
    move = False
    delete = None
    # The y-list decides whether or not the piece can move up, down, or both
    if colour == 0 and not king:
        y_list = (1, 1)
    elif colour == 1 and not king:
        y_list = (-1, -1)
    else:
        y_list = (1, -1)
    # This is the beginning of the loops!
    for y_move in y_list:
        if 0 > starting_point[1] + y_move > 7:
            continue
        for x_move in (1, -1):
            # Takes the starting point (where the selected piece is) and adds the y_move and the x_move
            end_point = (starting_point[0] + x_move, starting_point[1] + y_move)
            # Checks to see if the checker is off the board
            if end_point[0] not in range(0, 8) or end_point[1] not in range(0, 8):
                continue
            checker_match = False
            for piece in checker_board:
                # Checks to see if there are any pieces diagonally
                if piece.x == end_point[0] and piece.y == end_point[1]:
                    checker_match = True
                    # If the checker is a different colour, so we know whether or not it can jump over the piece
                    if piece.colour != colour:
                        checker_match2 = False
                        end_point2 = (end_point[0] + x_move, end_point[1] + y_move)
                        # Checks to see if the checker is off the board (again)
                        if end_point2[0] not in range(0, 8) or end_point2[1] not in range(0, 8):
                            break
                        for piece2 in checker_board:
                            # Checks to see if there is another checker piece after the first that could block the jump
                            if piece2.x == end_point2[0] and piece2.y == end_point2[1]:
                                checker_match2 = True  # Found another checker
                        # Didn't find another checker piece after the first, meaning the possible jump is not blocked
                        if not checker_match2:
                            highlight.append(end_point2)
                            if mouse_pos is not None:
                                if end_point2 == mouse_pos and end_point2 == mouse_pos:
                                    delete = end_point
                                    move = True
            # If there are no checker diagonally, allow that as a possible jump
            if not checker_match and first_move:
                highlight.append(end_point)
                if mouse_pos is not None:
                    if end_point == mouse_pos:
                        move = True
    return highlight, move, delete


def highlight_moves(checker_board, mouse_pos):
    global turn, first_move
    for piece in checker_board:
        if piece.selected:
            returned = find_highlighted(checker_board, (piece.x, piece.y), piece.colour, piece.king, mouse_pos)
            move = returned[-2]
            delete = returned[-1]
            highlight = []
            for item in returned[0]:
                if item is bool:
                    break
                highlight.append(item)
            for piece2 in highlight:
                pygame.draw.rect(screen, green, (piece2[0] * tile_size, piece2[1] * tile_size, tile_size, tile_size))
            if delete is None:
                if not first_move and not highlight:
                    if turn == 0:
                        turn = 1
                    else:
                        turn = 0
                    first_move = True
                    piece.selected = False
            else:
                for piece2 in checker_board:
                    if piece2.x == delete[0] and piece2.y == delete[1]:
                        checker_board.remove(piece2)
            if move:
                if piece.y + 1 == mouse_pos[1] or piece.y - 1 == mouse_pos[1]:
                    if turn == 0:
                        turn = 1
                    else:
                        turn = 0
                    first_move = True
                    piece.selected = False
                else:
                    first_move = False
                piece.x = mouse_pos[0]
                piece.y = mouse_pos[1]
            break


def king_convert(checker_board):
    for piece in checker_board:
        if piece.colour == 1 and piece.y == 0:
            piece.king = True
        elif piece.colour == 0 and piece.y == 7:
            piece.king = True


# Testing board list code
# for piece in board:
#     print("x:" + str(piece.x) + " y:" + str(piece.y) + " value:" + str(piece.value) + " colour:" + str(piece.colour))


# Using the user input
if user_input == "":
    board = create_checkerboard(starting_board)
else:
    board = create_checkerboard(user_input)

# Create the screen
screen = pygame.display.set_mode((screen_size, screen_size))

# Main game loop
running = True
while running:

    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            exit()
        # Press the "s" key to save the board
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            print(save_checkerboard(board))
        # Find mouse position when clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            previous_mouse_pos = select_checker(board, turn, pygame.mouse.get_pos())

    draw_checkerboard(background_colour, brown)  # Draw the checkerboard

    highlight_moves(board, previous_mouse_pos)  # Highlights possible moves

    king_convert(board)

    draw_checkers(board)  # Drawing the checkers

    pygame.display.update()  # Update the screen
