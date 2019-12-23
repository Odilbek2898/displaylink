from django.urls import path

from . import views

app_name = 'bek'
urlpatterns =  [
    path('', views.index, name = 'index'),
    # path('<int:registration_UserName_id>/', views.detail, name = 'detail'),
]