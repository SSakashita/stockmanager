from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name="login"),
    path('logout/', views.MyLogoutView.as_view(), name="logout"),
    path('mypage/',views.mypage, name="mypage"),
    path("create/", views.UserCreateView.as_view(), name="create"),
]