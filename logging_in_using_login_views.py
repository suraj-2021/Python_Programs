from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views import View

class LoginView(View):
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse("Logged in successfully")
        else:
            return HttpResponse("Invalid username or password")
