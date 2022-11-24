from node import Node, GridLocation


class Grid:

    GOAL_COLOR = 'red'
    BEGIN_COLOR = 'yellow'

    def __init__(self, rows, cols, line_separation, heuristic=None, init_cost=None):

        self.rows = rows
        self.cols = cols

        self.grid = [[Node(GridLocation(i, j), None, line_separation,
                           cost=init_cost) for j in range(self.cols)]
                     for i in range(self.rows)]

        self.heuristic = heuristic
        self.line_sep = line_separation
        self.cost = init_cost

    def draw_grid(self, window):
        for row in self.grid:
            for node in row:
                node.draw_node(window)

    def return_node(self, position):
        row, col = position
        return self.grid[row][col]

    def update(self, node):
        row, col = node.row, node.col
        self.grid[row][col] = node

    def child_nodes(self, node):
        row, col = node.row, node.col
        successors = []
        possible_locations = [(row + 1, col), (row - 1, col),
                              (row, col + 1), (row, col - 1)]

        for (r, c) in possible_locations:
            if (0 <= r < self.rows) and (0 <= c < self.cols) and (self.grid[r][c].color_name != 'black'):
                successors.append(GridLocation(r, c))

        return successors

    def get_init_goal(self):

        init = None
        goal = None
        for row in self.grid:
            for node in row:
                if node.color_name == self.GOAL_COLOR:
                    goal = node
                elif node.color_name == self.BEGIN_COLOR:
                    init = node
                if goal and init:
                    return goal, init

    def create_maze(self, draw_function, n=0,
                    sections=None, path=None):

        from random import randrange

        self.init_maze()

        sections = sections if sections is not None else [[(1, self.rows - 1), (1, self.cols - 1)]]
        path = path if path is not None else set()

        if not sections:
            return

        section = sections.pop(0)
        rows_section, cols_section = section
        begin_row, end_row = rows_section
        begin_col, end_col = cols_section

        height = end_row - begin_row
        width = end_col - begin_col

        if width > 1 and height > 1:
            if width > height:
                col = randrange(begin_col, end_col) if begin_col != end_col else begin_col
                for nodes in self.grid[begin_row: end_row]:
                    for c, node in enumerate(nodes[begin_col: end_col]):
                        if c + begin_col == col:
                            node.color = 'black' if node.state not in path else node.color_name
                            self.update(node)

                row = randrange(begin_row, end_row)
                node = self.return_node((row, col))
                node.color = 'white'
                self.update(node)

                path.add(node.state)

                new_sections = [[(begin_row, end_row), (begin_col, col - 1)],
                                [(begin_row, end_row), (col + 1, end_col)]]

            else:
                row = randrange(begin_row, end_row) if begin_row != end_row else begin_row
                for r, nodes in enumerate(self.grid[begin_row: end_row]):
                    for node in nodes[begin_col: end_col]:
                        if r + begin_row == row:
                            node.color = 'black' if node.state not in path else node.color_name
                            self.update(node)

                col = randrange(begin_col, end_col)
                node = self.return_node((row, col))
                node.color = 'white'
                self.update(node)
                path.add(node.state)

                new_sections = [[(begin_row, row - 1), (begin_col, end_col)],
                                [(row + 1, end_row), (begin_col, end_col)]]

            draw_function()

            for new_section in new_sections[::-1]:
                sections.append(new_section)

            return self.create_maze(draw_function, n+1,
                                    sections=sections, path=path)

        return self.create_maze(draw_function, n+1,
                                sections=sections, path=path)

    def init_maze(self):

        for r, nodes in enumerate(self.grid):
            for c, node in enumerate(nodes):
                if r in [0, self.rows - 1] or c in [0, self.cols - 1]:
                    node.color = 'black'
                    self.update(node)

    def reset(self):
        self.__init__(self.rows, self.cols, self.line_sep, self.heuristic, self.cost)



