from django.urls import path,include
# from login_app import views or
from . import views

app_name = 'login_app'

urlpatterns = [
    path('',views.index,name='index'),
]
