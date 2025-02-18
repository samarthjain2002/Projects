from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from .views import RegisterView, LoginView, TaskListCreateView, TaksDetailView, ResetTokenView, LogoutView


urlpatterns = [
    path("register/", RegisterView.as_view(), name = "register"),
    path("login/", LoginView.as_view(), name = "login"),
    path("todos/", TaskListCreateView.as_view(), name = "task-list-create"),
    path("todos/<int:pk>/", TaksDetailView.as_view(), name = "task-detail"),
    path("reset-token/", ResetTokenView.as_view(), name="reset-token"),
    path("logout/", LogoutView.as_view(), name="logout"),
]