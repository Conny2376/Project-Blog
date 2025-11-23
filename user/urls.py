from django.urls import path
from user import views

urlpatterns = [
    path(r"", views.HomePage.as_view())
]
