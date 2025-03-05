from django.shortcuts import render

# game/templates/multiends
def index(request):
    return render(request, "web.html")