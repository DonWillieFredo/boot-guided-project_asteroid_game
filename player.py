import pygame
from Circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        # Call the parent's constructor, passing x, y, and PLAYER_RADIUS
        super().__init__(x, y, PLAYER_RADIUS)
        
        # Initialize the rotation field
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    #Optionally, override the draw method to visualize the player as a triangle
    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, (255, 255, 255), points, 2) # Draw white triangle

