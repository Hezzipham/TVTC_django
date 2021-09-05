from django.shortcuts import render, HttpResponse

# Create your views here.
def game(request):
    # with open('game.txt', 'r') as data:
    #     games = data.read().split('\n')
    #     g_list = [game.split(", ") for game in games]
    #     g_num = len(g_list)
    return render(request, "game/in.html")