class Scoreboard:
    def __init__(self) -> None:
        self.score = 0

    def gain_point(self):
        self.score += 1

    def print_score(self):
        print(f"You scored 1 point! You are now on {self.score} point(s)")

    def print_final_score(self):
        print(f"You died. You finished on {self.score} point(s)!")