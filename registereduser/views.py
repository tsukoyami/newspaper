
from django.http import JsonResponse
from django.shortcuts import redirect, render

from source.models import Source
from .models import RegisteredUser
from .serializers import RegistereduserSerialiser
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .forms import SignUpForm, LoginForm


@csrf_exempt
@api_view(['GET', 'POST'])
def registereduser(request):
    if request.method == 'GET':
        sources = RegisteredUser.objects.all()
        serializer = RegistereduserSerialiser(sources, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        serializer = RegistereduserSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt    
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['logged_in_user'] = user.id
            return redirect('source')
        else:
            return render(request, 'registereduser/signup.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = SignUpForm()
    return render(request, 'registereduser/signup.html', {'form': form})

@csrf_exempt 
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = RegisteredUser.objects.get(username=username, password=password)
                if user:
                    request.session['logged_in_user'] = user.id
                    sources = Source.objects.filter(source_user=user)
                    if sources.exists():
                        return redirect('story')
                    else:
                        return redirect('source')
            except RegisteredUser.DoesNotExist:
                return render(request, 'registereduser/login.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = LoginForm()
    return render(request, 'registereduser/login.html', {'form': form})

@csrf_exempt
def logout(request):
    if 'logged_in_user' in request.session:
        del request.session['logged_in_user']
    return redirect('login')
