import random
import copy

from util import Node, StackFrontier, QueueFrontier

class Puzzle():
    def __init__(self):
        self.board = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, None]
        ]
        self.empty_row = 3
        self.empty_col = 3
    
    def __str__(self):
        result = ''
        for row in self.board:
            for item in row:
                if item == None:
                    result += '## '
                elif item < 10:
                    result += f' {item} '
                else:
                    result += f'{item} '
            result += '\n'
            
        return result

    def make_move(self, direction):
        match direction:
            case 'U':
                if self.empty_row < len(self.board)-1:
                    self.board[self.empty_row][self.empty_col] = self.board[self.empty_row+1][self.empty_col]
                    self.empty_row += 1
                    self.board[self.empty_row][self.empty_col] = None
            case 'D':
                if self.empty_row > 0:
                    self.board[self.empty_row][self.empty_col] = self.board[self.empty_row-1][self.empty_col]
                    self.empty_row -= 1
                    self.board[self.empty_row][self.empty_col] = None
            case 'L':
                if self.empty_col < len(self.board[self.empty_row])-1:
                    self.board[self.empty_row][self.empty_col] = self.board[self.empty_row][self.empty_col+1]
                    self.empty_col += 1
                    self.board[self.empty_row][self.empty_col] = None
            case 'R':
                if self.empty_col > 0:
                    self.board[self.empty_row][self.empty_col] = self.board[self.empty_row][self.empty_col-1]
                    self.empty_col -= 1
                    self.board[self.empty_row][self.empty_col] = None

    def scramble(self, num_moves):
        dirs = 'UDLR'
        for i in range(num_moves):
            direction = dirs[random.randint(0, 3)]
            print(direction)
            self.make_move(direction)
            print(puzzle)

    def neighbors(self):
        result = []
        # Is there an up neighbor?
        if self.empty_row < len(self.board)-1:
            new_puzzle = copy.deepcopy(self) 
            new_puzzle.make_move('U')
            result.append(("up", new_puzzle))
        # Is there a down neighbor?
        if self.empty_row > 0:
            new_puzzle = copy.deepcopy(self) 
            new_puzzle.make_move('D')
            result.append(("down", new_puzzle))
        # Is there a left neighbor?
        if self.empty_col < len(self.board[self.empty_row])-1:
            new_puzzle = copy.deepcopy(self) 
            new_puzzle.make_move('L')
            result.append(("left", new_puzzle))
        # Is there a right neighbor?
        if self.empty_col > 0:
            new_puzzle = copy.deepcopy(self) 
            new_puzzle.make_move('R')
            result.append(("right", new_puzzle))
        return result

    def solve(self):
        goal = Puzzle()

        #init frontier
        start = Node(state=self, parent=None, action=None)
        frontier = QueueFrontier()
        frontier.add(start)

        # Explored is a set of String'd versions of the board
        explored = set() 

        while True:
            # If nothing left in frontier, then no path
            if frontier.empty():
                raise Exception("no solution")
        
            # Choose a node from the frontier
            current_node = frontier.remove()

            # If node is the goal, then we have a solution            
            if str(current_node.state) == str(goal):
                # TODO
                print('win')
                return
            
            explored.add(str(current_node.state))

            # Add neighbors to the frontier.
            for action, state in current_node.state.neighbors():
                # TODO: Not going to work.  'in' likely doing ref comparison.
                if not frontier.contains_state(state) and str(state) not in explored: 
                    child = Node(state=state, parent=current_node, action=action)
                    frontier.add(child)


puzzle = Puzzle()
print(puzzle)     
puzzle.scramble(3)

puzzle.solve()
print(puzzle)
