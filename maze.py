import pygame
import numpy as np
import random

pygame.init()

screen_width = 600  
screen_height = 600  
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("This maze game is designed by Ansh ")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


maze_size = 15
cell_size = screen_width // maze_size


maze = np.zeros([maze_size, maze_size], dtype=object)

for _ in range(30):
    row = random.randint(0, maze_size - 1)
    column = random.randint(0, maze_size - 1)
    maze[row][column] = 1

start_point = [0, random.randint(0, maze_size - 1)]
end_point = [maze_size - 1, random.randint(0, maze_size - 1)]

maze[start_point[0], start_point[1]] = 'SSS'
maze[end_point[0], end_point[1]] = 'EEE'


player_position = start_point[:]


steps = 0

# Print game designer's name
designer_name = "Ansh"
print("Game designed by", designer_name)



random_number = random.randrange(10, 16)  
print("Reach the ball within number",random_number);


# Define the font
font = pygame.font.Font(None, 30)


designer_text = font.render("Game designed by Ansh", True, WHITE)




screen.blit(designer_text, (10, 10))



pygame.display.flip()



running = True
game_won = False
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if player_position[1] > 0 and maze[player_position[0], player_position[1] - 1] != 1:
                    player_position[1] -= 1
                    steps += 1
            elif event.key == pygame.K_RIGHT:
                if player_position[1] < maze_size - 1 and maze[player_position[0], player_position[1] + 1] != 1:
                    player_position[1] += 1
                    steps += 1
            elif event.key == pygame.K_UP:
                if player_position[0] > 0 and maze[player_position[0] - 1, player_position[1]] != 1:
                    player_position[0] -= 1
                    steps += 1
            elif event.key == pygame.K_DOWN:
                if player_position[0] < maze_size - 1 and maze[player_position[0] + 1, player_position[1]] != 1:
                    player_position[0] += 1
                    steps += 1

    screen.fill(BLACK)

  
    for i in range(maze_size):
        for j in range(maze_size):
            if maze[i][j] == 1:
                pygame.draw.rect(screen, RED, (j * cell_size, i * cell_size, cell_size, cell_size))
            elif maze[i][j] == 0:
                pygame.draw.rect(screen, GREEN, (j * cell_size, i * cell_size, cell_size, cell_size))
            elif maze[i][j] == 'SSS':
                pygame.draw.rect(screen, WHITE, (j * cell_size, i * cell_size, cell_size, cell_size))
                pygame.draw.circle(screen, GREEN, (j * cell_size + cell_size // 2, i * cell_size + cell_size // 2),
                                   cell_size // 4)
            elif maze[i][j] == 'EEE':
                pygame.draw.rect(screen, WHITE, (j * cell_size, i * cell_size, cell_size, cell_size))
                pygame.draw.circle(screen, RED, (j * cell_size + cell_size // 2, i * cell_size + cell_size // 2),
                                   cell_size // 4)

   
    pygame.draw.rect(screen, WHITE, (player_position[1] * cell_size, player_position[0] * cell_size, cell_size, cell_size))

    pygame.display.flip()

    
    if player_position == end_point:
        game_won = True
        break


print("Number of steps:", steps)




if game_won:
    result_text = font.render("Congratulations! You won the game!", True, WHITE)
else:
    result_text = font.render("Best of luck for next time. You lost the game.", True, WHITE)


screen.blit(result_text, (10, 40))


pygame.display.flip()


pygame.time.wait(3000)


pygame.quit()
