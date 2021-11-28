"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import tweet as home
from django.urls.conf import include
from followers.views import followers_feed
from userauth.views import (loginUser,logoutUser,registerUser)
from tweet.views import my_tweets,posttweet,get_all_tweets,profileview,user_profile_view
from followers.views import follow_user

urlpatterns = [
    path('', my_tweets),
    # path('globalfeed/', get_all_tweets),
    path('login', loginUser),
    path('logout/', logoutUser),
    path('register', registerUser),
    path('admin/', admin.site.urls),
    path(r'^twitter/', include('tweet.urls')),
    path('my_tweets', my_tweets),
    path('wall' , posttweet),
    path('profile/<str:name>/', profileview),
    path('followed/<str:name>/', follow_user ),
    path('followersfeed' ,followers_feed),
    path('userprofile', user_profile_view),
]
