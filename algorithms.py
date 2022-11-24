from node import Node
from data_structures import *


def bfs(maze, draw_function):

    goal_node, init_node = maze.get_init_goal()
    frontier = Queue()
    explored = {init_node.state}
    frontier.push(init_node)

    while not frontier.empty:

        current_node = frontier.pop()
        current_state = current_node.state

        if current_state == goal_node.state:
            return current_node

        current_node.color = ('purple' if current_node.state not in [init_node.state, goal_node.state]
                              else current_node.color_name)

        maze.update(current_node)

        for child in maze.child_nodes(current_node):
            if child in explored:
                continue
            child = Node(child, current_node, current_node.rect_dim)
            frontier.push(child)
            explored.add(child.state)
            child.color = 'purple' if child.state not in [goal_node.state] else maze.GOAL_COLOR
            maze.update(child)

            draw_function()

    return None


def dfs(maze, draw_function):

    goal_node, init_node = maze.get_init_goal()
    frontier = Stack()
    frontier.push(init_node)
    explored = {init_node.state}

    while not frontier.empty:

        current_node = frontier.pop()
        current_state = current_node.state

        if current_state == goal_node.state:
            return current_node

        current_node.color = ('purple' if current_node.state not in [init_node.state, goal_node.state]
                              else current_node.color_name)

        maze.update(current_node)

        for child in maze.child_nodes(current_node):
            if child in explored:
                continue
            child = Node(child, current_node, current_node.rect_dim)
            frontier.push(child)
            explored.add(child.state)
            child.color = 'purple' if child.state not in [goal_node.state] else maze.GOAL_COLOR
            maze.update(child)

        draw_function()

    return None


def astar(maze, draw_function):

    goal_node, init_node = maze.get_init_goal()
    init_node.heuristic = maze.heuristic(init_node, goal_node)
    frontier = PriorityQueue()
    frontier.push(init_node)
    explored = {init_node.state: 0}

    while not frontier.empty:

        current_node = frontier.pop()
        current_state = current_node.state

        if current_state == goal_node.state:
            return current_node

        current_node.color = ('purple' if current_node.state not in [init_node.state, goal_node.state]
                              else current_node.color_name)

        maze.update(current_node)

        for child in maze.child_nodes(current_node):
            new_cost = current_node.cost + 1
            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                child = Node(child, current_node, current_node.rect_dim,
                             cost=new_cost, heuristic=maze.heuristic(child, goal_node))
                frontier.push(child)
                child.color = 'blue' if child.state != goal_node.state else maze.GOAL_COLOR
                maze.update(child)

        draw_function()

    return None
