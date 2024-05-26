from django.urls import path
from . import views

app_name = 'cashback'

urlpatterns = [
    #views
    path('', views.view_login, name='view_login'),
    path('view_register', views.view_register, name='view_register'),
    path('view_user', views.view_user, name='view_user'),
    path('view_admin', views.view_admin, name='view_admin'),
    #functionalities
    path('create_user', views.create_user, name='create_user'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('add_to_budget', views.add_to_budget, name='add_to_budget'),
    path('remove_from_budget', views.remove_from_budget, name='remove_from_budget'),
]
