import pygame
pygame.init()

# Display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.SRCALPHA)
pygame.display.set_caption('Test game')

# Color
background_color = (135, 206, 235)
ground_color = (140, 70, 20)
player_color = (255, 0, 0)
object_color = (135, 170, 235)


#Background objects
class BackgroundObject:
    def __init__(self, x=0, y=0, w=0, h=0, p=0, c=(255, 255, 255)):
        self.rect = pygame.Rect(x, y, w, h)
        self.p = p #parallax
        self.c = c

backgroundobjects = []

test = BackgroundObject(600, 40, 400, 200, 0.3, object_color)
test2 = BackgroundObject(100, 70, 300, 100, 0.5, object_color)
test3 = BackgroundObject(1000, 260, 300, 100, 0.9, (135, 135, 255))
    
backgroundobjects.append(test)
backgroundobjects.append(test2)
backgroundobjects.append(test3)


background_offset = 0
parallax_factor = 0.5



#  Player and ground objects
player_rect = pygame.Rect(100, 500, 30, 50)
ground_rect = pygame.Rect(10, 550, 2000, 40)

#Platforms
platforms = [
    pygame.Rect(400, 400, 100, 20),
    pygame.Rect(600, 300, 150, 20),
    pygame.Rect(850, 200, 100, 20),
    pygame.Rect(1240, 200, 100, 20),
]

# Camera scroll
camera_offset = -player_rect.x + screen_width // 2

# Speed and gravity
player_speed = 5
gravity = 1.75
player_velocity_y = 0
player_velocity_x = 0
acceleration = 0.5
deceleration = 0.8
max_speed = 7

# Jumping
is_jumping = False 
jump_height = 12

key_up_pressed = False
jump_key_time = 0
max_jump_time = 0.5
jump_counter = 0
max_jump_counter = 15

clock = pygame.time.Clock()



# Gameloop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and not is_jumping:
        player_velocity_y = -jump_height
        is_jumping = True
    if keys[pygame.K_LEFT]:
        player_velocity_x -= acceleration
        player_velocity_x = max(player_velocity_x, -max_speed)
    elif keys[pygame.K_RIGHT]:
        player_velocity_x += acceleration
        player_velocity_x = min(player_velocity_x, max_speed)
    else:
        player_velocity_x *= deceleration
        if abs(player_velocity_x) < 0.1:
            player_velocity_x = 0
    

    # Gravity and speed
    player_velocity_y += gravity
    player_rect.y += player_velocity_y
    player_rect.x += player_velocity_x

    # Collisions
    if player_rect.colliderect(ground_rect):
        player_rect.y = ground_rect.y - player_rect.height
        is_jumping = False
        player_velocity_y = 0
        jump_counter = 0
    else:
        # High jump
        if keys[pygame.K_UP] and is_jumping and jump_counter < max_jump_counter:
            player_velocity_y = -jump_height
            jump_counter += 1
        else:
            is_jumping = True
            jump_counter = max_jump_counter

    # Collisions
    on_ground_or_platform = player_rect.colliderect(ground_rect)
    for platform in platforms:
        if player_rect.colliderect(platform):
            if player_velocity_y > 0:  # Above collision
                player_rect.y = platform.y - player_rect.height
                is_jumping = False
                player_velocity_y = 0
                jump_counter = 0
            elif player_velocity_y < 0:  # Below collision
                player_rect.y = platform.y + platform.height
                player_velocity_y = 0

    if on_ground_or_platform:
        is_jumping = False
        player_velocity_y = 0
        jump_counter = 0 

    
    
    #Background offset
    background_offset -= player_velocity_x
    camera_offset = -player_rect.x + screen_width // 2
    
 
    # Draw + camera offset
    screen.fill(background_color)
    for obj in backgroundobjects:
        pygame.draw.rect(screen, obj.c, obj.rect.move((int(background_offset * obj.p)), 0))
    pygame.draw.rect(screen, ground_color, ground_rect.move(camera_offset, 0))
    pygame.draw.rect(screen, player_color, player_rect.move(camera_offset, 0))
    for platform in platforms:
        pygame.draw.rect(screen, ground_color, platform.move(camera_offset, 0))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()