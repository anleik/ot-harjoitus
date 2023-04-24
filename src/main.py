import sqlite3
import pygame

pygame.init()

# SQLite Database
def sql_database():
    conn = sqlite3.connect("data.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS Data
                (XCOORD            BLOB NOT NULL,
                YCOORD             BLOB NOT NULL
                );''')
def save_progress(xcoord, ycoord):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Data")
    parameters  = (xcoord, ycoord)
    cursor.execute("INSERT INTO Data VALUES (?,?)", parameters)
    conn.commit()
    conn.close()
def progress_retrieve():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Data")
    retrieve_data = cursor.fetchall()
    conn.close()
    return retrieve_data

sql_database()

# Display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
pygame.display.set_caption('Test game')

# Color
background_color = (135, 206, 235)
ground_color = (140, 70, 20)
platform_color = (200, 70, 50)
player_color = (255, 0, 0)
obj_color = (135, 170, 235)
obj_color2 = (135, 135, 255)
obstacle_color = (0, 0, 0)
text_color = (240, 240, 240)

# Text
font = pygame.font.SysFont("IMPACT", 34)
DISTANCE = 0
def draw_texts():
    distance_text = font.render(f"{round(DISTANCE, 2)}", True, text_color)
    m_text = font.render("m", True, text_color)
    screen.blit(distance_text, (690, 10))
    screen.blit(m_text, (765, 10))

# Background objects
class BackgroundObject:
    def __init__(self, obj_x=0, obj_y=0, obj_w=0, obj_h=0, color=(255, 255, 255), par = 1):
        self.rect = pygame.Rect(obj_x, obj_y, obj_w, obj_h)
        self.color = color
        self.par = par

BACKGROUND_OFFSET = 0
PARALLAX_FACTOR = 0.5

#  Player
player_rect = pygame.Rect(100, 500, 30, 40)

# Ground Objects
class GroundObject:
    def __init__(self, grx= 0, gry = 0, grw = 0, grh = 0, color = ground_color):
        self.grx = grx
        self.gry = gry
        self.grw = grw
        self.grh = grh
        self.rect = pygame.Rect(grx, gry, grw, grh)
        self.color = color

# Platforms
class Platform:
    def __init__(self, plx= 0, ply = 0, plw = 0, plh = 0, color = platform_color, par = 1):
        self.plx = plx
        self.ply = ply
        self.plw = plw
        self.plh = plh
        self.rect = pygame.Rect(plx, ply, plw, plh)
        self.color = color
        self.par = par

# Obstacles
class Obstacle:
    def __init__(self, obx = 0, oby = 0, obw = 0, obh = 0, color = obstacle_color):
        self.obx = obx
        self.oby = oby
        self.obw = obw
        self.obh = obh
        self.rect = pygame.Rect(obx, oby, obw, obh)
        self.color = color


# Camera scroll
camera_offset = -player_rect.x + SCREEN_WIDTH // 2

# Speed and Gravity
PLAYER_SPEED = 5
GRAVITY = 1.70
PLAYER_VELOCITY_Y = 0
PLAYER_VELOCITY_X = 0
ACCELERATION = 0.5
DECELERATION = 0.8
MAX_SPEED = 7.5

# Jumping
IS_JUMPING = False
JUMP_HEIGHT = 12

KEY_UP_PRESSED = False
JUMP_KEY_TIME = 0
MAX_JUMP_TIME = 0.5
JUMP_COUNTER = 0
MAX_JUMP_COUNTER = 15

groundobjects = []
backgroundobjects = []
platforms = []
obstacles = []

def initialize():
    global groundobjects, backgroundobjects, platforms, obstacles, player_rect, DISTANCE, PLAYER_VELOCITY_X, BACKGROUND_OFFSET
    groundobjects = []
    groundobjects.append(GroundObject(10, 550, 2000, 40, ground_color))
    groundobjects.append(GroundObject(2210, 550, 1000, 40, ground_color))
    groundobjects.append(GroundObject(3450, 550, 100, 40, ground_color))
    groundobjects.append(GroundObject(3790, 550, 100, 40, ground_color))
    groundobjects.append(GroundObject(4130, 550, 100, 40, ground_color))
    groundobjects.append(GroundObject(4470, 550, 1500, 40, ground_color))

    backgroundobjects = []
    backgroundobjects.append(BackgroundObject(1000, 260, 300, 100, obj_color2, 0.9))
    backgroundobjects.append(BackgroundObject(200, 70, 300, 100, obj_color, 0.5))
    backgroundobjects.append(BackgroundObject(600, 40, 400, 200, obj_color, 0.3))
    backgroundobjects.append(BackgroundObject(1400, 150, 300, 200, obj_color2, 0.8))
    backgroundobjects.append(BackgroundObject(1500, 40, 400, 200, obj_color, 0.3))

    platforms = []
    platforms.append(Platform(400, 400, 100, 20, platform_color))
    platforms.append(Platform(600, 300, 150, 20, platform_color, 0.5))
    platforms.append(Platform(850, 200, 100, 20, platform_color))
    platforms.append(Platform(1240, 200, 100, 20, platform_color))
    platforms.append(Platform(1570, 200, 200, 20, platform_color))
    platforms.append(Platform(2290, 420, 300, 20, platform_color))

    obstacles = []
    obstacles.append(Obstacle(540, 360, 60, 150, obstacle_color))
    obstacles.append(Obstacle(775, 250, 50, 50, obstacle_color))
    obstacles.append(Obstacle(1000, 250, 100, 600, obstacle_color))
    obstacles.append(Obstacle(1400, 100, 100, 100))

    player_rect = pygame.Rect(100, 500, 30, 40)
    DISTANCE = 0
    PLAYER_VELOCITY_X = 0
    BACKGROUND_OFFSET = 0

initialize()

# Respawn
def respawncheck():
    if player_rect.y > 900:
        initialize()
    if player_rect.collidelist(obstacles) >= 0:
        initialize()

clock = pygame.time.Clock()

saved_progress = progress_retrieve()
print(saved_progress)
if saved_progress != []:
    player_rect.x, player_rect.y = saved_progress[0][0], saved_progress[0][1]
    BACKGROUND_OFFSET -= player_rect.x

# Gameloop
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    # Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        save_progress(player_rect.x, player_rect.y)
        RUNNING = False
    if keys[pygame.K_UP] and not IS_JUMPING:
        PLAYER_VELOCITY_Y = -JUMP_HEIGHT
        IS_JUMPING = True
    if keys[pygame.K_LEFT]:
        PLAYER_VELOCITY_X -= ACCELERATION
        PLAYER_VELOCITY_X = max(PLAYER_VELOCITY_X, -MAX_SPEED)
    elif keys[pygame.K_RIGHT]:
        PLAYER_VELOCITY_X += ACCELERATION
        PLAYER_VELOCITY_X = min(PLAYER_VELOCITY_X, MAX_SPEED)
    else:
        PLAYER_VELOCITY_X *= DECELERATION
        if abs(PLAYER_VELOCITY_X) < 0.1:
            PLAYER_VELOCITY_X = 0


    # Gravity and speed
    PLAYER_VELOCITY_Y += GRAVITY
    player_rect.y += PLAYER_VELOCITY_Y
    player_rect.x += PLAYER_VELOCITY_X

    # Ground Collisions
    if player_rect.collidelist(groundobjects) >= 0:
        player_rect.y = int(
            groundobjects[player_rect.collidelist(groundobjects)].gry - player_rect.height)
        IS_JUMPING = False
        PLAYER_VELOCITY_Y = 0
        JUMP_COUNTER = 0
    else:
        # High jump
        if keys[pygame.K_UP] and IS_JUMPING and JUMP_COUNTER < MAX_JUMP_COUNTER:
            PLAYER_VELOCITY_Y = -JUMP_HEIGHT
            JUMP_COUNTER += 1
        else:
            IS_JUMPING = True
            JUMP_COUNTER = MAX_JUMP_COUNTER

    # Platform Collisions
    for platform in platforms:
        if player_rect.colliderect(platform):
            if PLAYER_VELOCITY_Y > 0:  # Above collision
                player_rect.y = platform.ply - player_rect.height
                IS_JUMPING = False
                PLAYER_VELOCITY_Y = 0
                JUMP_COUNTER = 0
            elif PLAYER_VELOCITY_Y < 0:  # Below collision
                player_rect.y = platform.ply + platform.plh
                PLAYER_VELOCITY_Y = 0

    # Background offset
    BACKGROUND_OFFSET -= PLAYER_VELOCITY_X
    DISTANCE = (player_rect.x - 100) / 100
    camera_offset = -player_rect.x + SCREEN_WIDTH // 2

    # Respawn
    respawncheck()

    # Draw + camera offset
    screen.fill(background_color)
    for obj in backgroundobjects:
        pygame.draw.rect(screen, obj.color, obj.rect.move(
            (int(BACKGROUND_OFFSET * obj.par)), 0))
    for obj in groundobjects:
        pygame.draw.rect(screen, obj.color, obj.rect.move(camera_offset, 0))
    for obj in obstacles:
        pygame.draw.rect(screen, obj.color, obj.rect.move(camera_offset, 0))
    pygame.draw.rect(screen, player_color, player_rect.move(camera_offset, 0))
    for obj in platforms:
        pygame.draw.rect(screen, obj.color, obj.rect.move(int(camera_offset) ,0))

    draw_texts()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
