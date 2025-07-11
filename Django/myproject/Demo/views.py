from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home_view(request):
    name="Rajesh"
    return render(request, 'WelcomeApp/home.html',{'name':name})
def about_view(request):
    return render(request, 'WelcomeApp/about.html')
def contact_view(request):
    name=request.GET.get('name')
    return render(request, 'WelcomeApp/home.html',{'name':name})
def name_view(request,name):
    return render(request, 'WelcomeApp/home.html',{'name':name})
def http_resp(request):
    return HttpResponse('<html><body><h1>Welcome Back</h1></body></html>')
def json_data(request):
    data={'name': 'Rajesh'}
    return JsonResponse(data)