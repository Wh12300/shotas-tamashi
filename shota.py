import pygame
import random
import time

pygame.init()

pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("aicile romasgan nasroli napaleonebi")

background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (800, 600))

new_background = pygame.image.load("bck.jpg")
new_background = pygame.transform.scale(new_background, (800, 600))

cart_images = ["cart.png", "new_cart.jpg"]
cart_index = 0

cart_image = pygame.image.load(cart_images[cart_index])
cart_x = 370
cart_y = 400
cart_x_change = 0

object_image = pygame.image.load("object.png")
object_x = random.randint(0, 736)
object_y = 0
object_y_change = 0.5

score = 0

font = pygame.font.Font(None, 36)
text_x, text_y = 10, 10

last_collision_time = 0
collision_delay = 1
reset_object = False
game_over = False

def cart(x, y):
    screen.blit(cart_image, (x, y))

def object(x, y):
    screen.blit(object_image, (x, y))

def is_collision(cart_x, cart_y, object_x, object_y):
    cart_width = 64
    cart_height = 64
    object_width = 64
    object_height = 64

    if (cart_x + cart_width >= object_x and cart_x <= object_x + object_width and
        cart_y + cart_height >= object_y and cart_y <= object_y + object_height):
        return True
    return False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cart_x_change = -4
                if event.key == pygame.K_RIGHT:
                    cart_x_change = 4

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    cart_x_change = 0

    if not game_over:
        cart_x += cart_x_change
        if cart_x < 0:
            cart_x = 0
        elif cart_x > 736:
            cart_x = 736

        object_y += object_y_change
        if object_y > 600:
            if reset_object:
                object_x = random.randint(0, 736)
                object_y = 0
            else:
                reset_object = True

        if is_collision(cart_x, cart_y, object_x, object_y):
            if time.time() - last_collision_time >= collision_delay:
                score += 1
                last_collision_time = time.time()
                reset_object = True

    screen.blit(background, (0, 0))

    if score >= 10:
        screen.blit(new_background, (0, 0))
        cart_image = pygame.Surface((64, 64))
        cart_image.set_colorkey((0, 0, 0))
        object_image = pygame.Surface((64, 64))
        object_image.set_colorkey((0, 0, 0))
        text = font.render("", True, (255, 255, 255))
        game_over = True

    if not game_over:
        cart(cart_x, cart_y)
        object(object_x, object_y)
        text = font.render(f"Score: {score}", True, (255, 255, 255))

    screen.blit(text, (text_x, text_y))

    pygame.display.update()

pygame.quit()
