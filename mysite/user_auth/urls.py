# urls for user_auth app
# Below I imported path from 'django.urls'
from django.urls import path
from django.contrib.auth import views as django_auth_views
# Below I imported views from '. import'
from . import views
from .views import SignUpView

# install app 
# list of urls to sign up, show_user, logout, authentication 
app_name = 'user_auth'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user, 
         name='authenticate_user'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('show_user/', views.show_user, name="show_user"),
    path('logout/', django_auth_views.LogoutView.as_view(
        template_name='registration/logout.html',), name='logout'),
]
