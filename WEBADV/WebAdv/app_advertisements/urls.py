from django.urls import path
from .views import index, top_sellers, advertisement_post, register, login, profile

urlpatterns = [
    path('', index, name='main_page'),
    path('top_sellers/', top_sellers, name='top_sellers'),
    path('advertisement_post/', advertisement_post, name='advertisement_post'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
]
