import pygame
import random
import sys


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE


ZOMBIE_COLOR = (255, 0, 0)
HUMAN_COLOR = (0, 0, 255)
MEDIC_COLOR = (0, 255, 0)
BACKGROUND_COLOR = (0, 0, 0)


FPS = 30


class Entity(pygame.sprite.Sprite):
    """
    Base class for all moving entities in the simulation.
Handles basic movement and screen boundary checks.
"""
def __init__(self, x, y, color):
       super().__init__()
       self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
       self.image.fill(color)
       self.rect = self.image.get_rect()
       # Position entities on the grid
       self.rect.x = x * CELL_SIZE
       self.rect.y = y * CELL_SIZE


       # Movement direction (dx, dy) - can be -1, 0, or 1 for grid movement
       self.dx = random.choice([-1, 0, 1])
       self.dy = random.choice([-1, 0, 1])


def update(self):
       """
       Updates the entity's position and handles screen boundaries.
       """
       # Move the entity by one CELL_SIZE in its current direction
       self.rect.x += self.dx * CELL_SIZE
       self.rect.y += self.dy * CELL_SIZE


       # Boundary checks: Reverse direction if hitting screen edges
       if self.rect.left < 0:
           self.rect.left = 0
           self.dx = 1 # Move right
       elif self.rect.right > SCREEN_WIDTH:
           self.rect.right = SCREEN_WIDTH
           self.dx = -1 # Move left


       if self.rect.top < 0:
           self.rect.top = 0
           self.dy = 1 # Move down
       elif self.rect.bottom > SCREEN_HEIGHT:
           self.rect.bottom = SCREEN_HEIGHT
           self.dy = -1 # Move up


       # Randomly change direction occasionally for more dynamic movement
       if random.random() < 0.1: # 10% chance to change direction each frame
           self.dx = random.choice([-1, 0, 1])
           self.dy = random.choice([-1, 0, 1])


# --- Human Class ---
class Human(Entity):
   """
   Represents a human entity.
   Can be converted into a zombie.
   """
   def __init__(self, x, y):
       super().__init__(x, y, HUMAN_COLOR)
       self.is_zombie = False # Track if the human has become a zombie


   def turn_into_zombie(self):
       """
       Changes the human's appearance and state to a zombie.
       """
       self.image.fill(ZOMBIE_COLOR)
       self.is_zombie = True


# --- Zombie Class ---
class Zombie(Entity):
   """
   Represents a zombie entity.
   Infects humans on collision.
   """
   def __init__(self, x, y):
       super().__init__(x, y, ZOMBIE_COLOR)

class medic(Human):
     """
     Represents a human entity
   Can be converted into a zombie.
    """
   def __init__(self, x, y):
       super().__init__(x, y, MEDIC_COLOR)

    
        


# --- Main Game Function ---
def main():
   """
   Initializes Pygame, sets up the game window, and runs the main game loop.
   """
   pygame.init() # Initialize all the Pygame modules
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Set up the display window
   pygame.display.set_caption("Infection Simulator") # Set the window title
   clock = pygame.time.Clock() # Create a clock object to control frame rate


   # Sprite groups for managing entities
   all_entities = pygame.sprite.Group() # Group for all entities (for drawing and updating)
   humans = pygame.sprite.Group()       # Group specifically for human entities
   zombies = pygame.sprite.Group()      # Group specifically for zombie entities


   # --- Game Setup: Create Initial Entities ---
   # Create initial zombies
   for _ in range(10): # Start with 10 zombies
       x = random.randint(0, GRID_WIDTH - 1)
       y = random.randint(0, GRID_HEIGHT - 1)
       zombie = Zombie(x, y)
       all_entities.add(zombie)
       zombies.add(zombie)


   # Create initial humans
   for _ in range(40): # Start with 40 humans
       x = random.randint(0, GRID_WIDTH - 1)
       y = random.randint(0, GRID_HEIGHT - 1)
       human = Human(x, y)
       all_entities.add(human)
       humans.add(human)


   # --- Game Loop ---
   running = True
   while running:
       # Event handling
       for event in pygame.event.get():
           if event.type == pygame.QUIT: # Check if the user clicked the close button
               running = False


       # Update all entities' positions
       all_entities.update()


       # --- Collision Detection and Infection Logic ---
       # Iterate through each zombie to check for collisions with humans
       for zombie in zombies:
           # spritecollide returns a list of all sprites in a group that have collided with the given sprite
           # The 'True' argument means that the collided human sprites will be removed from the 'humans' group
           collided_humans = pygame.sprite.spritecollide(zombie, humans, False) # Don't remove immediately


           for human in collided_humans:
               if not human.is_zombie: # Only infect if the human is not already a zombie
                   human.turn_into_zombie() # Change the human's state and color
                   humans.remove(human)     # Remove from humans group
                   zombies.add(human)       # Add to zombies group (now it's a zombie)


       # --- Drawing ---
       screen.fill(BACKGROUND_COLOR) # Fill the screen with black each frame
       all_entities.draw(screen)     # Draw all entities to the screen


       pygame.display.flip() # Update the full display Surface to the screen
       clock.tick(FPS)       # Control the frame rate


   pygame.quit() # Uninitialize Pygame modules
   sys.exit()    # Exit the program


# --- Run the Game ---
if __name__ == "__main__":
    main()



