import pygame

pygame.init()

# Game constants.
WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 7

# Colours.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set the window caption.
pygame.display.set_caption("Pong")


class Paddle:
    COLOR = WHITE
    VELOCITY = 4

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VELOCITY
        else:
            self.y += self.VELOCITY


class Ball:
    MAX_VEL = 5
    COLOUR = WHITE

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.COLOUR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel


def draw(win, paddles, ball):
    """

    :param win: Game window.
    :param paddles: Game paddles.
    """
    win.fill(BLACK)

    for paddle in paddles:
        paddle.draw(win)

    # Draw dotted line down the middle. Implement as 20 rectangles on the screen but only select every other rectangle.
    draw_centre_line(win)

    ball.draw(win)
    # Pygame must be updated to display any changes.
    pygame.display.update()


def draw_centre_line(win):
    for i in range(10, HEIGHT, HEIGHT // 20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH // 2 - 3, i, 6, HEIGHT // 20))


def handle_collision(ball, left_paddle, right_paddle):
    # Handle collision with floor and ceiling.
    if (ball.y + ball.radius >= HEIGHT) or (ball.y - ball.radius <= 0):
        ball.y_vel *= -1

    # Check left paddle.
    if ball.x_vel < 0:
        # If the ball's y value is within the height range of the paddle.
        if left_paddle.y <= ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1

                # Calculate velocity in y direction after collision.
                middle_y = left_paddle.y + left_paddle.height / 2
                y_difference = ball.y - middle_y

                # The reduction factor is used to modulate the y velocity after collision.
                # The closer the ball is to the paddle centre when it strikes the paddle, the lower the y-velocity will be.
                # This adds greater variation to the game.
                reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL

                # The reduction factor ensures the y_velocity will be between -5 and 5.
                ball.y_vel = y_difference / reduction_factor


    # Right paddle.
    else:
        if right_paddle.y <= ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1

                # Calculate velocity in y direction after collision.
                middle_y = right_paddle.y + right_paddle.height / 2
                y_difference = ball.y - middle_y

                # The reduction factor is used to modulate the y velocity after collision.
                # The closer the ball is to the paddle centre when it strikes the paddle, the lower the y-velocity will be.
                # This adds greater variation to the game.
                reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL

                # The reduction factor ensures the y_velocity will be between -5 and 5.
                ball.y_vel = y_difference / reduction_factor


def handle_paddle_movement(keys, left_paddle, right_paddle):
    # If w key is pressed, move up. If s key pressed, move down.
    # Also ensure that paddles cannot move off the screen.
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VELOCITY >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VELOCITY <= HEIGHT - PADDLE_HEIGHT:
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VELOCITY >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VELOCITY <= HEIGHT - PADDLE_HEIGHT:
        right_paddle.move(up=False)


def main():
    run = True

    # Regulate the game speed.
    clock = pygame.time.Clock()

    # Create the two paddles.
    left_paddle = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

    # Main game loop.
    while run:
        # Prevent the game from running more frames per second than the FPS value. In this case, 60 FPS.
        # That is, the while loop will run a maximum of 60 times per second.
        clock.tick(FPS)

        # Draw on the game window.
        draw(WIN, [left_paddle, right_paddle], ball)

        # Retrieve all events; e.g., clicking mouse/keyboard, closing window...
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # Handle paddle movement.
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

        # Ball movement.
        ball.move()
        handle_collision(ball, left_paddle, right_paddle)
    pygame.quit()


if __name__ == '__main__':
    main()
