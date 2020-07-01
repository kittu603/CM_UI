from django.urls import path,include
from . import views

app_name = "UI"


urlpatterns = [
    path('', views.index , name = 'index'),
    path('api/', views.apiTab , name = 'apiTab'),
    path('sql/', views.sqlTab, name = 'sqlTab'),
    path('ssh/', views.sshTab, name = 'sshTab'),
]