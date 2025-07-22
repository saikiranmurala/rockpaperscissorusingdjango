from django.db import models

class GameResult(models.Model):
    player_move = models.CharField(max_length=10)
    computer_move = models.CharField(max_length=10)
    winner = models.CharField(max_length=10)
    played_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player_move} vs {self.computer_move} - Winner: {self.winner}"

