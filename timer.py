from turtle import Turtle

class TimeBoard(Turtle):
    def __init__(self, screen, game_over):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.game_over = game_over
        self.screen = screen
        self.time = 600
        self.print_time_score()


    def print_time_score(self):
        self.clear()
        self.goto(-300, 300)
        minutes = self.time // 60
        seconds = self.time % 60
        self.write(arg=f"TIME LEFT: {minutes:02d}:{seconds:02d}", move=False, align="center", font=("Arial", 15, "bold"))

        if self.time > 0 and self.game_over == False:
            self.time -= 1
            self.screen.ontimer(self.print_time_score, 1000)
        else:
            self.game_over = True
