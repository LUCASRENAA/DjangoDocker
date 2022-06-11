from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('logout/', views.logout_user),

    path('login/', views.login_user),
    path('login/submit', views.submit_login),





]