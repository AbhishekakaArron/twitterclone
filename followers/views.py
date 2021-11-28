from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Follower
from django.contrib.auth.models import User
from tweet.models import Tweet

# Create your views here.
@login_required(login_url='/login')
def follow_user(request, name):
    user= request.user
    followee = User.objects.get(username=name)
    follow = Follower( user=user,following= followee)
    follow.save()
    followers_feed(request)
    return render(request, 'user/follow.html')


@login_required(login_url='/login')
def followers_feed(request):
    user = request.user
    followers = Follower.objects.filter(user=user).distinct().values_list('following',flat=True)
    tweets = Tweet.objects.filter(author_id__in=followers).order_by('-created_at')
    context  = {'tweets': tweets}
    return render(request, 'user/followersfeed.html', context)
