import pygame


class Character:

    def __init__(self, ai_game):
        """Initialise the character and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the character image and get its rect.
        self.image = pygame.image.load('images/character.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the character at its current location"""
        self.screen.blit(self.image, self.rect)

