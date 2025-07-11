from django.shortcuts import render
from django.http import JsonResponse

def home_view(request):
    name = request.GET.get('name', 'Guest')
    return render(request, 'WelcomeApp/greeting.html', {'name': name})


def greet_user(request, username):
    return render(request, 'WelcomeApp/greeting.html', {'name': username})


def api_greet(request, username):
    return JsonResponse({'message': f'Hello, {username}! Welcome to the API.'})
