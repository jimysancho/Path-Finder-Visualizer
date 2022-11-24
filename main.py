import pygame
from grid import Grid
from algorithms import bfs, dfs, astar

pygame.init()

WIDTH, HEIGHT = 700, 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
ROWS, COLS = 15, 15
LINE_SEP = WIDTH // COLS
if HEIGHT // ROWS > LINE_SEP:
    LINE_SEP = HEIGHT // ROWS

window.fill((255, 255, 255))


def manhattan_distance(init, goal):
    x_diff = abs(init.col - goal.col)
    y_diff = abs(init.row - goal.row)
    return x_diff + y_diff


def draw_path(last_node, g, draw_function):

    current_node = last_node
    while current_node.parent is not None:
        parent = current_node.parent
        current_node = parent
        if current_node.color_name == 'yellow':
            continue
        current_node.color = 'green'
        g.update(current_node)
        draw_function()


def draw(win, g, clock, fps=20):

    clock.tick(fps)
    width, height = win.get_width(), win.get_height()
    g.draw_grid(win)

    for i in range(ROWS):
        y = i * LINE_SEP
        pygame.draw.line(win, (0, 0, 0), start_pos=(0, y), end_pos=(width, y))
        for j in range(COLS):
            x = j * LINE_SEP
            pygame.draw.line(win, (0, 0, 0), start_pos=(x, 0), end_pos=(x, width))

    pygame.display.update()


def reset_variables():
    return [False, False, False, False, None, False]


def get_grid_position(x, y):

    x /= LINE_SEP
    x = int(x)
    y /= LINE_SEP
    y = int(y)

    row = y
    col = x

    return row, col


def main():

    algorithms = {'dfs': dfs, 'bfs': bfs, 'astar': astar}
    key = 'astar'
    algorithm = algorithms[key]
    pygame.display.set_caption('PATH VISUALIZER')
    clock = pygame.time.Clock()
    fps = 15
    clock.tick(fps)

    if key == 'astar':
        grid = Grid(ROWS, COLS, LINE_SEP, heuristic=manhattan_distance, init_cost=1)
    else:
        grid = Grid(ROWS, COLS, LINE_SEP, None)

    run = True
    start_node = False
    end_node = False
    remove = False
    solve = False
    last_node = None
    create_maze = False

    while run:

        draw(window, grid, clock=clock)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                key_remove = keys[pygame.K_r]
                key_restore = keys[pygame.K_SPACE]
                key_solve = keys[pygame.K_s]

                if key_remove:
                    remove = True
                elif key_restore:
                    remove = False
                elif key_solve:
                    if start_node and end_node:
                        solve = True
                elif keys[pygame.K_m] and not create_maze:
                    grid.create_maze(draw_function=lambda: draw(window, grid, clock))
                    create_maze = True
                elif keys[pygame.K_c]:
                    start_node, end_node, remove, solve, last_node, create_maze = reset_variables()
                    grid.reset()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                position = get_grid_position(x, y)
                node = grid.return_node(position)

                if node.color_name == 'white' and not start_node:
                    node.color = 'yellow'
                    grid.update(node)
                    start_node = not start_node
                elif node.color_name == 'white' and start_node and not end_node:
                    node.color = 'red'
                    grid.update(node)
                    end_node = not end_node
                elif node.color_name == 'yellow' and end_node and start_node:
                    node.color = 'white'
                    grid.update(node)
                    start_node = not start_node
                elif node.color_name == 'red' and end_node and start_node:
                    node.color = 'white'
                    grid.update(node)
                    end_node = not end_node

            if pygame.mouse.get_pressed()[0]:

                if start_node and end_node:
                    x, y = pygame.mouse.get_pos()
                    position = get_grid_position(x, y)
                    node = grid.return_node(position)

                    if node.color_name not in ['yellow', 'red'] and not remove:
                        node.color = 'black'
                        grid.update(node)
                    elif node.color_name == 'black' and remove:
                        node.color = 'white'
                        grid.update(node)

        if solve and start_node and end_node:
            if last_node is None:
                last_node = algorithm(grid, lambda: draw(window, grid, clock=clock))
                if last_node is None:
                    start_node, end_node, remove, solve, last_node, create_maze = reset_variables()
                    grid.reset()
            else:
                draw_path(last_node, grid, lambda: draw(window, grid, clock=clock))

        pygame.display.update()


if __name__ == "__main__":
    main()
