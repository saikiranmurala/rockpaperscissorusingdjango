from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random
from .models import GameResult

def index(request):
    return render(request, 'game/index.html')

def load_game(request):
    return render(request, 'game/load.html')

@csrf_exempt
def play(request):
    if request.method == 'POST':
        user_move = request.POST.get('user_move')
        choices = ['rock', 'paper', 'scissor']
        computer_move = random.choice(choices)

        # Determine winner
        winner = get_winner(user_move, computer_move)

        # Save result
        GameResult.objects.create(
            player_move=user_move,
            computer_move=computer_move,
            winner=winner
        )

        return JsonResponse({
            'computer_move': computer_move,
            'winner': winner
        })

def get_winner(user, computer):
    if user == computer:
        return "draw"
    if (
        (user == "rock" and computer == "scissor") or
        (user == "scissor" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        return "user"
    return "computer"
