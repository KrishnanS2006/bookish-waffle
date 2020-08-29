import pygame

class Soap1:
    def __init__(self, x, y, img, width, height):
        self.x = x
        self.y = y
        self.movement = 5
        self.img = img
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_alive = True

    def move(self):
        if self.is_alive and self.y + self.height > 800:
            self.is_alive = False
        self.y += self.movement

    def update(self):
        self.move()
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        if self.is_alive:
            win.blit(self.img, (self.x, self.y))

class Soap2:
    def __init__(self, x, y, img, width, height):
        self.x = x
        self.y = 800 - height - y
        self.movement = 5
        self.img = img
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_alive = True

    def move(self):
        if self.is_alive and self.y + self.height > 800:
            self.is_alive = False
        self.y -= self.movement

    def update(self):
        self.move()
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        if self.is_alive:
            win.blit(self.img, (self.x, self.y))

class Soap3:
    def __init__(self, x, y, img, width, height):
        self.x = y
        self.y = x
        self.movement = 5
        self.img = img
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_alive = True

    def move(self):
        if self.is_alive and self.y + self.height > 800:
            self.is_alive = False
        self.x += self.movement

    def update(self):
        self.move()
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        if self.is_alive:
            win.blit(self.img, (self.x, self.y))

class Soap4:
    def __init__(self, x, y, img, width, height):
        self.x = 1000 - width - y
        self.y = x
        self.movement = 5
        self.img = img
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_alive = True

    def move(self):
        if self.is_alive and self.y + self.height > 800:
            self.is_alive = False
        self.x -= self.movement

    def update(self):
        self.move()
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        if self.is_alive:
            win.blit(self.img, (self.x, self.y))