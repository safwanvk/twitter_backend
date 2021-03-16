from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from rest_framework.response import Response

# Create your views here.
def login_view(request, *args, **kwargs):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user_ = form.get_user()
        login(request, user_)
        return Response({'msg': 'Success'}, status=200)
    
    return Response({'msg': 'Invalid Username'}, status=400)

def logout_view(request, *args, **kwargs):
    if request.method == "POST":
        logout(request)
        return Response({'msg': 'Success'}, status=200)
    
    return Response({'msg': 'Server Error'}, status=500)