from django.shortcuts import render, redirect,HttpResponse
from .forms import tweetform, UserRegistrationForm, UserLoginForm
from .models import tweet
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required #django decoretors in whatch python series
from django.contrib.auth import login , logout,authenticate
# Create your views here.

def index (request):
    return render(request,'index.html')


def tweet_list (request):
    tweets=tweet.objects.all().order_by('-create_at')

    return render(request,'tweet_list.html',{'tweets':tweets})

@login_required
def tweet_create(request):
    if not request.user.is_authenticated:
        return redirect("login_user")
    if request.method == "POST":
        form = tweetform(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit = False) #becouse we want to the save user as well # as of now not save to database thet we use commit
            tweet.user = request.user # user getting in request 
            tweet.save()
            return redirect('tweet_list')
    else:
        form = tweetform()
        return render(request,'tweet_form.html', {'form':form })
    
@login_required
def tweet_edit(request, tweet_id):
    Tweet = get_object_or_404(tweet,pk=tweet_id, user = request.user)  #tweet give in the model #user if log in then give to the edit opetions

    if request.method == "POST":
        form = tweetform(request.POST, request.FILES, instance = Tweet)
        if form.is_valid():
            Tweet = form.save(commit=False) #commit false becouse we can to add user
            Tweet.user = request.user
            Tweet.save()
            return redirect('tweet_list')
    else:
        form = tweetform(instance=Tweet)
        return render(request,'tweet_form.html', {'form':form })


    
@login_required
def tweet_delete(request ,tweet_id):
    tweets = get_object_or_404(tweet,pk=tweet_id , user = request.user)
    if request.method == 'POST':
        tweets.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confirm_delete.html',{'tweets': tweets})

def Register(request):

    if  request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) #read clean data in jango
            user.set_password(form.cleaned_data['password1']) #django in buldi method set_password
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form =UserRegistrationForm()
        context={
            "form": form
        }
        return render (request, 'Registration/registration.html', context)


def login_user (request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect("tweet_list")  
        else:
            return HttpResponse("User Deatil Not Found") 
        
    else:
        form = UserLoginForm()
        return render(request,'Registration\login.html',{"form": form})


def User_logout(request):
    logout(request)
    return redirect("login_user")