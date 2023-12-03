from django.shortcuts import get_object_or_404, render , redirect 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login 

from accounts.models import UserProfile
from django.contrib.auth.models import User


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password1']
            
            user = User.objects.create_user(username = username, email = email, password = password)
            user.save()
            userprofile = UserProfile.objects.get_or_create(user = user, name = user.username, email = user.email)
            login(request, user)
            return redirect('shop:item_list')

    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request , 'registration/signup.html' , context)



