import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    """A class to manage balls fired from the ship"""

    def __init__(self, ai_game):
        """Create a ball object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.ball_color

        # Create a ball rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.ball_width,
            self.settings.ball_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the ball's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move the ball up the screen."""
        # Update the decimal position of the ball.
        self.y -= self.settings.ball_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_ball(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
