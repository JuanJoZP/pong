# CONSTANT VARIABLES
WINDOWWIDTH = 960
WINDOWHEIGHT = 540
SIZE = (WINDOWWIDTH, WINDOWHEIGHT)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
PADDLE_XSPACING = 10

# GAME VARIABLES
PAUSE_TIME = 1.5  # pause seconds at the start and between points
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
settings = {
    "PADDLE_VELOCITY": 5,  # 5 to 10
    "BALL_VELOCITY": 7,  # ball velocity from 5 to 15
}
DIRECTION_MULTIPLIER = 2  # multiplier for the ball direction in the y-axis
DIRECTION_MAX = 4  # should be greater than multiplier and divisible by the multiplier
