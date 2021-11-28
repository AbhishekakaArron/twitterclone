from django.shortcuts import redirect, render,HttpResponse
from .models import Tweet
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def get_all_tweets(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    tweet_list = [{'id': t.id,
                    'content': t.content,
                    'author': t.author} for t in tweets]
    context = {'tweet_list':tweet_list}
    return render(request, "twitterhome/globalfeed.html", context )


@login_required(login_url='/login')
def my_tweets(request):
    tweets = Tweet.objects.filter(author=request.user).order_by('-created_at')
    tweet_list = [{'id': t.id,
                    'content': t.content,
                    'author': t.author} for t in tweets]
    context = {'tweet_list':tweet_list}
    return render(request, "twitterhome/myTweets.html", context )


@login_required(login_url='/login')
def posttweet(request):
    if request.method == 'POST':
        x = request.POST['tweet']
        new_tweet = Tweet(author=request.user,content = x)
        new_tweet.save()
        return render(request,'twitterhome/wall.html')
    return render(request, 'twitterhome/wall.html') 


@login_required(login_url='/login')
def profileview(request, name):
    user = User.objects.get(username=name)
    tweets = Tweet.objects.filter(author = user)
    tweet_list = [{'id': t.id,
                    'content': t.content,
                    'author': t.author} for t in tweets]
    context = {'tweet_list':tweet_list, 'name':name}
    return render(request,'user/profile.html', context)


@login_required(login_url='/login')
def user_profile_view(request):
    user = User.objects.get(username=request.user)
    tweets = Tweet.objects.filter(author = user)
    tweet_list = [{'id': t.id,
                    'content': t.content,
                    'author': t.author} for t in tweets]
    context = {'tweet_list':tweet_list}
    return render(request,'user/userprofile.html', context)