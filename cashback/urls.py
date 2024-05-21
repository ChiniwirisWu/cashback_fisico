from django.urls import path
from . import views

app_name = 'cashback'

urlpatterns = [
    path('', views.view_login, name='view_login'),
    path('view_register', views.view_register, name='view_register'),
    path('view_user', views.view_user, name='view_user'),
    path('view_admin', views.view_admin, name='view_admin')
]
