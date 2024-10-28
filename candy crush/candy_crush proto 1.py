import pygame
import random

# Initialisation de Pygame
pygame.init()

# Constantes
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
GRID_SIZE = 8
TILE_SIZE = SCREEN_WIDTH // GRID_SIZE
COLORS = [(25, 40, 70), (20, 25, 80), (0, 50, 255), (255, 255, 80), (255, 165, 20), (128, 50, 128)]

# Création de l'écran
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Candy Crush ")

# Fonction pour créer la grille
def create_grid():
    return [[random.choice(COLORS) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Fonction pour dessiner la grille
def draw_grid(grid):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            pygame.draw.rect(screen, grid[y][x], (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, (0, 0, 0), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

# Boucle principale
def main():
    grid = create_grid()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((25, 25, 25))  # Remplir l'écran de violet
        draw_grid(grid)  # Dessiner la grille
        pygame.display.flip()  # Mettre à jour l'écran

    pygame.quit()

if __name__ == "__main__":
    main()