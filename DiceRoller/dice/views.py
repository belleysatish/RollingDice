# dice/views.py
from django.http import JsonResponse
import random

def roll_dice(request):
    """API view to roll the dice and return a random value between 1 and 6."""
    dice_value = random.randint(1, 6)
    return JsonResponse({'dice_value': dice_value})


from django.shortcuts import render

def index(request):
    """View to display the dice roll page."""
    return render(request, 'dice/index.html')
