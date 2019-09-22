'''import modules'''
import pygame, random, time

pygame.init()
clock = pygame.time.Clock()
show_hitbox = True
map = []
animals = []

'''load sprites'''
screen_img = pygame.image.load("farm_game/Sprites/Wasteland_bg.png")
start_screen_img = pygame.image.load("farm_game/Sprites/start_Wasteland_bg.png")
default_ug_img = pygame.image.load("farm_game/Sprites/default_ug_bg.png")
start_default_ug_img = pygame.image.load("farm_game/Sprites/start_default_ug_bg.png")
player_left_img = pygame.image.load("farm_game/Sprites/Bratan_left.png")
player_right_img = pygame.image.load("farm_game/Sprites/Bratan_right.png")
player_left_shrink_img = pygame.image.load("farm_game/Sprites/Bratan_left_shrink.png")
player_right_shrink_img = pygame.image.load("farm_game/Sprites/Bratan_right_shrink.png")
bolt_left_img = pygame.image.load("farm_game/Sprites/Bolt_left.png")
bolt_right_img = pygame.image.load("farm_game/Sprites/Bolt_right.png")
bolt_left_shrink_img = pygame.image.load("farm_game/Sprites/Bolt_left_shrink.png")
bolt_right_shrink_img = pygame.image.load("farm_game/Sprites/Bolt_right_shrink.png")
platypus_left_img = pygame.image.load("farm_game/Sprites/Platypus_left.png")
platypus_right_img = pygame.image.load("farm_game/Sprites/Platypus_right.png")
cow_left_img = pygame.image.load("farm_game/Sprites/Cow_left.png")
cow_right_img = pygame.image.load("farm_game/Sprites/Cow_right.png")


class Window:

    def __init__(self):
        self.width = 950
        self.height = 950
        self.ground = 700
        self.screen = pygame.display.set_mode((self.width, self.height))

    '''draw background'''
    def draw(self):
        for tile in map:
            self.screen.blit(tile.image, (tile.x - bratan.camera_x, tile.y - bratan.camera_y))

        #self.screen.blit(start_screen_img, (0 - bratan.camera_x, 0 - bratan.camera_y))
        #self.screen.blit(screen_img, (950 - bratan.camera_x, 0 - bratan.camera_y))
        #self.screen.blit(screen_img, (-950 - bratan.camera_x, 0 - bratan.camera_y))
        #self.screen.blit(start_default_ug_img, (0 - bratan.camera_x, 950 - bratan.camera_y))


class World(Window):

    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.image = img

        self.place_x = None
        self.place_y = None
        self.place_img = None
        self.values = []

    def set_position(self, place):
        if place == 0:
            self.place_x = 0
            self.place_y = 0
            self.place_img = start_screen_img

        if place == 1:
            self.place_x = 0
            self.place_y = 1
            self.place_img = start_default_ug_img

        if place != 0 and place != 1:
            self.place_x = place // 2

            if place % 2 == 0:
                self.place_y = 0
                self.place_img = screen_img

            if place % 2 == 1:
                self.place_y = 1
                self.place_img = default_ug_img

        self.values = (950 * self.place_x, 950 * self.place_y, self.place_img)

    def create(self):
        for i in range(-10, 10):
            print(i)
            self.set_position(self, i)
            map.append(self(self.values[0], self.values[1], self.values[2]))

        #map.append(self(950 * 0, 950 * 0, start_screen_img))
        #map.append(self(950 * 1, 950 * 0, screen_img))
        #map.append(self(950 * -1, 950 * 0, screen_img))
        #map.append(self(950 * 0, 950 * 1, start_default_ug_img))


class Player:

    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = [self.x, self.y, self.width, self.height]
        self.vel = vel

        self.shrink_x = self.x
        self.shrink_y = self.y + 45
        self.shrink_width = self.width - 15
        self.shrink_height = self.height -45
        self.shrink_hitbox = [self.shrink_x, self.shrink_y, self.shrink_width, self.shrink_height]
        self.shrink_vel = self.vel * 2

        self.grow_x = self.x
        self.grow_y = self.y
        self.grow_width = self.width
        self.grow_height = self.height
        self.grow_hitbox = [self.grow_x, self.grow_y, self.grow_width, self.grow_height]
        self.grow_vel = self.vel

        self.facing = "left"
        self.camera_x = 0
        self.camera_y = 0
        self.shrinking = False
        self.max_health = 100
        self.health = self.max_health

    '''player movement'''
    def move(self):
        key = pygame.key.get_pressed()

        if self.camera_y == 0 or self.camera_y == game.height:
            if key[pygame.K_d] and self.x <= 1875 - self.width:
                self.facing = "right"
                bolt.facing = "right"
                self.x += self.vel
                if self.shrinking == False:
                    bolt.x = self.x + self.width * 0.4

                if self.shrinking == True:
                    bolt.x = self.x + self.width * 0.025

                self.camera_x += self.vel

        if self.camera_y == 0 or self.camera_y == game.height:
            if key[pygame.K_a] and  self.x >= -925:
                self.facing = "left"
                bolt.facing = "left"
                self.x -= self.vel
                bolt.x = self.x
                self.camera_x -= self.vel

        if self.shrinking == False and -1 < self.camera_x < 25 or self.shrinking == True and -10 < self.camera_x < 40:
            if key[pygame.K_s] and self.camera_y < game.height:
                self.y += self.vel
                self.shrink_y += self.vel
                self.grow_y += self.vel
                bolt.y += self.vel
                self.camera_y += self.vel

                if self.camera_y > game.height:
                    self.camera_y = game.height

            if key[pygame.K_w] and self.camera_y > 0:
                self.y -= self.vel
                self.shrink_y -= self.vel
                self.grow_y -= self.vel
                bolt.y -= self.vel
                self.camera_y -= self.vel

                if self.camera_y < 0:
                    self.camera_y = 0

        if key[pygame.K_ESCAPE]:
            pygame.quit()

    def shrink(self):
        if not self.shrinking:
            if self.facing == "right":
                bolt.x = self.x + self.width * 0.025

            self.y = self.shrink_y
            self.vel = self.shrink_vel
            bolt.y = bolt.y + 30
            bolt.shrink_y = bolt.y
            self.shrinking = True

        else:
            if bolt.shot == False:
                if self.facing == "right":
                    bolt.x = self.x + self.width * 0.4

            self.y = self.grow_y
            self.vel = self.grow_vel
            bolt.y = bolt.y - 30
            bolt.grow_y = bolt.y
            self.shrinking = False

    def check_death(self):
        if self.health <= 0:
            self.x = 450
            self.y = 625
            self.camera_x = 0
            self.camera_y = 0
            self.facing = "left"
            bolt.facing = "left"
            bolt.x = self.x
            bolt.y = self.y + 25
            bratan.shrinking = False
            self.health = self.max_health

    '''draw player on screen'''
    def draw(self):

        if self.shrinking == False:
            if show_hitbox == True:
                pygame.draw.rect(game.screen, (0,0,0), (self.grow_hitbox[0], self.grow_hitbox[1], self.grow_hitbox[2], self.grow_hitbox[3]), 1)
            if self.facing == "left":
                game.screen.blit(player_left_img, (self.x - self.camera_x, self.grow_y - self.camera_y))

            if self.facing == "right":
                game.screen.blit(player_right_img, (self.x - self.camera_x, self.grow_y - self.camera_y))

            pygame.draw.rect(game.screen, (255, 0, 0), (self.x - 20 - self.camera_x, self.y - 25 - self.camera_y, self.width + 40, 10))
            pygame.draw.rect(game.screen, (0, 55, 255), (self.x - 20 - self.camera_x, self.y - 25 - self.camera_y, (self.width + 40) * self.health / self.max_health, 10))

        if self.shrinking == True:
            if show_hitbox == True:
                pygame.draw.rect(game.screen, (0,0,0), (self.shrink_hitbox[0], self.shrink_hitbox[1], self.shrink_hitbox[2], self.shrink_hitbox[3]), 1)
            if self.facing == "left":
                game.screen.blit(player_left_shrink_img, (self.x - self.camera_x, self.shrink_y - self.camera_y))

            if self.facing == "right":
                game.screen.blit(player_right_shrink_img, (self.x - self.camera_x, self.shrink_y - self.camera_y))

            pygame.draw.rect(game.screen, (255, 0, 0), (self.x - 10 - self.camera_x, self.y - 25 - self.camera_y, self.width + 5, 5))
            pygame.draw.rect(game.screen, (0, 55, 255), (self.x - 10 - self.camera_x, self.y - 25 - self.camera_y, (self.width + 5) * self.health / self.max_health, 5))


class Bow:

    def __init__(self, range, attack_speed):
        self.x = bratan.x
        self.y = bratan.y + 25
        self.range = range
        self.cooldown = 0
        self.attack_speed = attack_speed


class Arrow:

    def __init__(self, vel):
        self.bolts = [self]

        self.x = crossbow.x
        self.y = crossbow.y
        self.width = 15
        self.height = 10
        self.hitbox = [self.x, self.y, self.width, self.height]

        self.get_x = self.x
        self.get_y = self.y     #get correct y coordinate when shrinking
        self.get_width = self.width
        self.get_height = self.height

        self.shrink_x = self.x
        self.shrink_y = self.y + 30
        self.shrink_width = self.width - 9
        self.shrink_height = self.height - 5
        self.shrink_hitbox_follow = [self.shrink_x, self.shrink_y, self.shrink_width, self.shrink_height]
        self.shrink_hitbox_shoot = [self.shrink_x, self.shrink_y, self.shrink_width, self.shrink_height]

        self.grow_x = self.x
        self.grow_y = self.y
        self.grow_width = self.width
        self.grow_height = self.height
        #self.grow_hitbox_follow = [self.grow_x, self.grow_y + 2, self.grow_width, self.grow_height]
        self.grow_hitbox_shoot = [self.grow_x, self.grow_y + 2, self.grow_width, self.grow_height]

        self.vel = vel
        self.current_x = self.x
        self.get_size = bratan.shrinking    #get correct value when shrinking
        self.facing = bratan.facing
        self.direction = self.facing
        self.shot = False
        self.hit = False

    def shoot(self):
        if self.shot:
            '''shoot right'''
            if self.direction == "right":
                if self.get_x < (self.current_x + crossbow.range) + self.vel and self.hit == False:    #shoot left until distance travelled
                    self.get_x += self.vel
                    self.shrink_hitbox_shoot[0] = self.get_x
                    self.grow_hitbox_shoot[0] = self.get_x
                    for animal in animals:
                        check_hit(self, animal)

                else:
                    crossbow.cooldown = crossbow.attack_speed
                    if bratan.shrinking == False:
                        self.x = bratan.x + bratan.width * 0.4
                    if bratan.shrinking == True:
                        self.x = bratan.x + bratan.width * 0.025
                    self.get_x = self.x
                    self.current_x = self.x
                    self.bolts.remove(self)
                    self.shot = False
                    self.hit = False

            '''shoot left'''
            if self.direction == "left":
                if self.get_x > (self.current_x - crossbow.range) - self.vel and self.hit == False:    #shoot left until distance travelled
                    self.get_x -= self.vel
                    self.shrink_hitbox_shoot[0] = self.get_x
                    self.grow_hitbox_shoot[0] = self.get_x
                    for animal in animals:
                        check_hit(self, animal)

                else:
                    crossbow.cooldown = crossbow.attack_speed
                    self.x = bratan.x
                    self.get_x = self.x
                    self.current_x = self.x
                    self.bolts.remove(self)
                    self.shot = False
                    self.hit = False

    def shoot_cooldown(self):
        if crossbow.cooldown > 0:
            crossbow.cooldown -= 1

            if crossbow.cooldown == 0:
                self.bolts.append(self)

    def draw(self):
        for bolt in self.bolts:
            '''shooting'''
            if self.shot == True:
                '''normal size'''
                if self.get_size == False:
                    if show_hitbox == True:
                        pygame.draw.rect(game.screen, (0,0,0), (self.grow_hitbox_shoot[0] - bratan.camera_x, self.grow_hitbox_shoot[1] - bratan.camera_y, self.grow_hitbox_shoot[2], self.grow_hitbox_shoot[3]), 1)
                    if self.direction == "left":
                        game.screen.blit(bolt_left_img, (self.get_x - bratan.camera_x, self.get_y - bratan.camera_y))

                    if self.direction == "right":
                        game.screen.blit(bolt_right_img, (self.get_x - bratan.camera_x, self.get_y - bratan.camera_y))

                '''shrinking'''
                if self.get_size == True:
                    if show_hitbox == True:
                        pygame.draw.rect(game.screen, (0,0,0), (self.shrink_hitbox_shoot[0] - bratan.camera_x, self.shrink_hitbox_shoot[1], self.shrink_hitbox_shoot[2], self.shrink_hitbox_shoot[3]), 1)
                    if self.direction == "left":
                        game.screen.blit(bolt_left_shrink_img, (self.get_x - bratan.camera_x, self.get_y - bratan.camera_y))

                    if self.direction == "right":
                        game.screen.blit(bolt_right_shrink_img, (self.get_x - bratan.camera_x, self.get_y - bratan.camera_y))

            '''following'''
            if self.shot == False:
                '''normal size'''
                if bratan.shrinking == False:
                    if self.facing == "left":
                        game.screen.blit(bolt_left_img, (self.x - bratan.camera_x, self.y - bratan.camera_y))
                        #pygame.draw.rect(game.screen, (0,0,0), (self.grow_hitbox_follow[0], self.grow_hitbox_follow[1], self.grow_hitbox_follow[2], self.grow_hitbox_follow[3]), 1)

                    if self.facing == "right":
                        game.screen.blit(bolt_right_img, (self.x - bratan.camera_x, self.y - bratan.camera_y))
                        #pygame.draw.rect(game.screen, (0,0,0), (self.grow_hitbox_follow[0] + bratan.shrink_width, self.grow_hitbox_follow[1], self.grow_hitbox_follow[2], self.grow_hitbox_follow[3]), 1)

                '''shrinking'''
                if bratan.shrinking == True:
                    #pygame.draw.rect(game.screen, (0,0,0), (self.shrink_hitbox_follow[0], self.shrink_hitbox_follow[1], self.shrink_hitbox_follow[2], self.shrink_hitbox_follow[3]), 1)
                    if self.facing == "left":
                        game.screen.blit(bolt_left_shrink_img, (self.x - bratan.camera_x, self.y - bratan.camera_y))

                    if self.facing == "right":
                        game.screen.blit(bolt_right_shrink_img, (self.x - bratan.camera_x + 5, self.y - bratan.camera_y))


class Animal:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = random.randint(0, (game.width-self.width))   #spawn animal at random x coordinate
        self.y = game.ground-self.height    #align sprite to ground
        self.current_x = self.x
        self.hitbox = [self.x, self.y, self.width, self.height]
        self.path = 150    #set distance animal is travelling
        self.direction = random.randint(0, 2)   #set random direction animal is moving to
        self.facing = "left"    #determine whether facing right or eft
        self.wait = 0   #countdown for standing animal
        self.react = False
        animals.append(self)

    '''pause between each movement'''
    def move_cooldown(self):
        if self.wait < 100:     #countdown
            self.wait += 1
            self.hitbox[0] = self.x

        else:
            self.wait = 0   #reset countdown
            self.direction = random.randint(0, 2)   #new movement
            self.current_x = self.x     #reset travelling distance

    '''random passive movement unique for each Animal
        right == 0
        left == 1
        standing == 2
        cooldown == 3   '''
    def move(self):

        '''moving right when on left border of screen'''
        if self.x <= -925:
            self.direction = 0

        '''moving left when on righr border of screen'''
        if self.x >= 1875 - self.width:
            self.direction = 1

        if self.react == False:
            '''moving right'''
            if self.direction == 0:
                self.facing = "right"

                if self.x < (self.current_x + self.path) + self.vel:    #moving right until distance travelled
                    self.x += self.vel
                    self.hitbox[0] = self.x

                else:
                    self.move_cooldown()    #wait until next move

            '''moving left'''
            if self.direction == 1:
                self.facing = "left"

                if self.x > (self.current_x - self.path) - self.vel:    #moving left until distance travelled
                    self.x -= self.vel
                    self.hitbox[0] = self.x

                else:
                    self.move_cooldown()    #wait until next movement

            '''standing still'''
            if self.direction == 2:
                if self.wait < 250:     #countdown until next movement
                    self.wait += 1
                    self.hitbox[0] = self.x

                else:
                    self.wait = 0   #reset countdown
                    self.direction = random.randint(0, 2)   #new movement

        if self.react == True:
            self.hit_reaction()

    def check_death(self):
        if self.health <= 0:
            animals.remove(self)

    '''draw animal on screen'''
    def draw(self, other):
        if show_hitbox == True:
            pygame.draw.rect(game.screen, (0,0,0), (self.hitbox[0] - other.camera_x, self.hitbox[1] - other.camera_y, self.hitbox[2], self.hitbox[3]), 1)

        if self.facing == "left":
            game.screen.blit(self.left_img, (self.x - other.camera_x, self.y - other.camera_y))

        if self.facing == "right":
            game.screen.blit(self.right_img, (self.x - other.camera_x, self.y - other.camera_y))

        pygame.draw.rect(game.screen, (255, 0, 0), (self.x - other.camera_x, self.y - 25 - other.camera_y, self.width, 10))
        pygame.draw.rect(game.screen, (0, 225, 0), (self.x - other.camera_x, self.y - 25 - other.camera_y, self.width * self.health / self.max_health, 10))


class Platypus(Animal):

    width = 75
    height = 25
    spawn_timer = 700
    spawn_cooldown = 700

    def __init__(self, width, height):
        super().__init__(width, height)
        self.hitbox = [self.x, self.y + 4, self.width, self.height - 4]
        self.vel = 2
        self.max_health = 50
        self.health = self.max_health
        self.left_img = platypus_left_img
        self.right_img = platypus_right_img

    def hit_reaction(self):
        if self.react and -900 <= self.x <= 1850 - self.width:
            if self.x <= bratan.x:
                self.facing = "left"
                if self.x > (self.current_x - self.path * 5) - self.vel:    #moving left until distance travelled
                    self.x -= self.vel * 3.5
                    self.hitbox[0] = self.x

                else:
                    self.current_x = self.x
                    self.direction = random.randint(0, 2)   #new movement
                    self.react = False

            if self.x >= bratan.x:
                self.facing = "right"
                if self.x < (self.current_x + self.path * 5) + self.vel:    #moving right until distance travelled
                    self.x += self.vel * 3.5
                    self.hitbox[0] = self.x

                else:
                    self.current_x = self.x
                    self.direction = random.randint(0, 2)   #new movement
                    self.react = False

        else:
            self.direction = 2
            self.react = False


class Cow(Animal):

    width = 100
    height = 50
    spawn_timer = 1000
    spawn_cooldown = 1000

    def __init__(self, width, height):
        super().__init__(width, height)
        self.hitbox = [self.x, self.y, self.width, self.height]
        self.vel = 0.5
        self.max_health = 200
        self.health = self.max_health
        self.attack_cooldown = 100
        self.left_img = cow_left_img
        self.right_img = cow_right_img

    def hit_reaction(self):
        if self.react:
            if self.attack_cooldown < 100:
                self.attack_cooldown += 1

            if self.x + self.width * 0.5 >= bratan.x + bratan.width:
                self.facing = "left"
                self.x -= self.vel * 4
                self.hitbox[0] = self.x

            if bratan.x + bratan.width >= self.x + self.width * 0.5 >= bratan.x + bratan.width / 2 and bratan.y <= game.ground:
                if self.attack_cooldown == 100:
                    bratan.health -= 10
                    self.attack_cooldown = 0

            if self.x + self.width * 0.5 <= bratan.x:
                self.facing = "right"
                self.x += self.vel * 4
                self.hitbox[0] = self.x

            if bratan.x <= self.x + self.width * 0.5 <= bratan.x + bratan.width / 2 and bratan.y <= game.ground:
                if self.attack_cooldown == 100:
                    bratan.health -= 10
                    self.attack_cooldown = 0

            if bratan.health <= 0 or self.x <= bratan.x - 600 or self.x >= self.x + 600:
                self.react = False


'''define all entities'''
game = Window()
bratan = Player(450, 625, 25, 75, 3)
crossbow = Bow(350, 100)
bolt = Arrow(15)

species = [Platypus, Cow]

def spawn(self):
    if len(animals) <= 10:
        if self.spawn_cooldown == self.spawn_timer:
            entity = self(self.width, self.height)
            self.spawn_cooldown = 0

        else:
            self.spawn_cooldown += 1

def check_hit(self, other):
    if self.get_size == False and self.direction == "left":
        if other.hitbox[0] <= self.grow_hitbox_shoot[0] <= other.hitbox[0] + other.hitbox[2] and other.hitbox[1] <= self.grow_hitbox_shoot[1] + self.grow_hitbox_shoot[3] / 2 <= other.hitbox[1] + other.hitbox[3]:
            other.health -= 25
            other.react = True
            self.hit = True

    if self.get_size == False and self.direction == "right":
        if other.hitbox[0] <= self.grow_hitbox_shoot[0] + self.grow_hitbox_shoot[2] <= other.hitbox[0] + other.hitbox[2] and other.hitbox[1] <= self.grow_hitbox_shoot[1] + self.grow_hitbox_shoot[3] / 2 <= other.hitbox[1] + other.hitbox[3]:
            other.health -= 25
            other.react = True
            self.hit = True

    if self.get_size == True and self.direction == "left":
        if other.hitbox[0] <= self.shrink_hitbox_shoot[0] <= other.hitbox[0] + other.hitbox[2] and other.hitbox[1] <= self.shrink_hitbox_shoot[1] + self.shrink_hitbox_shoot[3] / 2 <= other.hitbox[1] + other.hitbox[3]:
            other.health -= 10
            other.react = True
            self.hit = True

    if self.get_size == True and self.direction == "right":
        if other.hitbox[0] <= self.shrink_hitbox_shoot[0] + self.shrink_hitbox_shoot[2] <= other.hitbox[0] + other.hitbox[2] and other.hitbox[1] <= self.shrink_hitbox_shoot[1] + self.shrink_hitbox_shoot[3] / 2 <= other.hitbox[1] + other.hitbox[3]:
            other.health -= 10
            other.react = True
            self.hit = True

World.create(World)

'''display all sprites'''
def redrawScreen():
    game.draw()
    for animal in animals:
        animal.draw(bratan)
    bratan.draw()
    bolt.draw()
    pygame.display.flip()

'''gameloop'''
while True:
    clock.tick(60)  #set fps

    '''check events'''
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            '''sneaking'''
            if event.key == pygame.K_e:
                bratan.shrink()

            if event.key == pygame.K_h:
                if show_hitbox == True:
                    show_hitbox = False

                else:
                    show_hitbox = True

            '''shoot'''
            if event.key == pygame.K_SPACE:
                if crossbow.cooldown == 0 and bolt.shot == False:
                    bolt.current_x = bolt.x
                    bolt.get_y = bolt.y
                    bolt.get_size = bratan.shrinking
                    '''idfk why but it works'''
                    if bratan.shrinking == True:
                        if bratan.facing == "left":
                            bolt.get_x = bolt.x
                        if bratan.facing == "right":
                            bolt.get_x = bolt.x + 4
                        bolt.shrink_hitbox_shoot[1] = bolt.get_y

                    if bratan.shrinking == False:
                        bolt.get_x = bolt.x
                        bolt.grow_hitbox_shoot[1] = bolt.get_y + 2

                    bolt.direction = bratan.facing
                    bolt.shot = True
                    bolt.shoot()

        '''quit game'''
        if event.type == pygame.QUIT:
            pygame.quit()

    '''execute all actions'''
    for specie in species:
        spawn(specie)
    bolt.shoot()
    bolt.shoot_cooldown()
    bratan.move()
    bratan.check_death()
    for animal in animals:
        animal.move()
        animal.check_death()

    redrawScreen()
