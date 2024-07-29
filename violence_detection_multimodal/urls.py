from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

from . import views

app_name = 'colorapp'

urlpatterns = [
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('login', views.about, name='login'),
    path('report', views.report, name='report'),
    path('livereport', views.livereport, name='livereport'),
    path('signup', views.signup, name='signup'),
    path('story', views.story, name='story'),
    path('location', views.location, name='location'),
    path('showvideo', views.showvideo, name='showvideo'),
    path('predictViolence', views.predictViolence, name = 'PredictViolence'),
    path('predictSOS', views.predictSOS, name = 'PredictSOS'),
    path('getmylocation', views.getmylocation, name = 'getmylocation')
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)