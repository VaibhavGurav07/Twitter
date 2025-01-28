from django.urls import path
from . import views

urlpatterns = [
    path('',views.tweet_list, name='tweet_list'),
    
    path('create/',views.tweet_create, name='tweet_create'),
    
    path('<int:tweet_id>/edit/',views.tweet_edit, name='tweet_edit'),
    
    path('<int:tweet_id>/delete/',views.tweet_delete, name='tweet_delete'),

    path('register/',views.Register,name='register'),

    path('accounts/login/',views.login_user, name="login_user"),

    path("logout/",views.User_logout, name="logout_user"),


    # path('search/',views.search, name='search')
    
]