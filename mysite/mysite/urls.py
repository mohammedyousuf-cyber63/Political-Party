"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('use_auth/', include('user_auth.urls')),
    # ex: /home/
    path("", views.IndexView.as_view, name='index'),
    # ex: /home/5/
    path('<int:question_id>/', views.DetailView.as_view, name='detail'),
    # ex: /home/5/results/
    path('<int:question_id>/results/', views.ResultsView.as_view, name='results'),
    # ex: /home/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # event page
    path('event/', views.event_page, name='event')
]