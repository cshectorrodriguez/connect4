import connectfour

def print_board(game_state: connectfour.GameState) -> None:
    '''Displays the current state of the game board to the console.'''
    for col in range(connectfour.BOARD_COLUMNS):
        print(col+1, end=" ")
    print()
    for row in range(connectfour.BOARD_ROWS):
        rows = ""
        for col in range(connectfour.BOARD_COLUMNS):
            if game_state.board[col][row] == connectfour.NONE:
                rows += ". "
            if game_state.board[col][row] == connectfour.RED:
                rows += "R "
            if game_state.board[col][row] == connectfour.YELLOW:
                rows += "Y "
        print(rows[:-1])

def print_welcome() -> None:
    '''Prints a welcome statement to the user.'''
    print("Welcome to Connect Four!")

def print_user(username: str) -> None:
    '''Prints a welcome statment including a given username to the user.'''
    print(f"Welcome {username}!")

def prompt_host() -> str:
    '''Prompts the user for a host until given a valid input.'''
    while True:
        host = input("Host: ").strip()
        if host=='':
            print('Not a valid host; please try again')
        else:
            return host

def prompt_port() -> int:
    '''Prompts the user for a port until given a valid input.'''
    while True:
        try:
            port = int(input('Port: ').strip())
            if port < 0 or port > 65535:
                print('Not a valid port; please try again')
            else:
                return port
        except ValueError:
            print('Not a valid port; please try again')

def prompt_user() -> str:
    '''Prompts the user for a username until given a valid username.'''
    while True:
        user = input("Username: ").strip()
        if user == '':
            print("Not a valid username; please try again")
        elif len(user.split(" ")) > 1:
            print("Not a valid username; please try again")
        else:
            return user

def print_turn(game_state: connectfour.GameState) -> None:
    '''Prints the player that has the current turn.'''
    if game_state.turn == connectfour.RED:
        print("Turn: Red")
    if game_state.turn == connectfour.YELLOW:
        print("Turn: Yellow")

def prompt_choice() -> str:
    '''Prompts the user for the type of move they want to make until given a valid choice.'''
    while True:
            choice = input("Drop or Pop: ").strip().upper()
            if choice == "DROP" or choice == "POP":

                return choice
            else:
                print("Not a valid choice; please try again")

def prompt_col() -> int:
    '''Prompts the user for a column number until given a valid column number.'''
    while True:
            col = input("Column: ").strip()
            try:
                col_num = int(col)
                if col_num in list(range(1, connectfour.BOARD_COLUMNS + 1)):
                    return col_num
                else:
                    print("Not a valid column; please try again")
            except:
                print("Not a valid column; please try again")

def make_move(game_state: connectfour.GameState, choice: str, column_num: int) -> connectfour.GameState:
    '''Makes a move given a move choice (drop/pop) and a column number.'''
    if choice == "DROP":
        return connectfour.drop(game_state, column_num - 1)
    if choice == "POP":
        return connectfour.pop(game_state, column_num - 1)

def winner(win):
    '''Prints the winner of the game.'''
    if win == connectfour.RED:
        print("Winner: Red")
    else:
        print("Winner: Yellow")
