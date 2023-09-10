class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.score = 0
        with open('files/highscore') as f:
            high_score = f.readline()
        self.high_score = int(high_score)

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
