"""
    Alak Board Game
"""
import sys
from itertools import cycle

def new_board(number_of_squares: int):
    """
        Initialise a new board with n squares

        Args:
            number_of_squares (int): The number of square in the board

        Returns:
            list: A list which represents the initial state of the board
    """

    # 0 represent an empty square

    return [0] * number_of_squares

def display(board: list, number_of_squares: int):
    """
        Prints the board

        Args:
            board (list): The list
            number_of_squares (int): The number of squares
    """

    def square_display_value(square_value: int):
        """
            Returns ., x or o based on the square value

            Args:
                square_value (int): The value of a square position within a board

            Returns:
                string: Returns the square display value
        """

        if square_value == 0:
            return "."
        elif square_value == 1:
            return "X"
        elif square_value == 2:
            return "O"

    if board:
        square_state = ''.join(['{0: <3}'.format(
            square_display_value(board[i])) for i in range(0, number_of_squares)])

        square_position = ''.join(['{0: <3}'.format(i+1) for i in range(0, number_of_squares)])

        print('{}\n{}'.format(square_state, square_position))

def possible(board: list, number_of_squares: int, player: int, removed: list, i: int):
    """
        Indicates wheter a player can put a pawn at a particular position on the board

        Args:
            board (list): The game board
            number_of_squares (int): The size of the game board
            player (int): The player who is putting down a pawn
            removed (list): A list that represents the position \
            of previous pawns that have been removed from the board
            i (int): The position where to put the pawn

        Returns:
            boolean: Returns true if it is possible to put down a pawn or else false
    """

    if i < 0 or i > number_of_squares - 1:
        #print(1)
        return False

    if not board:
        #print(2)
        return False

    if i in removed[player-1]:
        #print(3)
        return False

    if board[i] == 0:
        #print(4)
        return True

def select(board: list, number_of_squares: int, player: int, removed: list):
    """
        Asks the player to input a square where she wishes to put her pawn.

        Args:
            board (list): The game board
            number_of_squares (int): The size of the game board
            player (int): The player who is putting down her pawn
            removed (list): The list of previously removed pawns from the board

        Returns:
            int: Returns the square position where the player wishes to put down her pawn
    """

    print('Player {}'.format(player))

    while True:
        try:
            input_value = input('Choose a licit number of square: ')

            if input_value:
                # Zero based index
                square_value = int(input_value) - 1

                if possible(board, number_of_squares, player, removed, square_value):
                    return square_value
        except KeyboardInterrupt:
            # Exit
            sys.exit(0)

def put(board: list, number_of_squares: int, player: int, removed: list, i: int):
    """
        Args:
            board (list): The game board
            number_of_squares (int): The size of the game board
            player (int): The player who is putting down her pawn
            removed (list): The list of previously removed pawns from the board
    """

    if i < number_of_squares:
        board[i] = player

        # Remove on the left hand side

        if i > 0:
            start = None
            end = None

            for j in range(i-1, -1, -1):

                if board[j] == player and isinstance(start, int) and end is None:
                    #print([1.1, i, j, board[j]])
                    end = j + 1
                    break
                elif board[j] == player and start is None:
                    print(1.8)
                    break
                #elif board[j] == player and isinstance(start, int):
                    #print([1.2, i, j, board[j]])
                #   continue
                elif board[j] == 0:
                    #print([1.3, i, j, board[j]])
                    start = None
                    break
                elif board[j] != player and start is None and j == 0:
                    #print([1.4, i, j, board[j]])
                    start = j
                    end = j
                    break
                elif board[j] != player and start is None:
                    #print([1.5, i, j, board[j]])
                    start = j
                elif isinstance(start, int) and end is None and board[j] == player and j == 0:
                    #print([1.6, i, j, board[j]])
                    end = j + 1
                    break
                elif isinstance(start, int) and end is None and \
                             board[j] not in [player, 0]  and j == 0:
                    #print([1.7, i, j, board[j]])
                    end = j

            #print(start)
            #print(end)

            if start is not None and end is not None:
                for j in range(end, start+1):
                    removed[player % 2].append(j)
                    board[j] = 0

        if i < number_of_squares - 1:
            start = None
            end = None

            for j in range(i+1, number_of_squares):

                if board[j] == player and isinstance(start, int) and end is None:
                    #print(2.1)
                    end = j - 1
                    break
                elif board[j] == player and start is None:
                    #print(2.7)
                    break
                #elif board[j] == player and isinstance(start, int):
                #    print(2.2)
                #    continue
                elif board[j] == 0:
                    break
                elif board[j] not in [player, 0] and start is None and j == number_of_squares - 1:
                    #print(2.3)
                    start = j
                    end = j
                    break
                elif board[j] != player and start is None:
                    #print(2.4)
                    start = j
                elif isinstance(start, int) and end is None \
                    and board[j] == player and j == number_of_squares - 1:
                    #print(2.5)
                    end = j
                    break
                elif isinstance(start, int) and end is None and \
                             board[j] not in [player, 0]  and j == number_of_squares - 1:
                    #print(2.6)
                    end = j

            #print(start)
            #print(end)

            if start is not None and end is not None:
                for j in range(start, end+1):
                    removed[player % 2].append(j)
                    board[j] = 0            
            
def again(board: list, number_of_squares: int, player: int, removed: list):
    """
        Checks if a player can put a pawn on the board

        Args:
            board (list): The game board
            number_of_squares (int): The size of the game board
            player (int): The player who is putting down her pawn
            removed (list): The list of previously removed pawns from the board

        Returns:
            boolean: Return True if a player can put a pawn on the board or else False
    """

    number_of_empty_squares = board.count(0)

    number_of_removed_pawns = len(removed)

    return True if number_of_empty_squares - number_of_removed_pawns > 0 else False

def win(board: list, number_of_squares: int):
    """
        Displays the result of the game

        Args:
            board (list): The game board
            number_of_squares (int): The size of the game board
    """

    player_one_count = board.count(1)
    player_two_count = board.count(2)

    if player_one_count > player_two_count:
        print("Winner: 1")
    elif player_one_count < player_two_count:
        print("Winner: 1")
    elif player_one_count == player_two_count:
        print("Winner: Tie")

def alak(number_of_squares: int):
    """
        Alak board game

        Args:
            number_of_squares (int): The size of the game board
    """

    board = new_board(number_of_squares)
    removed_list = [[], []]

    display(board, number_of_squares)

    print("\n")

    player_turns = cycle([1, 2])

    next_turn = next(player_turns)

    while board.count(0) > 0:
        player_input = select(board, number_of_squares, next_turn, removed_list)

        removed_list[next_turn%2] = []

        put(board, number_of_squares, next_turn, removed_list, player_input)

        print("\n")

        display(board, number_of_squares)

        print("\n")

        next_turn = next(player_turns)

    win(board, number_of_squares)

if __name__ == "__main__":
    alak(9)
