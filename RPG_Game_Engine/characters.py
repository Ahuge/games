
# Gain access to pygame library
import pygame

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
