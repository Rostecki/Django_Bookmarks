from django.urls import path
from . import views


app_name = 'bookmarks'

urlpatterns = [
    # Widoki logowania
    path('login/', views.user_login, name='login')
]
