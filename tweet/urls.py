from django.urls import path
from .views import posttweet,my_tweets,get_all_tweets,profileview,user_profile_view


urlpatterns = [
    path(r'^globalfeed/', get_all_tweets, name='globalfeed'),
    # path('my_tweets', my_tweets,name="my_tweets"),
    # path('wall' , posttweet),
    # path('profile/<str:name>/', profileview),
]
