from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('index1', views.index1, name = "index1"),
    path('counter', views.counter, name = "counter"),
    path('register', views.register, name = "register"),
    path('login', views.login, name = "login"),
    path('logout', views.logout, name = "logout"),
    path('post/<str:pk>', views.post, name = "post"),
    path('blog', views.blog, name = "blog"),
]