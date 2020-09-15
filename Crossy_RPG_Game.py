# Pygame development


# Gain access to pygame library
import pygame

# Size of the screen
SCREEN_TITLE = "Crossy"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Colors according to RGB codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

# Clock used to update gane events and frames
clock = pygame.time.Clock()

class Game:

    # Typical rate of 60, equivalent to FPS
    TICK_RATE = 60

    # Initializer for the game class to set up the width, height and title
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # Create the window of specified size in white to display the game
        self.game_screen = pygame.display.set_mode((width, height))

        # Set the game window color to white
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

    def run_game_loop(self):
        is_game_over = False
        direction = 0

        player_character = PlayerCharacter('player.png', 375, 700, 50, 50)
        enemy_0 = EnemyCharacter('enemy.png', 20, 400, 50, 50)
        treasure = GameObject('treasure.png', 375, 50, 50, 50)

        # Main game loop, used to update all gameplay such as movement, checks and graphics
        # Runs until is_game_over = True
        while not is_game_over:

            # A loop to get all of the events occuring at any given time
            # Events are most often mouse movement, mouse and button clicks or exit events
            for event in pygame.event.get():
                # If we have a quit type event (exit out) then exit out of the game loop
                if event.type == pygame.QUIT:
                    is_game_over = True
                # Detect when key is pressed down    
                elif event.type == pygame.KEYDOWN:
                    # Move up if up key is pressed
                    if event.key == pygame.K_UP:
                        direction = 1
                    # Move down if down key is pressed    
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                # Detect when key is released        
                elif event.type == pygame.KEYUP:
                    # Stop movement when key is no longer pressed
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                    
                print(event)

            # Redraw the screen to be a white window
            self.game_screen.fill(WHITE_COLOR)

            # Draw the treasure
            treasure.draw(self.game_screen)

            # Update the player position
            player_character.move(direction, self.height)
            # Draw the player at the new position
            player_character.draw(self.game_screen)

            # Move and draw enemy character
            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)

            # Deciding if game is over on collision with enemy/treasure
            if player_character.detect_collision(enemy_0):
                is_game_over = True
            elif player_character.detect_collision(treasure):
                is_game_over = True
                
            # Update all game graphcis
            pygame.display.update()
            # Tick the clock to update everything within the game
            clock.tick(self.TICK_RATE)

# Generic game object class to be subclassed by other objects in the game
class GameObject:

    def __init__(self, image_path, x, y, width, height):

        # Load the player image from file directory
        object_image = pygame.image.load(image_path)
        # Scaled image up
        self.image = pygame.transform.scale(object_image, (width, height))

        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

    # Draw the object by blitting it onto the background (game screen)
    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

# Class to represent the character controlled by the player
class PlayerCharacter(GameObject):

    # How many tiles the character moves per second
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # Move function will move character up if direction > 0 and down if < 0
    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED

        # Make sure the character never goes past the bottom of the screen
        if self.y_pos >= max_height - 70:
            self.y_pos = max_height - 70

    # Return False (no collision) if y pos and x pos do not overlap
    # Return True x and y pos overlap
    def detect_collision(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False
        
        return True


# Class to represent the enemy character
class EnemyCharacter(GameObject):

    # How many tiles the character moves per second
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # Move function will move character up if direction > 0 and down if < 0
    def move(self, max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 70:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED    
        

pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()



# Quit pygame and the program
pygame.quit()
quit()






# Draw a rectangle on top of the game screen canvas (x, y, width, height)
            # pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
            # Draw a circle on top of the game screen (and on top of rectangle) (x, y, radius)
            # pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)

            # Draw player image on top of the screen at (x, y) position
            # game_screen.blit(player_image, (375, 375))
