
class Connect4Game:
    """
    Represents a state in the Connect 4 game, with a given board and a player. There are
    two players in the game: 'R' (red player) and 'B' (blue player). A whitespace ' ' in
    the board indicates a free space. The board is represented by a matrix, where the
    rows are numbered up to down (0 corresponds to the upper row).
    """

    def __init__(self, rows, cols, board=None, turn='R'):
        self.rows = rows
        self.cols = cols
        if board:
            self.board = [[board[i][j] for j in range(cols)] for i in range(rows)]
        else:
            self.board = [[' ' for i in range(cols)] for j in range(rows)]
        self.is_terminal = False
        self.winner = None
        self.current_player = turn
        
    def __str__(self):
        to_str = ""
        for i in range(self.cols + 2):
            to_str += "- "
        to_str += '\n'
        for row in self.board:
            to_str += '|'
            for piece in row:
                if piece == 'R':
                    to_str += 'O'
                elif piece == 'B':
                    to_str += 'X'
                else:
                    to_str += ' '
                to_str += ' '
            to_str += ' |\n'
        for i in range(self.cols + 2):
            to_str += "- "
        to_str += '\n  '
        for i in range(self.cols):
            to_str += "%d " % i
        return to_str
    
    # Returns a list with the different actions possible given the state of the board
    def possible_actions(self):
        return [col for col in range(self.cols) if self.board[0][col] == ' ']
    
    # Returns a new state after an action of the game
    def result_state(self, action):
        """
        Completar con el codigo necesario para generar un nuevo estado del juego cuando
        se ejecuta la accion indicada (correpondiente a la insercion de una ficha en la
        columna indicada por <action>). Esta funcion tambien debe indicar si el estado es
        terminal (cuando ya no quedan acciones o cuando hay un ganador) mediante un booleano
        en el atributo <is_terminal>, y si hay un ganador debe indicarse cual es en el 
        atributo <winner>.
        """
        return None
    
    # Returns the list of (action, new_state) possible given the current state
    def successors(self):
        """
        Completar con el codigo necesario para generar una lista con los pares
        (accion, nuevo_estado) que serian accesibles desde el estado actual
        """
        return []
    
    # Returns the utility of the given state
    def utility(self, player):
        if self.winner == player:
            return 1
        elif self.winner:
            return -1
        else:
            return 0
    
    # Changes the turn of the player to play
    def next_player(self):
        if self.current_player == 'R':
            self.current_player = 'B'
        else:
            self.current_player = 'R'
    
    # Checks if the action played on (row, col) position provokes a win of
    # the current player
    def check_win(self, row, col):
        if (self.four_in_row(row, col, 1, 0) or 
            self.four_in_row(row, col, 0, 1) or 
            self.four_in_row(row, col, 1, 1) or 
            self.four_in_row(row, col, -1, 1)):
            self.winner = self.board[row][col]
            return True
        else:
            return False
    
    # Auxiliar function to check if there is a winning action on (row, col) given
    # a direction (delta_x, delta_y)
    def four_in_row(self, row, col, delta_x, delta_y):
        player = self.board[row][col]
        counter = 1
        x, y = row + delta_x, col + delta_y
        while 0 <= x < self.rows and 0 <= y < self.cols and self.board[x][y] == player:
            counter += 1
            x, y = x + delta_x, y + delta_y
        x, y = row - delta_x, col - delta_y
        while 0 <= x < self.rows and 0 <= y < self.cols and self.board[x][y] == player:
            counter += 1
            x, y = x - delta_x, y - delta_y
            
        if counter >= 4:
            return True


# Evaluation function for the alpha-beta search

infinity = 1.0e400

def eval_board(state, player):

    if state.winner:
        if player == state.winner:
            score = infinity
        else:
            score =  -infinity
        
    else:
        """
        Completar con el codigo para evaluar un estado intermedio del
        tablero del juego (<state>), segun sea mas o menos beneficioso para el
        jugador <player>
        """
        score = 0
                    
    return score
    

        