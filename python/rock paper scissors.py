import random
pygame.init()

class Button:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def clicked(self):
        pos = pygame.mouse.get_pos()
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True
        return False


class RpsGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((960, 640))
        pygame.display.set_caption("RPS Smasher")

        self.bg = pygame.image.load("background.jpg")
        self.r_btn_img = pygame.image.load("r_button.png").convert_alpha()
        self.p_btn_img = pygame.image.load("p_button.png").convert_alpha()
        self.s_btn_img = pygame.image.load("s_button.png").convert_alpha()

        self.rock_img = pygame.image.load("rock.png").convert_alpha()
        self.paper_img = pygame.image.load("paper.png").convert_alpha()
        self.scissors_img = pygame.image.load("scissors.png").convert_alpha()

        self.rock_btn = Button(20, 500, 300, 140)
        self.paper_btn = Button(330, 500, 300, 140)
        self.scissors_btn = Button(640, 500, 300, 140)

        self.font = pygame.font.Font(None, 80)
        self.text = self.font.render("0 : 0", True, (255, 255, 255))

        self.pl_score = 0
        self.pc_score = 0
        self.p_option = ""
        self.pc_option = ""

    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.r_btn_img, (20, 500))
        self.screen.blit(self.p_btn_img, (330, 500))
        self.screen.blit(self.s_btn_img, (640, 500))
        self.screen.blit(self.text, (380, 20))

    def player(self):
        if self.rock_btn.clicked():
            self.p_option = "rock"
            self.screen.blit(self.rock_img, (120, 200))
        elif self.paper_btn.clicked():
            self.p_option = "paper"
            self.screen.blit(self.paper_img, (120, 200))
        elif self.scissors_btn.clicked():
            self.p_option = "scissors"
            self.screen.blit(self.scissors_img, (120, 200))

    def computer(self):
        self.pc_option = random.choice(["rock", "paper", "scissors"])
        if self.pc_option == "rock":
            self.screen.blit(self.rock_img, (600, 200))
        elif self.pc_option == "paper":
            self.screen.blit(self.paper_img, (600, 200))
        else:
            self.screen.blit(self.scissors_img, (600, 200))

    def score(self):
        if self.p_option == self.pc_option:
            return
        if (self.p_option == "rock" and self.pc_option == "scissors") or \
           (self.p_option == "paper" and self.pc_option == "rock") or \
           (self.p_option == "scissors" and self.pc_option == "paper"):
            self.pl_score += 1
        else:
            self.pc_score += 1

        self.text = self.font.render(f"{self.pl_score} : {self.pc_score}", True, (255, 255, 255))

    def game_loop(self):
        clock = pygame.time.Clock()
        run = True

        while run:
            self.draw()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rock_btn.clicked() or self.paper_btn.clicked() or self.scissors_btn.clicked():
                        self.draw()
                        self.player()
                        self.computer()
                        self.score()
                        pygame.display.update()

            clock.tick(30)

        pygame.quit()


if __name__ == "__main__":
    game = RpsGame()
    game.game_loop()
