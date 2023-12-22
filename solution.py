import pygame

pygame.init()

# Game constants.
WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100

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

def draw(win, paddles):
    """

    :param win: Game window.
    :param paddles: Game paddles.
    """
    win.fill(BLACK)

    for paddle in paddles:
        paddle.draw(win)

    # Pygame must be updated to display any changes.
    pygame.display.update()


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

    # Main game loop.
    while run:
        # Prevent the game from running more frames per second than the FPS value. In this case, 60 FPS.
        # That is, the while loop will run a maximum of 60 times per second.
        clock.tick(FPS)

        # Draw on the game window.
        draw(WIN, [left_paddle, right_paddle])

        # Retrieve all events; e.g., clicking mouse/keyboard, closing window...
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break


        # Handle paddle movement.
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

    pygame.quit()


if __name__ == '__main__':
    main()
