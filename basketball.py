import pygame


# Their curls cascade, a silken sight,
# Like sunlit waves, both dark and bright.
# I wonder if each curl holds a story,
# A love song whispered, full of glory.
# Their laughter rings, a sweet refrain,
# That dances through their curly mane.
# I asked them once, "Do they get in your way?"
# They smiled, "Only when they lead me to you each day!"
# Their curls surround, a soft embrace,
# Like gentle tendrils, finding their place.
# I said their hair was a masterpiece to behold,
# They blushed, "Just like your heart, brave and bold."
# Their hair's a mystery, a tangled art,
# But in their eyes, I see my counterpart.
# And though I may try to make silly jokes,
# My heart's the only truth this poem evokes.


class Basketball(pygame.sprite.Sprite):
    def __init__(self, pos, player, time, direction):
        super().__init__(player.group)

        self.player = player
        self.original_image = pygame.image.load("images/basketball.png").convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.midleft)
        self.direction = direction

        self.group = player.group

        self.speed = 400
        self.time = time
        self.menu = False
        self.collision_state = None

        self.shooting = False

        self.height = 0
        self.velocity = 0
        self.jump_speed = 400
        self.jump_start = 1
        self.gravity = -800

        self.velocity = self.jump_speed
        self.height = self.jump_start

        self.scale_factor = 1.0


    def ball_movement(self):
            
           self.rect.right =- 1

    def update(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))

        self.scale_factor = self.player.scale_factor

        if self.player.height != 0:
            self.shooting = True

        if self.shooting:
            if self.height != 0:
                self.velocity += self.gravity * dt
                self.height += self.velocity * dt
                if self.height < 0:
                    self.height = 0
                    self.velocity = 0
                    self.shooting = False
                    self.group.remove(self)

        self.rect.center = round(self.pos.x), round(self.pos.y - self.height)

        width, height = self.original_image.get_size()
        new_width = int(width * self.scale_factor)
        new_height = int(height * self.scale_factor)

        if new_width != self.rect.width or new_height != self.rect.height:
            self.image = pygame.transform.scale(
                self.original_image, (new_width, new_height)
            )
            self.rect = self.image.get_rect(center=self.rect.center)

        colliding_sprites = pygame.sprite.spritecollide(
            self, self.group, False, pygame.sprite.collide_mask
        )

        colliding_sprites = [
            sprite
            for sprite in colliding_sprites
            if sprite != self and sprite != self.player
        ]


        if colliding_sprites:
            self.ball_movement()

        if self.rect.left > 2100 or self.rect.left < 0 or self.rect.bottom < 0:
            self.ball_movement()
