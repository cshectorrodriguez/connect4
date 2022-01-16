import connectfour
import connectfour_design

def main() -> None:
    '''Runs the Connect Four game until the game is over.'''
    new_game = connectfour.new_game()
    connectfour_design.print_welcome()

    while True:
        connectfour_design.print_board(new_game)
        connectfour_design.print_turn(new_game)

        while True:

            try:
                game_choice = connectfour_design.prompt_choice()
                game_column = connectfour_design.prompt_col()

                new_game = connectfour_design.make_move(new_game, game_choice, game_column)
                break

            except:
                print('Not a valid move; try again')

        if _check_win(new_game) == True:
            break

def _check_win(game_state: connectfour.GameState) -> bool:
    '''Checks if there is a winner, prints the game board and prints the winning player.'''
    if connectfour.winner(game_state) != connectfour.NONE:
        connectfour_design.print_board(game_state)
        connectfour_design.winner(connectfour.winner(game_state))
        return True

if __name__ == "__main__":
    main()
