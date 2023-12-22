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

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

def draw(win, paddles):
    """

    :param win: Game window.
    :param paddles: Game paddles.
    """
    win.fill(BLACK)

    # TODO: draw paddles.

    # Pygame must be updated to display any changes.
    pygame.display.update()


def main():
    run = True

    # Regulate the game speed.
    clock = pygame.time.Clock()

    # Create the two paddles.
    left_paddle = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(PADDLE_WIDTH - 10, HEIGHT // 2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

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

    pygame.quit()


if __name__ == '__main__':
    main()
