# Pygame development


# Gain access to pygame library
import pygame

from characters import EnemyCharacter, PlayableCharacter, GameObject

# Size of the screen
SCREEN_TITLE = "Crossy"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Colors according to RGB codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

# Clock used to update gane events and frames
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)


def construct_level(game_board, things):
    for game_thing in things:
        game_thing.draw(game_board)


class Game:

    # Typical rate of 60, equivalent to FPS
    TICK_RATE = 60

    # Initializer for the game class to set up the width, height and title
    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # Create the window of specified size in white to display the game
        self.game_screen = pygame.display.set_mode((width, height))

        # Set the game window color to white
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

        # Load and set background image for scene
        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))

    def run_game_loop(self, level_speed):
        is_game_over = False
        did_win = False
        direction = 0

        player_character = PlayerCharacter('player.png', 375, 700, 50, 50)
        enemy_0 = EnemyCharacter('enemy.png', 20, 600, 50, 50)
        # Speed increased as advance in difficulty
        enemy_0.SPEED *= level_speed

        # Create another enemy
        enemy_1 = EnemyCharacter('enemy.png', self.width - 40, 400, 50, 50)
        enemy_1.SPEED *= level_speed
        
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
            # Draw image onto background
            self.game_screen.blit(self.image, (0, 0))
            

            # Update the player position
            player_character.move(direction, self.height)

            # Move and draw enemy character
            enemy_0.move(self.width)            

            level_objects = [treasure, player_character, enemy_0]
            construct_level(self.game_screen, level_objects)
            # Draw the treasure
            # treasure.draw(self.game_screen)
            # Draw the player at the new position
            # player_character.draw(self.game_screen)
            # enemy_0.draw(self.game_screen)

            # End game if collision with enemy/treasure
            # Close game if lose
            # Restart game loop if win
            if player_character.detect_collision(enemy_0):
                is_game_over = True
                did_win = False
                text = font.render('You lose!', True, BLACK_COLOR)
                self.game_screen.blit(text, (300, 350))
                pygame.display.update()
                clock.tick(1)
                break
            elif player_character.detect_collision(treasure):
                is_game_over = True
                did_win = True
                text = font.render('You win!', True, BLACK_COLOR)
                self.game_screen.blit(text, (300, 350))
                pygame.display.update()
                clock.tick(1)
                break
                
            # Update all game graphcis
            pygame.display.update()
            # Tick the clock to update everything within the game
            clock.tick(self.TICK_RATE)

        if did_win:
            self.run_game_loop(level_speed + 0.5)
        else:
            return
        

pygame.init()

new_game = Game('background.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop(1)



# Quit pygame and the program
pygame.quit()
quit()






# Draw a rectangle on top of the game screen canvas (x, y, width, height)
            # pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
            # Draw a circle on top of the game screen (and on top of rectangle) (x, y, radius)
            # pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)

            # Draw player image on top of the screen at (x, y) position
            # game_screen.blit(player_image, (375, 375))
