import pygame
import random
import time

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DFS Maze Solver Visualization")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)      # Target point
GREEN = (0, 255, 0)    # Start point
BLUE = (0, 0, 255)     # Explored area during DFS
YELLOW = (255, 255, 0)  # Final path

# Maze dimensions (rows, cols) and cell size
ROWS, COLS = 30, 30
CELL_SIZE = WIDTH // COLS

# Maze structure (1 for wall, 0 for path)
maze = [[1 for _ in range(COLS)] for _ in range(ROWS)]

# Movement directions: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# DFS algorithm to generate the maze
def generate_maze(x, y):
    maze[x][y] = 0  # Mark the current cell as a path
    random.shuffle(directions)
    
    for dx, dy in directions:
        nx, ny = x + 2 * dx, y + 2 * dy
        if 0 <= nx < ROWS and 0 <= ny < COLS and maze[nx][ny] == 1:
            maze[x + dx][y + dy] = 0  # Knock down the wall
            generate_maze(nx, ny)

    # Ensure a valid path exists to the bottom-right corner
    maze[ROWS - 2][COLS - 1] = 0
    maze[ROWS - 1][COLS - 2] = 0
    maze[ROWS - 1][COLS - 1] = 0

# DFS to solve the maze
visited = set()
path_to_goal = []

def dfs_solve(x, y):
    if (x, y) in visited:
        return False
    visited.add((x, y))

    # Visualize the step (color explored area in BLUE)
    pygame.draw.rect(screen, BLUE, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()
    time.sleep(0.02)  # Slow down for visualization

    if (x, y) == (ROWS - 1, COLS - 1):  # Exit condition (bottom-right corner)
        path_to_goal.append((x, y))
        return True

    # Explore neighbors
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < ROWS and 0 <= ny < COLS and maze[nx][ny] == 0:
            if dfs_solve(nx, ny):
                path_to_goal.append((x, y))  # Append cell to the final path
                return True

    return False

def highlight_path():
    """Highlight the correct path to the goal in yellow."""
    for x, y in reversed(path_to_goal):  # Reverse the path to highlight from start to goal
        pygame.draw.rect(screen, YELLOW, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.display.update()
        time.sleep(0.05)

# Draw the maze on the screen
def draw_maze():
    screen.fill(WHITE)
    for x in range(ROWS):
        for y in range(COLS):
            color = BLACK if maze[x][y] == 1 else WHITE
            pygame.draw.rect(screen, color, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Mark start and end points
    pygame.draw.rect(screen, GREEN, (0 * CELL_SIZE, 0 * CELL_SIZE, CELL_SIZE, CELL_SIZE))  # Start point
    pygame.draw.rect(screen, RED, ((COLS - 1) * CELL_SIZE, (ROWS - 1) * CELL_SIZE, CELL_SIZE, CELL_SIZE))  # Target point
    
    pygame.display.update()

def main():
    running = True

    # Generate the maze
    generate_maze(0, 0)

    # Draw the initial maze
    draw_maze()

    # Solve the maze using DFS from the top-left (0,0) to bottom-right (ROWS-1,COLS-1)
    dfs_solve(0, 0)

    # Highlight the final path after DFS is complete
    highlight_path()

    # Keep the window open after solving
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
